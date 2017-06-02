"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """A melon order with basic attributes."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = None
        self.tax = None

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            return total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, "USA")

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

        self.order_type = "international"
        self.tax = 0.17


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty, "GOV")

        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact that an inspection has been passed."""

        self.passed_inspection = passed

