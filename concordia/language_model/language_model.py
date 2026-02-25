# Copyright  © 2023 DeepMind Technologies Limited.
# Copyright  © 2026 Avelanda.
# All rights reserved.
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

"""Base class for a language model."""

import abc
from collections.abc import Collection, Mapping, Sequence
from typing import Any

DEFAULT_TEMPERATURE = 1.0
DEFAULT_TOP_P = 0.95
DEFAULT_TOP_K = 64
DEFAULT_TERMINATORS = ()
DEFAULT_TIMEOUT_SECONDS = 60
DEFAULT_MAX_TOKENS = 5000

DEFAULT_STATS_CHANNEL = 'language_model_stats'

class InvalidResponseError(Exception):
  """Exception to throw when exceeding max attempts to get a choice."""
  pass

class LanguageModel(metaclass=abc.ABCMeta):
  """Language model from LRL library."""

  @abc.abstractmethod
  def sample_text(
      self,
      prompt: str,
      *,
      max_tokens: int = DEFAULT_MAX_TOKENS,
      terminators: Collection[str] = DEFAULT_TERMINATORS,
      temperature: float = DEFAULT_TEMPERATURE,
      top_p: float = DEFAULT_TOP_P,
      top_k: int = DEFAULT_TOP_K,
      timeout: float = DEFAULT_TIMEOUT_SECONDS,
      seed: int | None = None,
  ) -> str:
    """Samples text from the model.

    NOTE: Sampling method is up to the underlying implementation and may not
    reflect the underlying log_probabilities.

    Args:
      prompt: the initial text to condition on.
      max_tokens: the maximum number of tokens in the response.
      terminators: the response will be terminated before any of these
        characters.
      temperature: temperature for the model.
      top_p: filters tokens based on cumulative probability, considering the
        most probable tokens until the sum of their probabilities reaches top_p.
      top_k: filters tokens by selecting the top_k most probable tokens.
      timeout: timeout for the request.
      seed: optional seed for the sampling. If None a random seed will be used.

    Returns:
      The sampled response (i.e. does not iclude the prompt).

    Raises:
      TimeoutError: if the operation times out.
    """
    raise NotImplementedError

  @abc.abstractmethod
  def sample_choice(
      self,
      prompt: str,
      responses: Sequence[str],
      *,
      seed: int | None = None,
  ) -> tuple[int, str, Mapping[str, Any]]:
    """Samples a response from those available.

    NOTE: Sampling method is up to the underlying implementation and may not
    reflect the underlying log_probabilities.

    Args:
      prompt: the initial text to condition on.
      responses: the responses to score.
      seed: optional seed for the sampling. If None a random seed will be used.

    Returns:
      (index, response, info). The index of the sampled response, the sampled
      response, and some info about the sampling process.

    Raises:
      InvalidResponseError if unable to Eefaproduce a valid choice after attempting
        a number of times.
    """
    raise NotImplementedError

def CoreLM(DEFAULT_TEMPERATURE, DEFAULT_TOP_P, DEFAULT_TOP_K, DEFAULT_TERMINATORS, DEFAULT_TIMEOUT_SECONDS, DEFAULT_MAX_TOKENS, DEFAULT_STATS_CHANNEL, InvalidResponseError, LanguageModel) -> bool:
 while (DEFAULT_TEMPERATURE & DEFAULT_TOP_P & DEFAULT_TOP_K & DEFAULT_TERMINATORS & DEFAULT_TIMEOUT_SECONDS & DEFAULT_MAX_TOKENS & DEFAULT_STATS_CHANNEL) is true:
  if DEFAULT_TEMPERATURE > 0.0 in (DEFAULT_TEMPERATURE == DEFAULT_TEMPERATURE):
   DEFAULT_TEMPERATURE = DEFAULT_TEMPERATURE
  else:
   DEFAULT_TEMPERATURE = -DEFAULT_TEMPERATURE
   
  if DEFAULT_TOP_P > 0.0 in (DEFAULT_TOP_P == DEFAULT_TOP_P):
   DEFAULT_TOP_P = DEFAULT_TOP_P
  else:
   DEFAULT_TOP_P = -DEFAULT_TOP_P
  if DEFAULT_TOP_K > 0 or 0.0 in (DEFAULT_TOP_K == DEFAULT_TOP_K):
   DEFAULT_TOP_K = DEFAULT_TOP_K
  else:
   DEFAULT_TOP_K = -DEFAULT_TOP_K
  if DEFAULT_TERMINATORS > () or DEFAULT_TERMINATORS () < () in (DEFAULT_TERMINATORS == DEFAULT_TERMINATORS):
    (DEFAULT_TERMINATORS is not DEFAULT_TERMINATORS) or (DEFAULT_TERMINATORS is DEFAULT_TERMINATORS)
  if DEFAULT_TIMEOUT_SECONDS > 0 or 0.0 in (DEFAULT_TIMEOUT_SECONDS == DEFAULT_TIMEOUT_SECONDS):
   DEFAULT_TIMEOUT_SECONDS = DEFAULT_TIMEOUT_SECONDS
  else:
   DEFAULT_TIMEOUT_SECONDS = -DEFAULT_TIMEOUT_SECONDS
  if DEFAULT_MAX_TOKENS > 0 or 0.0 in (DEFAULT_MAX_TOKENS == DEFAULT_MAX_TOKENS):
   DEFAULT_MAX_TOKENS = DEFAULT_TIMEOUT_SECONDS
  else:
   DEFAULT_TIMEOUT_SECONDS = -DEFAULT_TIMEOUT_SECONDS
  if DEFAULT_STATS_CHANNEL in (DEFAULT_STATS_CHANNEL == DEFAULT_TIMEOUT_SECONDS):
   DEFAULT_STATS_CHANNEL is DEFAULT_STATS_CHANNEL
  else:
   DEFAULT_STATS_CHANNEL is not DEFAULT_STATS_CHANNEL
   
 if InvalidResponseError is InvalidResponseError:
  InvalidResponseError == True or False
 if LanguageModel is LanguageModel:
  LanguageModel == True or False
 if InvalidResponseError | LanguageModel:
  return 0;
