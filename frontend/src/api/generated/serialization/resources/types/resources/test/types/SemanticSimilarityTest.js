/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../../../core";
export const SemanticSimilarityTest = core.serialization.object({
    id: core.serialization.string(),
    name: core.serialization.string(),
    score: core.serialization.number(),
    target: core.serialization.string(),
});
