%define _unpackaged_files_terminate_build 1
%define pypi_name chardet

%def_with check

Name: python3-module-%pypi_name
Version: 5.1.0
Release: alt1
Epoch: 1

Summary: Character encoding auto-detection in Python
License: LGPL-2.1
Group: Development/Python3

Url: https://pypi.org/project/chardet/
VCS: https://github.com/chardet/chardet
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
Character encoding auto-detection in Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%_bindir/chardetect
%python3_sitelibdir/chardet/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 09 2022 Stanislav Levin <slev@altlinux.org> 1:5.1.0-alt1
- 3.0.4 -> 5.1.0.

* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 1:3.0.4-alt3
- Build without python2 support.

* Sun Dec 13 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.0.4-alt2
- Downgrade to version 3.0.4.

* Fri Dec 11 2020 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Sun Apr 13 2014 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)
- build for python3 too

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Mar 22 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.3.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.3
- Site-packages removed from packages (Closes #18909)
- Packager tag added

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.2
- Really fix build on x86_64

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.1
- Egg dropped to build on x86_64

* Sun Dec 28 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus (thanks Mandriva for initial spec)
