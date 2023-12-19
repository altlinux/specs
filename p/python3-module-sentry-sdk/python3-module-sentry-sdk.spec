%define oname sentry-sdk
%define mod_name sentry_sdk
%define sourcename sentry-python

%def_with check

Name: python3-module-%oname
Version: 1.39.1
Release: alt1

Summary: The official Python SDK for Sentry.io

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sentry-sdk
Vcs: https://github.com/getsentry/sentry-python
BuildArch: noarch

Source: %sourcename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-certifi
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-executing
BuildRequires: python3-module-pytest-localserver
BuildRequires: python3-module-pysocks
BuildRequires: python3-module-pip
BuildRequires: python3-module-pytest-asyncio
%endif

%add_findreq_skiplist %python3_sitelibdir/%mod_name/integrations/*

%description
%summary.

%prep
%setup -n %sourcename-%version

%build
%pyproject_build

%install
%pyproject_install
rm -rf tests/ingegrations

%check
%pyproject_run_pytest -v --ignore tests/integrations/gcp/test_gcp.py \
    --ignore tests/integrations/socket/test_socket.py \
    --deselect tests/test_utils.py::test_default_release \
    --deselect tests/integrations/wsgi/test_wsgi.py::test_session_mode_defaults_to_request_mode_in_wsgi_handler \
    --deselect tests/integrations/wsgi/test_wsgi.py::test_auto_session_tracking_with_aggregates

%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Dec 18 2023 Alexander Burmatov <thatman@altlinux.org> 1.39.1-alt1
- New version 1.39.1 (thx toni@).

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- initial build
