%define oname language_tags

%def_with check

Name: python3-module-language-tags
Version: 1.3.1
Release: alt1

Summary: This project is a Python version of the language-tags Javascript project

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/language-tags/

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
This Python API offers a way to validate and lookup languages tags.

It is based on BCP 47 (RFC 5646) and the latest IANA language subtag
registry.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat May 09 2026 Anton Vyatkin <toni@altlinux.org> 1.3.1-alt1
- new version 1.3.1
- migrate to pyproject macros
- build with check

* Fri Apr 14 2023 Anton Vyatkin <toni@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1.git20141218.2
- build python3 module separately
- cleanup spec, build from tarball, update buildreqs

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20141218.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141218.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141218
- Initial build for Sisyphus

