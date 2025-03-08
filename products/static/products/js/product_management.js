// ====================================================================
// SCRIPTS FOR EDITING PRODUCTS
// ====================================================================
// Adds click handlers to delete buttons & confirmation modals

/**
* Initializes deletion functionality for the product delete buttons.
* 
* For each button in the `deleteProductBtns` collection:
* - Retrieves the associated Product's ID upon click.
* - Updates the `deleteProductConfirm` link's href to point to the 
* deletion endpoint for the specific Product.
* - Displays a confirmation modal (`deleteProductModal`) to prompt 
* the user for confirmation before deletion.
*/
const deleteProductBtns = document.getElementsByClassName("btn-delete-product");
const deleteProductModal = new bootstrap.Modal(document.getElementById("deleteProductModal"));
const deleteProductConfirm = document.getElementById("deleteProductConfirm");
const deleteProductName = document.getElementById("deleteProductName");
for (let button of deleteProductBtns) {
    button.addEventListener("click", (e) => {
      let productId = e.target.getAttribute("data-product_id");
      let productName = e.target.getAttribute("data-product_name");
      deleteProductConfirm.href = `delete/${productId}`;
      deleteProductName.innerHTML = `${productName}`;
      deleteProductModal.show();
    });
}