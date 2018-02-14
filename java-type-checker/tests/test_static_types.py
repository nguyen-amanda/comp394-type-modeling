# -*- coding: utf-8 -*-

from java_type_checker import *
from tests.fixtures import Graphics
from tests.helpers import TypeTest
import unittest


class TestStaticTypes(TypeTest):

    def test_variable_static_type_is_its_declared_type(self):
        self.assertEqual(
            Graphics.point,
            Variable("p", Graphics.point).static_type())

    def test_literal_static_type_is_its_type(self):
        self.assertEqual(
            Type.int,
            Literal("3", Type.int).static_type())

    def test_null_literal_static_type_is_null(self):
        self.assertEqual(
            Type.null,
            NullLiteral().static_type())

    def test_method_call_static_type_is_method_return_type(self):
        # p.getX() → double
        self.assertEqual(
            Type.double,
            MethodCall(Variable("p", Graphics.point), "getX").static_type())

    def test_object_instantiation_static_type_is_the_instantiate_type(self):
        # new Point() → Point
        self.assertEqual(
            Graphics.point,
            ConstructorCall(Graphics.point).static_type())


if __name__ == '__main__':
    unittest.main()
