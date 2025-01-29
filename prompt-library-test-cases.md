# Guide for generating test cases

## Format
1. Generate a CSV with pipe symbol as delimiter

2. Aim for high coverage, but prioritize test quality

3. Generate at least 15 test cases from each feature including: positive and negative scenarios with different test data

4. Use the following columns:
- Test Scenario ID: Use format Test_Scenario #001
- User Role
- Scenario Description: Include name of the feature and use clear descriptions referencing the business value for testing this component
- Steps to Execute: Add specific steps including interaction with UI components or APIs
- Test Data
- Expected Results: Test both positive and negative scenarios
- Actual Results: [entered manually by user]
- Status (Pass/Fail): [entered manually by user]