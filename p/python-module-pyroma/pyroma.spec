%define _unpackaged_files_terminate_build 1
%define oname pyroma

%def_with python3

Name: python-module-%oname
Version: 2.2
Release: alt1.1
Summary: Test your project's packaging friendliness
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyroma/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/de/f3/104ae27624982cd4b6de786d9afe23a2dc0b8c0999443ba370b3755848c7/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-docutils
%endif

%py_provides %oname

%description
Pyroma rhymes with aroma, and is a product aimed at giving a rating of
how well a Python project complies with the best practices of the Python
packaging ecosystem, primarily PyPI, pip, Distribute etc, as well as a
list of issues that could be improved.

The aim of this is both to help people make a project that is nice and
usable, but also to improve the quality of Python third-party software,
making it easier and more enjoyable to use the vast array of available
modules for Python.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pyroma rhymes with aroma, and is a product aimed at giving a rating of
how well a Python project complies with the best practices of the Python
packaging ecosystem, primarily PyPI, pip, Distribute etc, as well as a
list of issues that could be improved.

The aim of this is both to help people make a project that is nice and
usable, but also to improve the quality of Python third-party software,
making it easier and more enjoyable to use the vast array of available
modules for Python.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Test your project's packaging friendliness
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pyroma rhymes with aroma, and is a product aimed at giving a rating of
how well a Python project complies with the best practices of the Python
packaging ecosystem, primarily PyPI, pip, Distribute etc, as well as a
list of issues that could be improved.

The aim of this is both to help people make a project that is nice and
usable, but also to improve the quality of Python third-party software,
making it easier and more enjoyable to use the vast array of available
modules for Python.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pyroma rhymes with aroma, and is a product aimed at giving a rating of
how well a Python project complies with the best practices of the Python
packaging ecosystem, primarily PyPI, pip, Distribute etc, as well as a
list of issues that could be improved.

The aim of this is both to help people make a project that is nice and
usable, but also to improve the quality of Python third-party software,
making it easier and more enjoyable to use the vast array of available
modules for Python.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Initial build for Sisyphus

