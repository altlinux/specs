%define modulename icu

%def_with python3

Name: python-module-%modulename
Version: 2.0.2
Release: alt1

%setup_python_module %modulename

Summary: Python extension wrapping the ICU C++ API
License: ISC-style
Group: Development/Python

Url: http://pyicu.osafoundation.org/

%define srcname PyICU-%version
# http://pypi.python.org/packages/source/P/PyICU/%srcname.tar.gz
# VCS: https://github.com/ovalhub/pyicu.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libicu-devel python-devel
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
PyICU - Python extension wrapping the ICU C++ API.

%if_with python3
%package -n python3-module-%modulename
Summary: Python extension wrapping the ICU C++ API
Group: Development/Python3

%description -n python3-module-%modulename
PyICU - Python extension wrapping the ICU C++ API.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%python_sitelibdir/*
#%exclude %python_sitelibdir/*.egg-info
%doc CREDITS README* CHANGES samples/

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*.egg-info
%doc CREDITS README* CHANGES samples/
%endif

%changelog
* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1
- Updated to upstream version 2.0.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2
- switched build from tarballs to upstream git

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Version 1.8
- Added module for Python 3

* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Kirill Maslinsky <kirill@altlinux.org> 1.2-alt1
- 1.2

* Tue May 31 2011 Kirill Maslinsky <kirill@altlinux.org> 1.1-alt1
- 1.1

* Fri Dec 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Updated to post-1.0.1 snapshot r166 to fix build with fresh ICU.

* Wed Aug 25 2010 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

