%define _unpackaged_files_terminate_build 1

%global oname ddt
%def_with check

Name: python3-module-ddt
Version: 1.7.2
Release: alt1

Summary: A Python library to multiply test cases

Group: Development/Python3
License: MIT
URL: https://pypi.org/project/ddt
VCS: https://github.com/datadriventests/ddt

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(yaml)
BuildRequires: python3(aiounittest)
%endif

%description
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/%oname.py
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/__pycache__

%changelog
* Tue Mar 05 2024 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Automatically updated to 1.7.2.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1
- Automatically updated to 1.7.1.

* Thu Dec 28 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Automatically updated to 1.7.0.

* Fri Aug 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Automatically updated to 1.5.0.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt2
- Drop python2 support.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.1.1 -> 1.4.2.

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- Initial build for ALT (based on CentOS 1.0.1-2.el7.src)
