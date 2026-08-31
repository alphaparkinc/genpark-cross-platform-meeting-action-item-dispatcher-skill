from client import CrossPlatformMeetingActionItemDispatcherClient

def main():
    client = CrossPlatformMeetingActionItemDispatcherClient()
    res = client.dispatch_meeting_action_items('## Design Sync\n- Charlie to finalize dark mode tokens\n- Dave to prepare Figma handoff', ['SLACK', 'JIRA'])
    print('Meeting Action Item Dispatcher: ' + res['dispatch_job_id'] + ' (' + str(res['extracted_action_items_count']) + ' items)')
    print('Resolution Accuracy: ' + str(res['assignee_resolution_accuracy_pct']) + '% | Status: ' + res['workspace_sync_status'])
    print('Sync Targets: ' + ', '.join(res['sync_target_destinations']))
    print('Summary URL: ' + res['dashboard_summary_url'])

if __name__ == '__main__':
    main()
