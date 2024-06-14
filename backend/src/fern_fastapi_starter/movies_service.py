from .api.generated.prompt_api.service.service import AbstractPromptApiService
from .api.generated.types import Prompt, VersionContext, Tag, DeploymentTag, FunctionCall, ToolCall, Transcript, TranscriptEntry, TranscriptEvaluation, TranscriptRequest
from .api.generated import ApiAuth 

class ProManServices(AbstractPromptApiService):
    
    def get_prompt(self, *, phone_number: str, auth: ApiAuth) -> Prompt:
        return Prompt(
            id="ArgoID",
            name="Our First Prompt!",
            content="You are an agent of good. Act like it!",
            transcripts=[
                Transcript(
                    call_end_time="2023-01-01T01:00:00Z",
                    call_sid="ABC123",
                    call_start_time="2023-01-01T00:30:00Z",
                    customer_phone_number=phone_number,
                    id="transcriptID",
                    merchant_id="merchantID",
                    merchant_phone_number="555-1234",
                    prompt_content="Please provide your order number.",
                    prompt_id="promptID",
                    prompt_variables=["order_number"],
                    transcript_content=[
                        TranscriptEntry(
                            role="agent",
                            content="Can I have your order number, please?",
                            name="Agent Smith",
                            tool_call_id="toolCallID",
                            tool_calls=[
                                ToolCall(
                                    index=0,
                                    id="toolCallID1",
                                    function=FunctionCall(
                                        arguments="{'order_number': '12345'}",
                                        name="getOrderStatus"
                                    ),
                                    type="API"
                                )
                            ]
                        )
                    ]
                )
            ],
            tags=[
                Tag(id="tag1", name="priority")
            ],
            deployment_tag=DeploymentTag.DEVELOPMENT,
            create_time="2023-01-01T00:00:00Z",
            prompt_variables=["order_number"],
            version_context=VersionContext(
                parent_id="parentPromptID",
                children_ids=["childPromptID1", "childPromptID2"]
            ),
            additional_comments="This is a sample prompt."
        )

    def post_transcript(self, *, body: TranscriptRequest, prompt_id: str, auth: ApiAuth) -> Transcript:
        pass