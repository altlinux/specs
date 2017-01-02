%define oname six

%def_with python3

Name: python-module-%oname
Version: 1.9.0
Release: alt1.hg20150430.1.2
Summary: Python 2 and 3 compatibility utilities
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/six
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/gutworth/six
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel

# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: python-module-setuptools-tests}}

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: python3-module-setuptools-tests}}
%endif

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions. See the documentation for more information on what is
provided.

%if_with python3
%package -n python3-module-%oname
Summary: Python 2 and 3 compatibility utilities
Group: Development/Python3

%description -n python3-module-%oname
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions. See the documentation for more information on what is
provided.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
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

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc README documentation/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README documentation/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 02 2017 Michael Shigorin <mike@altlinux.org> 1.9.0-alt1.hg20150430.1.2
- BOOTSTRAP: avoid python-module-setuptools-tests if skipping %%check

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.hg20150430.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.hg20150430.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.hg20150430
- New snapshot

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.hg20150105
- Version 1.9.0

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.hg20141209
- New snapshot
- Added chr (ALT #30557)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.hg20141030
- Version 1.8.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.hg20140713
- Version 1.7.3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Wed Mar 06 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.0-alt1
- Version 1.2.0

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

