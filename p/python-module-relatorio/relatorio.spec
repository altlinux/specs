%define oname relatorio

%def_without python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: A templating library able to output odt and pdf files
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/relatorio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-lxml
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-lxml
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

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

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES LICENSE README
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

