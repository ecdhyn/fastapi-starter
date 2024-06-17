/**
 * This file was auto-generated by Fern from our API Definition.
 */
export interface TranscriptEvaluation {
    /** the unique ArgoID for the transcript evaluation */
    id: string;
    /** name of transcript evaluation */
    name: string;
    /** content of the transcript evaluation */
    content: string;
    /** the ArgoID of the associated transcript */
    transcriptId: string;
    /** the ArgoID of the associated prompt */
    promptId: string;
    /** a score from 0 to 1 identifying how well the transcript did */
    score: number;
}