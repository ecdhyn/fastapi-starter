/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../../..";
import { ProManApi } from "../../../../../..";
import * as core from "../../../../../../core";
export declare const RegexTest: core.serialization.ObjectSchema<serializers.types.RegexTest.Raw, ProManApi.types.RegexTest>;
export declare namespace RegexTest {
    interface Raw {
        id: string;
        name: string;
        is_passed: boolean;
        target: string;
    }
}
