%define _unpackaged_files_terminate_build 1
%define oname xmltodict

Name: python3-module-%oname
Version: 0.13.0
Release: alt2

Summary: Makes working with XML feel like you are working with JSON

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/xmltodict/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest

%py3_provides %oname

%description
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test3

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Mon Apr 10 2023 Anton Vyatkin <toni@altlinux.org> 0.13.0-alt2
- Fix BuildRequires

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Mon Jul 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- build python3 module separately
- new version (0.12.0) with rpmgs script

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.0-alt1
- Updated to upstream version 0.11.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150118
- Version 0.9.1

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20140727
- Initial build for Sisyphus

