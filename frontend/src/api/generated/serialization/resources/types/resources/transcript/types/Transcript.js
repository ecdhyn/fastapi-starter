/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../../../core";
export const Transcript = core.serialization
    .object({
    id: core.serialization.string(),
})
    .extend(core.serialization.lazyObject(async () => (await import("../../../../..")).types.TranscriptRequest));