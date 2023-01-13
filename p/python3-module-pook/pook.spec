%define  oname pook

%def_with check

Name:    python3-module-%oname
Version: 1.1.1
Release: alt1

Summary: HTTP traffic mocking and testing made easy in Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/h2non/pook

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-furl
BuildRequires: python3-module-xmltodict
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-requests
BuildRequires: python3-module-urllib3
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

# don't install tests in such directory please
rm -rf %buildroot%python3_sitelibdir/tests

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v -k 'not test_engines'

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%doc LICENSE *.rst

%changelog
* Fri Jan 13 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.

* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
