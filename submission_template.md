# AI Code Review Assignment (Python)

## Candidate
- Name: Kalkidan Tadesse
- Approximate time spent: 1hr and 15 mins

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Incorrect denominator while averaging the total of non-cancelled orders by the total number of orders which includes the cancelled ones.

### Edge cases & risks
- Division by zero in case of orders list being empty causes a ZeroDivisionError.
- All orders are cancelled which results averaging 0 with non-zero value.
- Missing validation of keys(amount and status)having no value.

### Code quality / design issues
- Count variable misleading by suggesting it represents the number of orders being averaged but in reality it represents all orders. 
- No input validation to check the input is a list or that each order is a dictionary.
- The filtering is only applied to numerator. 
- No docstring or comments explain the function's purpose, parameters, or return value.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Improve variable naming for clarity
- Add input validation for missing keys
- Add protection against division by zero
- Fix the denominator to count only non-cancelled orders
- Add proper documentation

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
1. Test that the function handles an empty list gracefully. To ensure the function doesn’t crash with a ZeroDivisionError and instead returns a safe default (e.g., 0.0) as specified, since dividing by zero is undefined but the business may expect a neutral value.
2. Verify the function correctly handles the case where no valid orders exist for averaging. This is a critical edge case where the numerator is 0 and the count of valid orders is 0. The function must avoid division by zero and return a consistent result (like 0.0) to prevent runtime errors and align with documented behavior.
3. Test with orders that are missing the status or amount keys. The function uses direct key access (order["status"]), which raises a KeyError if keys are missing. Testing this ensures the function validates input structure and fails safely with a clear ValueError, improving robustness and debuggability.
4. Test with non-dictionary items in the orders list to verify robustness. If the function assumes all items are dictionaries, it will crash when accessing .get() or ["key"]. Validating type prevents unexpected exceptions and enforces contract expectations.
5. Test with very large amounts, negative amounts (if allowed), and single-order scenarios. Large numbers test floating-point precision and performance; negative amounts verify whether the logic accepts refunds or adjustments (as allowed by “numeric” type); single-order tests confirm the average isn’t skewed by off-by-one errors.
6. Test different capitalizations of "cancelled" (e.g., "Cancelled", "CANCELLED") if the business logic should be case-insensitive. Testing this clarifies whether the behavior is intentional (exact match only) or a hidden bug ensuring alignment with domain requirements.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The claim that the function correctly excludes cancelled orders from the calculation is incorrect and doesn't mention the flaw in the denominator.

### Rewritten explanation
- This function attempts to calculate the average order value by summing the amounts of non-cancelled orders. However, it contains a critical bug: while cancelled orders are properly excluded from the total sum, they are still included in the divisor (the total count of all orders). This results in an artificially deflated average. Additionally, the function lacks protection against division by zero when the orders list is empty and doesn't validate that order dictionaries contain the required keys. A correct implementation should divide the sum of non-cancelled order amounts by the count of non-cancelled orders only, and should handle edge cases like empty inputs or missing data gracefully.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The function contains a critical logical bug it divides the sum of non-cancelled order amounts by the total number of orders (including cancelled ones), which produces an incorrect average. This undermines the core purpose of the function. Additionally, it lacks protection against division by zero (e.g., empty input or all orders cancelled) and will crash on missing dictionary keys (KeyError). These issues make the code unsafe for production use without modifications.
- Confidence & unknowns: High confidence in the identified bugs based on code logic and standard Python behavior. However, there are unknowns around business requirements, such as:
    Should the average be 0, None, or raise an exception when no valid orders exist?
    Is status comparison case-sensitive? (e.g., "Cancelled" vs "cancelled")

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The function only checks for the presence of "0" in string, which is insufficient to validate an email address
- There is no structural validation indicating the valid email must have a non-empty local part and a non-empty domain part.

### Edge cases & risks
- A string with a single or multiple "@" will incorrectly be counted as valid.
- Leading or Trailing whitespace might be considered valid.
- Missing domain or username passing the current check.
- If the list contains non-string types, the code may raise a TypeError when checking "@" in email.

### Code quality / design issues
- Lack of input validation 
- No documentation or comments
- Inconsistency with real-world expectations of syntatic validity.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Must contain exactly one "@"
- The part before "@" must be non-empty
- The part after "@" must be non-empty and contain atleast one dot
- Add type safety 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
1. Test that the function handles an empty list gracefully.
To ensure the function doesn’t crash or raise an exception when given an empty input list, and instead returns 0 as a safe default
2. Verify the function correctly handles strings that contain "@" but are not valid email addresses.
The function must return 0 for these, as they violate the requirement of having exactly one "@" with non-empty local and domain parts.
3. Test with list items that are not strings (e.g., None, integers, dictionaries). Testing this confirms the function avoids AttributeError or TypeError during string operations.
4. Test with strings containing whitespace. Testing this reveals a limitation: the function may count syntactically invalid emails, highlighting a gap between intended and actual behavior that should be addressed or documented.

