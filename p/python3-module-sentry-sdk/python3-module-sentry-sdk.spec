%define oname sentry-sdk
%define mod_name sentry_sdk
%define sourcename sentry-python

%def_with check

Name: python3-module-%oname
Version: 2.66.1
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
%pyproject_run_pytest --ignore tests/tracing/test_span_streaming.py \
    --ignore tests/tracing/test_span_batcher.py \
    --deselect tests/test_utils.py::test_default_release \
    --deselect 'tests/tracing/test_decorator.py::test_span_templates_ai_dicts[True]' \
    --deselect 'tests/tracing/test_decorator.py::test_span_templates_ai_objects[True]' \
    --deselect 'tests/tracing/test_sampling.py::test_only_captures_segment_when_sampled_is_true_span_streaming[True]' \
    --deselect tests/tracing/test_span_origin.py::test_span_origin_manual_span_streaming \
    --deselect tests/tracing/test_span_origin.py::test_span_origin_custom_span_streaming \
    --deselect 'tests/utils/test_contextvars.py::test_leaks[threads]' \
    --deselect tests/utils/test_contextvars.py::test_leaks_when_is_contextvars_broken_is_false

%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Fri Jul 24 2026 Alexander Burmatov <thatman@altlinux.org> 2.66.1-alt1
- New version 2.66.1.

* Mon Oct 13 2025 Alexander Burmatov <thatman@altlinux.org> 2.41.0-alt1
- New version 2.41.0.

* Fri Mar 22 2024 Alexander Burmatov <thatman@altlinux.org> 1.43.0-alt1
- New version 1.43.0.

* Mon Dec 18 2023 Alexander Burmatov <thatman@altlinux.org> 1.39.1-alt1
- New version 1.39.1 (thx toni@).

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- initial build
