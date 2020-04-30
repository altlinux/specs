%define _unpackaged_files_terminate_build 1
%define oname selenium

Name: python-module-%oname
Version: 3.141.0
Release: alt2
Summary: Python bindings for Selenium
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/selenium/

Source0: %oname-%version.tar.gz
Patch: selenium-use-without-bundled-libs.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%description
Python language bindings for Selenium WebDriver.

The selenium package is used automate web browser interaction from
Python.

%prep
%setup -q -n %oname-%version
%patch -p2

%build
%python_build

%install
%python_install

find %buildroot -type f -name '*.so' -exec rm -f '{}' +

%check
python2 setup.py test

%files
%python_sitelibdir/*

%changelog
* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 3.141.0-alt2
- Fixed FTBFS.

* Sun Apr 12 2020 Alexey Shabalin <shaba@altlinux.org> 3.141.0-alt1
- build for python2 only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 19 2017 Lenar Shakirov <snejok@altlinux.ru> 3.0.2-alt2
- selenium-use-without-bundled-libs.patch added

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.47.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.47.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.47.0-alt1
- Version 2.47.0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.44.0-alt1
- Version 2.44.0

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.43.0-alt1
- Initial build for Sisyphus

