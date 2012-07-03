%define oname python-subunit

%def_with python3

Name: python-module-%oname
Version: 0.0.7
Release: alt2
Summary: Python implementation of subunit test streaming protocol
License: Apache of BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/python-subunit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-testtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-testtools python-tools-2to3
%endif

%description
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 implementation of subunit test streaming protocol
Group: Development/Python3

%description -n python3-module-%oname
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%package -n python3-module-%oname-tests
Summary: Tests for python-subunit (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

This package contains tests for python-subunit.
%endif

%package tests
Summary: Tests for python-subunit
Group: Development/Python
Requires: %name = %version-%release

%description tests
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

This package contains tests for python-subunit.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

%files
%doc NEWS README
%_bindir/*
%exclude %_bindir/py3_*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc NEWS README
%exclude %_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.7-alt1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

