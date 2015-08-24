%define oname tidylib

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150711
Summary: Python wrapper for HTML Tidy (tidylib) on Python 2 and 3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytidylib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/countergram/pytidylib.git
Source: %name-%version.tar

BuildPreReq: libtidy
BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%ifarch x86_64
Requires: libtidy-0.99.so.0()(64bit)
%else
Requires: libtidy-0.99.so.0
%endif

%description
PyTidyLib is a Python package that wraps the HTML Tidy library. This
allows you, from Python code, to "fix" invalid (X)HTML markup.

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper for HTML Tidy (tidylib) on Python 2 and 3
Group: Development/Python3
%py3_provides %oname
%ifarch x86_64
Requires: libtidy-0.99.so.0()(64bit)
%else
Requires: libtidy-0.99.so.0
%endif

%description -n python3-module-%oname
PyTidyLib is a Python package that wraps the HTML Tidy library. This
allows you, from Python code, to "fix" invalid (X)HTML markup.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
py.test -vv
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%files
%doc README docs/rst/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README docs/rst/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150711
- Version 0.3.0

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141219
- Initial build for Sisyphus

