/**
 * This file was auto-generated by Fern from our API Definition.
 */
import { ProManApi } from "../../../../../..";
export declare type Test = ProManApi.types.Test.ExactMatch | ProManApi.types.Test.Regex | ProManApi.types.Test.SemanticSimilarity | ProManApi.types.Test.JsonValidity;
export declare namespace Test {
    interface ExactMatch extends ProManApi.types.ExactMatchTest {
        testType: "exact_match";
    }
    interface Regex extends ProManApi.types.RegexTest {
        testType: "regex";
    }
    interface SemanticSimilarity extends ProManApi.types.SemanticSimilarityTest {
        testType: "semantic_similarity";
    }
    interface JsonValidity extends ProManApi.types.JsonValidityTest {
        testType: "json_validity";
    }
}