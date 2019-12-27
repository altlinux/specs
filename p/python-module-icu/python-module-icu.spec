%define _unpackaged_files_terminate_build 1

%define modulename icu

%def_with python2

Name: python-module-%modulename
# python3 setup.py -V|tail -1
Version: 2.4.2
Release: alt1

%{?_with_python2:%setup_python_module %modulename}

Summary: Python extension wrapping the ICU C++ API
License: MIT
Group: Development/Python

Url: http://pyicu.osafoundation.org/

%define srcname PyICU-%version
# http://pypi.python.org/packages/source/P/PyICU/%srcname.tar.gz
# VCS: https://github.com/ovalhub/pyicu.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libicu-devel
BuildRequires: python3-devel python3-module-setuptools

%if_with python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
%endif

%description
PyICU - Python extension wrapping the ICU C++ API.

%package -n python3-module-%modulename
Summary: Python extension wrapping the ICU C++ API
Group: Development/Python3

%description -n python3-module-%modulename
PyICU - Python extension wrapping the ICU C++ API.

%prep
%setup
%if_with python2
cp -fR . ../python2
%endif

%build
%python3_build

%if_with python2
pushd ../python2
%python_build
popd
%endif

%install
%python3_install

%if_with python2
pushd ../python2
%python_install
popd
%endif

%if_with python2
%files
%python_sitelibdir/*
#%exclude %python_sitelibdir/*.egg-info
%doc CREDITS README* CHANGES samples/
%endif

%files -n python3-module-%modulename
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*.egg-info
%doc CREDITS README* CHANGES samples/


%changelog
* Fri Dec 27 2019 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2
- made python2 build optional
- fixed License tag

* Sun Oct 13 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt2
- updated to v2.3.1-30-g5fb711a (compatible with icu-65.1)

* Sat May 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3 (compatible with icu-64.1)

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt2
- Rebuilt with new icu.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

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

