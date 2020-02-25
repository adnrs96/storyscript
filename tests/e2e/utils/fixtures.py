from os import path


from storyhub.sdk.ServiceWrapper import ServiceWrapper


test_dir = path.dirname(path.dirname(path.realpath(__file__)))


fixture_dir = path.join(test_dir, "..", "fixtures")
fixture_file = path.join(fixture_dir, "hub_fixture.json.fixed")

hub = ServiceWrapper.from_json_file(fixture_file)
