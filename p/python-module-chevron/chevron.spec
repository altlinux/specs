%define oname chevron

%def_with python3

Name: python-module-%oname
Version: 0.8.4
Release: alt1.1
Summary: Mustache templating language renderer
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/chevron/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
A python implementation of the mustache templating language.

%package -n python3-module-%oname
Summary: Mustache templating language renderer
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python implementation of the mustache templating language.

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
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1
- Version 0.8.4

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1
- Version 0.7.6

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

