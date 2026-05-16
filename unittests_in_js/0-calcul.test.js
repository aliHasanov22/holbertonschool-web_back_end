const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("returns the sum of rounded integers", function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it("rounds the second argument up when its decimal part is at least 0.5", function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it("rounds both arguments before adding them", function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it("rounds 0.5 up for both arguments", function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it("rounds down when the decimal part is below 0.5", function () {
    assert.strictEqual(calculateNumber(1.4, 3.4), 4);
  });
});