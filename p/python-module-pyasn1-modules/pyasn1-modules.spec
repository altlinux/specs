%define _unpackaged_files_terminate_build 1
%define mname pyasn1-modules

Name: python-module-%mname
Version: 0.2.1
Release: alt1%ubt

Summary: ASN.1 modules for Python
License: %bsdstyle
Group: Development/Python
# Source-git: https://github.com/etingof/pyasn1-modules.git
Url: https://pypi.python.org/pypi/pyasn1-modules

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-licenses

BuildRequires: python-module-pyasn1 >= 0.4.1
BuildRequires: python3-module-pyasn1 >= 0.4.1
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

Requires: python-module-pyasn1 >= 0.4.1

%description
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%package -n python3-module-%mname
Summary: ASN.1 modules for Python 3
Group: Development/Python3
Requires: python3-module-pyasn1 >= 0.4.1

%description -n python3-module-%mname
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python setup.py test -v

pushd ../python3
python3 setup.py test -v
popd

%files
%doc LICENSE.txt README.md
%python_sitelibdir/pyasn1_modules
%python_sitelibdir/pyasn1_modules-%version-*.egg-info/

%files -n python3-module-%mname
%doc LICENSE.txt README.md
%python3_sitelibdir/pyasn1_modules
%python3_sitelibdir/pyasn1_modules-%version-*.egg-info/

%changelog
* Tue Mar 13 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1%ubt
- 0.1.5 -> 0.2.1

* Thu Nov 09 2017 Stanislav Levin <slev@altlinux.org> 0.1.5-alt1%ubt
- 0.0.8 -> 0.1.5

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Version 0.0.7

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Version 0.0.5

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt2
- Version 0.0.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.4-alt1.rc0.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.rc0
- Initial build for Sisyphus

