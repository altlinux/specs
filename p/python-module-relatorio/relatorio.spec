%define _unpackaged_files_terminate_build 1
%define oname relatorio

%def_without python3

Name: python-module-%oname
Version: 0.6.4
Release: alt1.1
Summary: A templating library able to output odt and pdf files
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/relatorio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/18/de/18b3e8d004e43f86884c5c6148d4b15b86d07a267f45835c684deb2a4c06/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-genshi python-module-lxml
BuildPreReq: python-module-nose python-module-pycha
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-genshi python3-module-lxml
BuildPreReq: python3-module-nose python3-module-pycha
%endif

%py_provides %oname

%description
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A templating library able to output odt and pdf files
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

This package contains tests for %oname.
%endif

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3
- Fixed build

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Moved tests into separate package

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

