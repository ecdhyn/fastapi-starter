/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../../..";
import { ProManApi } from "../../../../../..";
import * as core from "../../../../../../core";
export declare const Prompt: core.serialization.ObjectSchema<serializers.types.Prompt.Raw, ProManApi.types.Prompt>;
export declare namespace Prompt {
    interface Raw {
        id: string;
        name: string;
        content: string;
        transcripts: serializers.types.Transcript.Raw[];
        tags: serializers.types.Tag.Raw[];
        deployment_tag: serializers.types.DeploymentTag.Raw;
        create_time: string;
        prompt_variables: string[];
        version_context: serializers.types.VersionContext.Raw;
        additional_comments: string;
    }
}
