/**
 * This file was auto-generated by Fern from our API Definition.
 */
export interface SemanticSimilarityTest {
    id: string;
    name: string;
    /** similarity score between 0 and 1 */
    score: number;
    /** the target phrase */
    target: string;
}
