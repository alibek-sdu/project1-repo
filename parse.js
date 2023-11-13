import puppeteer from "puppeteer";

function delay(time) {
  return new Promise(function (resolve) {
    setTimeout(resolve, time);
  });
}

let products = [](async () => {
  // Launch the browser and open a new blank page
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });
  const page = await browser.newPage();

  // Navigate the page to a URLÌ
  const res = await page.goto("https://www.technodom.kz/");

  const openCategoriesModal = async (
    categoryIndex,
    submenuId,
    subcategoryIndex
  ) => {
    console.log(categoryIndex, submenuId, subcategoryIndex);
    const clickResult = await page.waitForSelector(".Desktop_catalog__9Dyq2");

    await Promise.all([
      //Click catalog
      clickResult.evaluate((el) => el.click()),
    ]);

    await delay(1000);

    const categories = await page.$$("li > .MenuLink_root__YQd1_");

    if (categories.length <= categoryIndex) {
      return;
    }
    const category = categories[categoryIndex];

    if (category) {
      await category.hover();
      await delay(1000);
      const subcategories = await page.$$(".SubMenu_main__H1ew0 > div"); //find subcategories

      if (subcategories.length <= submenuId) {
        // reclick on top modal
        await Promise.all([clickResult.evaluate((el) => el.click())]);
        await delay(1000);
        return await openCategoriesModal(categoryIndex + 1, 0, 0);
      }
      const subcategory = subcategories[submenuId];

      if (subcategory) {
        const subcategoryList = await subcategory.$$(
          ".SubMenu_list__oBMB2 > li > a"
        );
        const subcategoryLink = await subcategory.waitForSelector(
          ".SubMenu_titleLink__nuBQV"
        );

        if (subcategoryList.length <= subcategoryIndex) {
          await Promise.all([clickResult.evaluate((el) => el.click())]);
          await delay(1000);
          return await openCategoriesModal(categoryIndex, submenuId + 1, 0);
        }
        const subcategoryListItem = subcategoryList[subcategoryIndex];
        if (subcategoryListItem) {
          await Promise.all([
            await subcategoryListItem.evaluate((el) => el.click()),
            await page.waitForNavigation(),
          ]);
        }
        await delay(1000);

        // Function to extract product details from a product card
        async function extractProductDetails() {
          return await page.evaluate(() => {
            const productTitle = document
              .querySelector(".ProductCardV_title__rFAYr")
              .textContent.trim();
            const productRating = document
              .querySelector(".RatingAndReviewsCount_rating__xG62B")
              .textContent.trim();
            const productReviews = document
              .querySelector(".RatingAndReviewsCount_review__EiJSu")
              .textContent.trim();
            const productPrice = document
              .querySelector(".ProductCardPrices_price__5dlTx")
              .textContent.trim();
            const productOldPrice = document
              .querySelector(".ProductCardPrices_oldPrice__lrAgm")
              .textContent.trim();

            return {
              productTitle,
              productRating,
              productReviews,
              productPrice,
              productOldPrice,
            };
          });
        }

        // Recursive function to navigate through pagination
        async function scrapePage() {
          // Wait for the product cards to be visible
          await page.waitForSelector(".ProductCardV_card__pIoz2");

          // Extract product details from all product cards on the page
          const productsByPage = await page.evaluate(() => {
            const productCards = document.querySelectorAll(
              ".ProductCardV_card__pIoz2"
            );
            const productData = [];
            productCards.forEach((card) => {
              const productDetails = {
                productCard: card.innerHTML,
              };
              productData.push(productDetails);
            });
            return productData;
          });

          // Output product details
          console.log("Products on this page:", productsByPage);
          products.push(productsByPage);

          // Go to the next page if available
          const nextPageButton = await page.$(
            ".Paginator__List-ArrowIcon-Right"
          );
          if (nextPageButton) {
            await nextPageButton.click();
            await delay(2000); // Wait for the page to load, adjust the timeout as needed
            await scrapePage(); // Recursively call scrapePage for the next page
          }
        }

        // Start scraping
        await scrapePage();

        return await openCategoriesModal(
          categoryIndex,
          submenuId,
          subcategoryIndex + 1
        );
      } else {
        await delay(1000);
        return await openCategoriesModal(categoryIndex, submenuId + 1, 0);
      }
    } else {
      await delay(1000);
      return await openCategoriesModal(categoryIndex + 1, 0, 0);
    }
  };

  await browser.close();
})();
