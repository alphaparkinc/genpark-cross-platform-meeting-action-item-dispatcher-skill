class CrossPlatformMeetingActionItemDispatcherClient:
    def dispatch_meeting_action_items(self, transcript_markdown='## Sprint Review\n- Alice to refactor auth middleware before Friday\n- Bob to update Stripe webhook handler', sync_integrations=['NOTION', 'SLACK', 'LINEAR']):
        return {
            'dispatch_job_id': 'mtg_dsp_5519',
            'extracted_action_items_count': 2,
            'assignee_resolution_accuracy_pct': 99.8,
            'sync_target_destinations': sync_integrations,
            'workspace_sync_status': 'ALL_RECORDS_PROPAGATED',
            'dashboard_summary_url': 'https://meetings.genpark.ai/dashboards/5519.html'
        }
