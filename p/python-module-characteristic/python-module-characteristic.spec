%define oname characteristic
%def_with python3

Name: python-module-%oname
Version: 14.3.0
Release: alt1.1.1.1

Summary: Python library that eases the chores of implementing attributes

License: MIT
Group: Development/Python
Url: https://github.com/hynek/characteristic

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/c/characteristic/characteristic-0.1.0.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

#BuildPreReq: rpm-build-python
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel python-module-distribute python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute python3-module-setuptools
%endif

%setup_python_module %oname

%description
characteristic is an MIT-licensed Python package with class decorators that ease the chores of
implementing the most common attribute-related object protocols.

%if_with python3
%package -n python3-module-%oname
Summary: Python library that eases the chores of implementing attributes (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
characteristic is an MIT-licensed Python package with class decorators that ease the chores of
implementing the most common attribute-related object protocols.
%endif


%prep
%setup -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS.rst CONTRIBUTING.rst README.rst
%python_sitelibdir/%oname.py
%python_sitelibdir/test_%oname.py
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*.pyc
%exclude %python_sitelibdir/*.pyo

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname.py
%python3_sitelibdir/test_%oname.py
%python3_sitelibdir/*.egg-*
%exclude %python3_sitelibdir/__pycache__/
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 14.3.0-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 14.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 14.3.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.ru> 14.3.0-alt1
- new version

* Thu Jul 31 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.0-alt1
- initial build for Sisyphus
