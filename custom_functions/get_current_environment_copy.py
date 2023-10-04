def get_current_environment_copy(**kwargs):
    """
    Returns the current running environment (phantom-dev.transurban.com or phantom.transurban.com) to allow swapping test/prod variables automatically in playbooks.
    
    Returns a JSON-serializable object that implements the configured data paths:
        environment
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    from urllib.parse import urlparse
    
    # Return only the netloc section of the URL
    try:
        outputs = {
            'environment': urlparse(phantom.get_base_url())[1],
            'status': 'success',
            'message': 'Successfully returned current SOAR environment',
        }
        phantom.debug('Phantom URL: {}'.format(outputs['environment']))
    except Exception as e:
        outputs = {
            'status': 'failed',
            'message': 'Exception occured: {}'.format(e),
        }
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
