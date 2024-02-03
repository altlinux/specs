%define  modulename httpretty

%def_with check

Name:    python3-module-%modulename
Version: 1.1.4
Release: alt2

Summary: HTTP client mocking tool for Python - inspired by Fakeweb for Ruby
License: MIT
Group:   Development/Python3
URL:     https://github.com/gabrielfalcao/HTTPretty

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-httpserver
BuildRequires: python3-module-sure
BuildRequires: python3-module-requests
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-httplib2
BuildRequires: python3-module-tornado
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-boto3
BuildRequires: python3-module-httpx
BuildRequires: python3-module-fakeredis
%endif

BuildArch: noarch

Source: %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/gabrielfalcao/HTTPretty/issues/405
export EVENTLET_NO_GREENDNS=yes
%pyproject_run_pytest -k "not test_http_passthrough \
    and not test_https_passthrough \
    and not test_httpretty_should_allow_forcing_headers_urllib2 \
    and not test_debug \
    and not test_httpretty_should_allow_registering_regexes_with_streaming_responses \
    and not test_httpretty_should_handle_paths_starting_with_two_slashes \
    and not test_httpretty_bypasses_when_disabled \
    and not test_httpretty_bypasses_a_unregistered_request \
    and not test_using_httpretty_with_other_tcp_protocols \
    and not test_disallow_net_connect_1 \
    and not test_recording_calls"

%files
%doc *.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Sat Feb 03 2024 Anton Vyatkin <toni@altlinux.org> 1.1.4-alt2
- Fixed FTBFS.

* Tue Dec 12 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.4-alt1
- Update version to 1.1.4.

* Thu Dec 03 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.3-alt1
- Splite python3 module from python-module-httpretty package
