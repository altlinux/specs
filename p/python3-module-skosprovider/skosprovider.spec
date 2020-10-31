%define oname skosprovider

Name: python3-module-%oname
Version: 0.5.0
Release: alt2.git20141218

Summary: Abstraction layer for SKOS vocabularies

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/skosprovider/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/koenedaele/skosprovider.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-language-tags python3-module-nose python3-module-pytest-cov python3-module-setuptools

%description
This library helps abstract vocabularies (thesauri, controlled lists,
authority files). It depends heavily on the SKOS specification, but adds
elements of other specifications such as the ISO 25964 SKOS extension
where deemed useful.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2.git20141218
- build python3 module

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.git20141218.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141218
- Initial build for Sisyphus

