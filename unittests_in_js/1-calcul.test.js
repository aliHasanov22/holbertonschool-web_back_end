const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
  describe("SUM", function () {
    it("adds rounded numbers", function () {
      assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
    });

    it("handles values that round down", function () {
      assert.strictEqual(calculateNumber("SUM", 1.2, 4.2), 5);
    });
  });

  describe("SUBTRACT", function () {
    it("subtracts rounded numbers", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
    });

    it("handles values that round up and down", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.6, 4.2), -2);
    });
  });

  describe("DIVIDE", function () {
    it("divides rounded numbers", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });

    it("returns Error when the rounded denominator is 0", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
    });
  });
});