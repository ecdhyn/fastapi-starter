/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../../../core";
export const ToolCall = core.serialization.object({
    index: core.serialization.number(),
    id: core.serialization.string(),
    function: core.serialization.lazyObject(async () => (await import("../../../../..")).types.FunctionCall),
    type: core.serialization.string(),
});
