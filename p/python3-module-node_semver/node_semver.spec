%define oname node_semver

%def_with check

Name: python3-module-%oname
Version: 0.9.1
Release: alt1

Summary: python version of node-semver

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/node-semver/

# Source-url: https://github.com/podhmo/python-semver/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with check
%py3_buildrequires pytest >= 2.13.1
%endif

%description
Python version of [node-semver] (https://github.com/isaacs/node-semver).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%check
py.test3 -v .

%files
%doc README.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/nodesemver/

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1
- package module is nodesemver now, drop the semver rename

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt2
- rename semver module to node_semver (ALT bug 39271)

* Thu Oct 29 2020 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- initial build for ALT Sisyphus
