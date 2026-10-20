%define pypi_name mwclient

%def_enable check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1

Summary: Python client library for the MediaWiki API

License: MIT
Group: Development/Python3
URL: https://github.com/mwclient/mwclient

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-responses
BuildRequires: python3-module-requests-oauthlib
%endif

%description
mwclient is a lightweight Python client library to the MediaWiki API
which provides access to most API functionality.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# the suite mocks all HTTP requests, no network is needed
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -v -o addopts=""

%files
%doc README.md CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (renamed from python-module-mwclient, python3 only)
- switch to pyproject build from the release tarball instead of the git tree
- enable tests

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev.git20140622
- Version 0.7dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.6.5-alt1
- initial build for ALT Linux Sisyphus
