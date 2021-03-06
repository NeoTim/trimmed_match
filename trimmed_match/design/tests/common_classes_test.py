# Copyright 2020 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Tests for trimmed_match.design.common_classes."""

import pandas as pd

from trimmed_match.design import common_classes
import unittest

GeoXType = common_classes.GeoXType
GeoLevelData = common_classes.GeoLevelData
GeoLevelPotentialOutcomes = common_classes.GeoLevelPotentialOutcomes
TimeWindow = common_classes.TimeWindow


class CommonClassesTest(unittest.TestCase):

  def setUp(self):
    super().setUp()
    self._geox_outcome = GeoLevelData(1, 1.0, 2.0)
    self._potential_outcomes = GeoLevelPotentialOutcomes(
        GeoLevelData(1, 1.0, 2.0), GeoLevelData(1, 3.0, 4.0))
    self._t1 = pd.Timestamp("2019-01-01")
    self._t2 = pd.Timestamp("2020-01-01")

  def testGeoXType(self):
    for x in ["CONTROL", "GO_DARK", "HEAVY_UP", "HEAVY_DOWN", "HOLD_BACK"]:
      self.assertIn(x, GeoXType.__members__)
    self.assertNotIn("go-dark", GeoXType.__members__)

  def testGeoLevelData(self):
    self.assertEqual(1.0, self._geox_outcome.response)
    self.assertEqual(2.0, self._geox_outcome.spend)

  def testGeoLevelPotentialOutcomes(self):
    self.assertEqual(1.0, self._potential_outcomes.controlled.response)
    self.assertEqual(2.0, self._potential_outcomes.controlled.spend)
    self.assertEqual(3.0, self._potential_outcomes.treated.response)
    self.assertEqual(4.0, self._potential_outcomes.treated.spend)

  def testTimeWindow(self):
    result1 = TimeWindow(self._t1, self._t2)
    self.assertEqual(self._t1, result1.first_day)
    self.assertEqual(self._t2, result1.last_day)


if __name__ == "__main__":
  unittest.main()
