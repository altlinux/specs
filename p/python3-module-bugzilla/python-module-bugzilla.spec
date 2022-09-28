%define _unpackaged_files_terminate_build 1
%define pypi_name python-bugzilla
%define mod_name bugzilla

%def_with check

Name: python3-module-%mod_name
Version: 3.2.0
Release: alt1

Summary: Library and command line tool for interacting with Bugzilla
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-bugzilla/

BuildArch: noarch

# Source-url: https://github.com/python-bugzilla/python-bugzilla
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# deps
BuildRequires: python3(requests)

BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
This package provides two bits:
- bugzilla python module for talking to a Bugzilla instance over XMLRPC or REST
- /usr/bin/bugzilla command line tool for performing actions from the command
line: create or edit bugs, various queries, etc.

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
%doc NEWS.md README.md examples
%_bindir/bugzilla
%_man1dir/bugzilla.*
%python3_sitelibdir/bugzilla/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 2.3.0 -> 3.2.0.
- Modernized packaging.
- Enabled testing.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt1
- python2 disabled

* Wed Jun 19 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)
- switch to build from tarball

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.ru> 2.1.0-alt1
- Version 2.1.0

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Thu Sep 04 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
