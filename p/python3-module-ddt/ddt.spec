%define _unpackaged_files_terminate_build 1

%global oname ddt
%def_with check

Name: python3-module-ddt
Version: 1.5.0
Release: alt1

Summary: A Python library to multiply test cases

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/ddt/

# https://github.com/datadriventests/ddt.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(yaml)
%endif

%description
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.md
%python3_sitelibdir/*

%changelog
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
