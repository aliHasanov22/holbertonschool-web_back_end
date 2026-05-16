const { expect } = require("chai");
const calculateNumber = require("./2-calcul_chai");

describe("calculateNumber", function () {
  describe("SUM", function () {
    it("adds rounded numbers", function () {
      expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });

    it("handles values that round down", function () {
      expect(calculateNumber("SUM", 1.2, 4.2)).to.equal(5);
    });
  });

  describe("SUBTRACT", function () {
    it("subtracts rounded numbers", function () {
      expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4);
    });

    it("handles values that round up and down", function () {
      expect(calculateNumber("SUBTRACT", 1.6, 4.2)).to.equal(-2);
    });
  });

  describe("DIVIDE", function () {
    it("divides rounded numbers", function () {
      expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);
    });

    it("returns Error when the rounded denominator is 0", function () {
      expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
    });
  });
});