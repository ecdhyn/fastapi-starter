/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../../../core";
export const NotFoundErrorBody = core.serialization
    .object({})
    .extend(core.serialization.lazyObject(async () => (await import("../../../../..")).types.ErrorBody));
