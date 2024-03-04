%define oname humanize

Name: python3-module-%oname
Version: 4.9.0
Release: alt1

Summary: Python humanize utilities

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/humanize/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling python3-module-hatch-vcs
BuildRequires: python3-module-pytest python3-module-freezegun

#py3_provides %oname

%description
This modest package contains various common humanization utilities, like
turning a number into a fuzzy human readable duration ('3 minutes ago')
or into a human readable size or throughput.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
#pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt1
- new version 4.9.0
- switch to pyproject_build

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 4.4.0-alt1
- new version 4.4.0 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- new version 4.3.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)
- build python3 separated

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20141113.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20141113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20141113
- Initial build for Sisyphus

