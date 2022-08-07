%define oname aniso8601

%def_with check

Name: python3-module-%oname
Version: 9.0.1
Release: alt1

Summary: Another ISO 8601 parser for Python

Url: https://bitbucket.org/nielsenb/aniso8601
License: BSD
Group: Development/Python3

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
This is a Python library for parsing date strings
in ISO 8601 format into datetime format.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3 -v

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Fri Aug 05 2022 Grigory Ustinov <grenka@altlinux.org> 9.0.1-alt1
- Build new version.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt2
- Drop python2 support.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- initial build