5. Test with valid-looking emails that lack a dot in the domain. Although such addresses can be valid in internal networks, the function’s design intentionally requires at least one dot in the domain for real-world relevance. Testing ensures these cases are correctly excluded, validating that the dot-check logic is enforced as specified in the docstring.
6. Test with international characters, uppercase domains, and complex but valid formats (e.g., "test.myuser+t@TEST.CO.ET").
These cases verify that the function focuses only on structural rules (one "@", non-empty parts, dot in domain) without imposing unnecessary restrictions like case sensitivity or ASCII-only assumptions ensuring it remains permissive enough for realistic email diversity while still filtering out obvious invalid entries.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It claims to count valid email addresses misinterpretation of correctness.
- Vague about invalid entries without specifying what constitutes invalid.
- While the handling of empty input is true it is also misleading since it doesn't address deeper flaws.

### Rewritten explanation
- This function attempts to count email-like strings in a given list using basic syntactic rules. It considers an entry valid only if it is a string containing exactly one '@' symbol, with non-empty text before and after the '@', and at least one dot in the domain part (e.g., "user@example.com"). Non-string items are skipped, and malformed or incomplete addresses (like "user@", "@domain", or "user@@example.com") are excluded. Note that this is not a full email validator per internet standards but a practical heuristic for common use cases.

## 4) Final Judgment
- Decision: Reject
- Justification: The original implementation is fundamentally flawed, it misidentifies many invalid strings as valid emails, which could lead to data corruption, security issues (e.g., in user registration), or incorrect analytics. The proposed fix introduces reasonable, real-world validation that balances correctness and simplicity without overcomplicating the logic. While not RFC-compliant, it aligns with typical application needs.
- Confidence & unknowns:
High confidence in the corrected approach for general-purpose use.
Unknowns:
Whether the system requires support for dotless domains (e.g., internal networks using user@mailserver). If so, the dot requirement could be made optional via a parameter.
Whether case sensitivity or Unicode emails matter (unlikely for basic counting).

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Incorrect divisor which considers the total count of all input elements.

### Edge cases & risks
- All values are None: Leads to division by zero if the logic were corrected to count only valid values but currently, it would return 0.0 / len(values) = 0.0, which is misleading (should raise an error or return None).
Empty input list: len(values) == 0 causes ZeroDivisionError on return total / count.
Non-numeric non-None values: Passing strings like "abc" or other uncastable types will raise a ValueError during float(v).
Mixed types: While float(v) handles ints and numeric strings, it fails on unexpected types.

### Code quality / design issues
- Misleading variable name: count suggests it tracks valid items, but it actually stores total length.
- No input validation or error handling.
- No documentation or type hints.
- Logic conflates "total items" with "valid items", reducing clarity.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Replace count = len(values) with a counter that increments only for valid (non-None) values.
- Handle edge cases: empty list and all-None inputs.
- Add basic error resilience or clear contract (e.g., assume inputs are either None or numeric/numeric-string).
- Improve variable naming and add comments.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

1. Normal case: Mix of numbers and None → verify correct average.
2. All valid: No None → should match standard average.
3. All None: Should raise ValueError (or handle per spec).
4. Empty list: Must raise ValueError.
5. Single valid value: Ensure no off-by-one errors.
6. Numeric strings: e.g., "3.5" → should be accepted.
7. Invalid non-None values: e.g., "abc", objects → expect ValueError.
8. Integers and floats mixed: Ensure type conversion works.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Claims it "averages the remaining values" but the code divides by the original list length.
- Says it safely handles mixed input types but will crash on non-float

### Rewritten explanation
- This function computes the arithmetic mean of valid measurements in a list, where valid entries are those that are not None and can be converted to a float. It sums all valid values and divides by the number of valid entries not the total list length. The function raises a ValueError if the input list is empty or contains no valid measurements. Note that non-None values that cannot be converted to floats (e.g., strings like "N/A") will cause a TypeError or ValueError.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation contains a critical mathematical error that invalidates its core purpose. It returns a biased (too low) average whenever None values are present. Additionally, it lacks handling for common edge cases (empty input, all-None), making it unreliable in real-world use.

- Confidence & unknowns: High confidence in bug identification. Unknowns include whether the system expects silent failure (e.g., returning None instead of raising) or tolerance for non-numeric strings but these can be clarified via requirements. The fix aligns with standard statistical practice for handling missing data.

