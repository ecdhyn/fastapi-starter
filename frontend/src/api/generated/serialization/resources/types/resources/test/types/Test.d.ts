/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../../..";
import { ProManApi } from "../../../../../..";
import * as core from "../../../../../../core";
export declare const Test: core.serialization.Schema<serializers.types.Test.Raw, ProManApi.types.Test>;
export declare namespace Test {
    type Raw = Test.ExactMatch | Test.Regex | Test.SemanticSimilarity | Test.JsonValidity;
    interface ExactMatch extends serializers.types.ExactMatchTest.Raw {
        TestType: "exact_match";
    }
    interface Regex extends serializers.types.RegexTest.Raw {
        TestType: "regex";
    }
    interface SemanticSimilarity extends serializers.types.SemanticSimilarityTest.Raw {
        TestType: "semantic_similarity";
    }
    interface JsonValidity extends serializers.types.JsonValidityTest.Raw {
        TestType: "json_validity";
    }
}
