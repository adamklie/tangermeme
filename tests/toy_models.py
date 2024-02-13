# toy_models.py
# Contact: Jacob Schreiber <jmschreiber91@gmail.com>

import torch
import pytest

from tangermeme.utils import one_hot_encode
from tangermeme.utils import random_one_hot

from nose.tools import assert_raises
from numpy.testing import assert_array_almost_equal


torch.manual_seed(0)
torch.use_deterministic_algorithms(True)


class SumModel(torch.nn.Module):
	def __init__(self):
		super(SumModel, self).__init__()
		
	def forward(self, X):
		return X.sum(axis=-1)


class FlattenDense(torch.nn.Module):
	def __init__(self):
		super(FlattenDense, self).__init__()

		self.dense = torch.nn.Linear(400, 3)

	def forward(self, X, alpha=0, beta=1):
		X = X.reshape(X.shape[0], 400)
		return self.dense(X) * beta + alpha


class Conv(torch.nn.Module):
	def __init__(self):
		super(Conv, self).__init__()
		self.conv = torch.nn.Conv1d(4, 12, (3,))


	def forward(self, X):
		return self.conv(X)


class Scatter(torch.nn.Module):
	def __init__(self):
		super(Scatter, self).__init__()

	def forward(self, X):
		return X.permute(0, 2, 1)


class ConvDense(torch.nn.Module):
	def __init__(self):
		super(ConvDense, self).__init__()

		self.dense = torch.nn.Linear(400, 3)
		self.conv = torch.nn.Conv1d(4, 12, (3,))

	def forward(self, X, alpha=0):
		return self.conv(X) + alpha, self.dense(X.reshape(X.shape[0], 400)) 