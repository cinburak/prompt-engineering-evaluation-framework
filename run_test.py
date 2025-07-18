from prompt_eval.evaluators.match import ExactMatchEvaluator

def main():
    """
    Runs a simple test for the ExactMatchEvaluator.
    """
    print("--- Running ExactMatchEvaluator Test ---")

    # 1. Initialize the evaluator
    evaluator = ExactMatchEvaluator()

    # 2. Define test cases
    # Case 1: Should be a perfect match (score: 1.0)
    case_1_generated = "hello world"
    case_1_reference = "  HELLO WORLD  "

    # Case 2: Should not match (score: 0.0)
    case_2_generated = "hello world"
    case_2_reference = "hello there"

    # 3. Run evaluations and print results
    print("\nTesting Case 1 (Should Match):")
    print(f"  Generated: '{case_1_generated}'")
    print(f"  Reference: '{case_1_reference}'")
    result_1 = evaluator.evaluate(case_1_generated, case_1_reference)
    print(f"  Result -> Score: {result_1['score']}, Reasoning: {result_1['reasoning']}")

    print("\nTesting Case 2 (Should NOT Match):")
    print(f"  Generated: '{case_2_generated}'")
    print(f"  Reference: '{case_2_reference}'")
    result_2 = evaluator.evaluate(case_2_generated, case_2_reference)
    print(f"  Result -> Score: {result_2['score']}, Reasoning: {result_2['reasoning']}")

    print("\n--- Test Finished ---")

if __name__ == "__main__":
    main()