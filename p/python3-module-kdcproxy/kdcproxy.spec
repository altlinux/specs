%define _unpackaged_files_terminate_build 1

%define mname kdcproxy
%def_with check

Name: python3-module-%mname
Version: 1.0.0
Release: alt1

Summary: A kerberos KDC HTTP proxy WSGI module
License: %mit
Group: Development/Python3
Url: https://pypi.org/project/kdcproxy
# Source-git: https://github.com/latchset/kdcproxy

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: libkrb5
BuildRequires: python3(dns)
BuildRequires: python3(pyasn1)
BuildRequires: python3(tox)
BuildRequires: python3(webtest)
%endif

BuildArch: noarch

%description
This package contains a Python 3.x WSGI module for proxying KDC requests
over HTTP by following the MS-KKDCP protocol. It aims to be simple
to deploy, with minimal configuration.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
%_bindir/tox.py3 --sitepackages -vvr

%files
%doc COPYING README
%python3_sitelibdir/%mname/
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info/

%changelog
* Fri Jan 22 2021 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.4.2 -> 1.0.0.

* Fri Oct 04 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- 0.4.1 -> 0.4.2.
- Dropped Python2 package.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 0.4.1-alt2
- Added missing dep on Pytest.

* Tue Feb 12 2019 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4 -> 0.4.1.

* Tue Aug 14 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1
- 0.3.3 -> 0.4.

* Thu Jul 26 2018 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- 0.3.2 -> 0.3.3
- Build package for Python3

* Wed Sep 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Initial build.

