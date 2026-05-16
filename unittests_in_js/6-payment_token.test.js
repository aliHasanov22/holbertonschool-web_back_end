const assert = require("assert");
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("getPaymentTokenFromAPI", function () {
  it("returns the expected object when successful", function (done) {
    getPaymentTokenFromAPI(true).then((response) => {
      assert.deepStrictEqual(response, { data: "Successful response from the API" });
      done();
    });
  });
});