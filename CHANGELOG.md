# Changelog

## Repository Completion and Enhancements

This document summarizes all the bug fixes, enhancements, and improvements made to complete the VietLegalQA repository.

## Bug Fixes

### 1. Syntax Error in `utils.py`
- **File**: `vietlegalqa/modules/construct/utils.py:85`
- **Issue**: Used `==` instead of `=` for default parameter
- **Fix**: Changed `threshold: Optional[int] == 3` to `threshold: Optional[int] = 3`

### 2. Missing Import in `constructor.py`
- **File**: `vietlegalqa/modules/construct/constructor.py`
- **Issue**: `Optional` type hint used but not imported
- **Fix**: Added `Optional` to imports from `typing` module

### 3. Incorrect Enumerate Usage in `extract_clauses_comma`
- **File**: `vietlegalqa/modules/construct/utils.py:109`
- **Issue**: Incorrect use of `enumerate()` in nested loop
- **Fix**: Changed `for next_clause in enumerate(...)` to `for next_clause in ...`

### 4. Comparison Operators Logic Errors in `QAPair`
- **File**: `vietlegalqa/data/qa.py`
- **Issues**: 
  - `__ne__` used `and` instead of `or` logic
  - `__lt__`, `__gt__`, `__le__`, `__ge__` had incorrect chaining logic
- **Fix**: 
  - Simplified `__ne__` to use `not self.__eq__()`
  - Fixed comparison logic to properly chain field comparisons
  - Simplified `__le__` and `__ge__` to use existing comparison methods

### 5. Wrong Field Constants in DocField and QAField
- **File**: `vietlegalqa/data/utils.py`
- **Issue**: Property methods returned wrong field indices (using `FIELD` instead of `DOC_FIELD`/`QA_FIELD`)
- **Fix**: Updated all property methods to use correct field constants

### 6. Bug in `to_dataset` Method
- **File**: `vietlegalqa/data/utils.py:320`
- **Issue**: Used `self.data.to_list()` but `self.data` is a dict, not a Dataset
- **Fix**: Changed to `self.to_list()`

### 7. Missing Dependencies in requirements.txt
- **File**: `requirements.txt`
- **Issue**: Missing `underthesea`, `torch`, and `tqdm` packages
- **Fix**: Added all missing dependencies

### 8. Script Argument Type Issues
- **File**: `script/answer_extraction.py`
- **Issues**: 
  - `verbose` argument type was `bool` instead of `int`
  - `use_gpu` should use `action='store_true'` for proper argparse handling
  - Missing function call in `is_available` check
  - Unused `output_file` argument
  - Typo in default output filename ("tvpl_contruct.pkl")
- **Fix**: 
  - Changed `verbose` to `int` type
  - Changed `use_gpu` to use `action="store_true"`
  - Fixed `is_available()` function call
  - Implemented `output_file` usage
  - Fixed typo and improved output path handling
  - Added help text for all arguments

### 9. Hardcoded ID Prefix
- **File**: `vietlegalqa/modules/construct/constructor.py:128`
- **Issue**: Used hardcoded "tvpl_" prefix instead of `id_prefix` parameter
- **Fix**: Changed to use `id_prefix` parameter

### 10. None Type Error in QAPair
- **File**: `vietlegalqa/data/qa.py:24`
- **Issue**: `type.upper()` called when `type` could be `None`
- **Fix**: Added null check: `type.upper() if type is not None else None`

### 11. Incorrect Type Hint for stanza_tokenizer
- **File**: `vietlegalqa/modules/construct/utils.py:35`
- **Issue**: Return type was `str` but function returns `List[List[str]]`
- **Fix**: Updated return type annotation

### 12. Bug in QADataset.get_article Method
- **File**: `vietlegalqa/data/qa.py:233`
- **Issue**: Incorrectly used `self.data[id]` as document key
- **Fix**: Extract article ID from QA pair and use it correctly

### 13. Dataset Loading Issues
- **File**: `vietlegalqa/data/load.py`
- **Issue**: Incorrect dataset splitting in tuple cases
- **Fix**: Fixed dataset loading to properly use split parameter

### 14. Dictionary Key Bug in Document and QADataset Initialization
- **Files**: `vietlegalqa/data/doc.py:87`, `vietlegalqa/data/qa.py:204`
- **Issue**: Used index as key instead of actual ID when loading from dict format
- **Fix**: Changed to use actual ID value as dictionary key

## Enhancements

### 1. Comprehensive README Documentation
- **File**: `README.md`
- **Enhancements**:
  - Added detailed project overview
  - Included installation instructions
  - Added quick start guide with examples
  - Documented project structure
  - Added methodology explanation
  - Included citation information
  - Added references to related papers

### 2. Subfolder Documentation
- **Files**: 
  - `vietlegalqa/data/README.md`
  - `vietlegalqa/modules/README.md`
  - `vietlegalqa/models/README.md`
  - `script/README.md`
- **Enhancements**: Created comprehensive documentation for each module/subfolder

## Code Quality Improvements

- Fixed all identified syntax errors
- Corrected type hints throughout the codebase
- Improved error handling consistency
- Fixed logical errors in comparison operators
- Standardized code patterns

## Repository Structure

The repository now follows proper Python package structure with:
- Proper `__init__.py` files in all packages
- Comprehensive documentation
- Clear module organization
- Well-documented scripts

## Testing Recommendations

While no automated tests were added in this round, the following areas should be tested:
1. Document loading from various sources
2. QA pair generation pipeline
3. Dataset export functionality
4. Comparison operators
5. Edge cases with None values

## Future Improvements

Potential areas for future enhancement:
1. Add unit tests
2. Add integration tests
3. Add type checking with mypy
4. Add CI/CD pipeline
5. Add setup.py or pyproject.toml for package installation
6. Add example notebooks showing usage
7. Add model training scripts
8. Improve error messages
