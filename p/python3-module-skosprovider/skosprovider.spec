%define oname skosprovider

%def_with check

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Abstraction layer for SKOS vocabularies

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/skosprovider/
Vcs: https://github.com/koenedaele/skosprovider.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-rfc3987
BuildRequires: python3-module-language-tags
BuildRequires: python3-module-html5lib
%endif

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
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc *.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Fri Apr 14 2023 Anton Vyatkin <toni@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

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

