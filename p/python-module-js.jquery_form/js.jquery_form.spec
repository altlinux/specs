%define oname js.jquery_form

%def_with python3

Name: python-module-%oname
Version: 3.09
Release: alt1.1
Summary: Fanstatic packaging of jQuery Form
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.jquery_form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js js.jquery

%description
This library packages jQuery Form for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of jQuery Form
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery

%description -n python3-module-%oname
This library packages jQuery Form for fanstatic.

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

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.09-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.09-alt1
- Initial build for Sisyphus

