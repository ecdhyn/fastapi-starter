/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../../../core";
export const RegexTest = core.serialization.object({
    id: core.serialization.string(),
    name: core.serialization.string(),
    isPassed: core.serialization.property("is_passed", core.serialization.boolean()),
    target: core.serialization.string(),
});
