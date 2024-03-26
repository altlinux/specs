%define pypi_name appengine-standard

%def_without check

Name:    python3-module-%pypi_name
Version: 1.1.6
Release: alt1

Summary: Google App Engine services SDK for Python 3
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/GoogleCloudPlatform/appengine-python-standard

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-abseil-py
BuildRequires: python3-module-six
BuildRequires: python3-module-protobuf
BuildRequires: python3-module-ruamel-yaml
BuildRequires: python3-module-frozendict
BuildRequires: python3-module-requests
BuildRequires: python3-module-attrs
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytz
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-google-auth-library-python
BuildRequires: python3-module-pymox
BuildRequires: python3-module-google-api-client
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-rsa
BuildRequires: python3-module-sortedcontainers
BuildRequires: python3-module-urllib3
%endif

%add_python3_req_skip google
%add_python3_req_skip protorpc
%add_python3_req_skip treewizard
%add_python3_req_skip stringtemplate3

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
find . -name '*.py' -o -name 'cxxtestgen' | xargs sed -i \
    -e '1 s:#!%_bindir/env python$:#!%_bindir/python3:' \
    -e '1 s:#! %_bindir/env python$:#! %_bindir/python3:' \
    %nil

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests --cov=google.appengine

%files
%doc *.md
%python3_sitelibdir/google/
%python3_sitelibdir/appengine_python_standard-*/

%changelog
* Thu Feb 01 2024 Alexander Burmatov <thatman@altlinux.org> 1.1.6-alt1
- New 1.1.6 version.

* Tue Oct 03 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus.
