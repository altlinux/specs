%define oname sentry-sdk
%define mod_name sentry_sdk
%define sourcename sentry-python

%def_with check

Name: python3-module-%oname
Version: 2.41.0
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
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-watch
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-certifi
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-executing
BuildRequires: python3-module-pytest-localserver
BuildRequires: python3-module-pysocks
BuildRequires: python3-module-pip
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-forked
BuildRequires: python3-module-brotli
BuildRequires: python3-module-httpcore
BuildRequires: python3-module-gevent
BuildRequires: python3-module-asttokens
BuildRequires: python3-module-responses
BuildRequires: python3-module-socksio
BuildRequires: python3-module-httpx+http2
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
rm -rf tests/integrations

%check
%pyproject_run_pytest --deselect tests/test_utils.py::test_default_release

%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Oct 13 2025 Alexander Burmatov <thatman@altlinux.org> 2.41.0-alt1
- New version 2.41.0.

* Fri Mar 22 2024 Alexander Burmatov <thatman@altlinux.org> 1.43.0-alt1
- New version 1.43.0.

* Mon Dec 18 2023 Alexander Burmatov <thatman@altlinux.org> 1.39.1-alt1
- New version 1.39.1 (thx toni@).

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- initial build
