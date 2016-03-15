%define oname js.jquery_timepicker_addon

%def_with python3

Name: python-module-%oname
Version: 1.3.1
Release: alt1.1
Summary: Fanstatic packaging of jQuery-Timepicker-Addon
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.jquery_timepicker_addon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js js.jqueryui

%description
This library packages jQuery-Timepicker-Addon for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of jQuery-Timepicker-Addon
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jqueryui

%description -n python3-module-%oname
This library packages jQuery-Timepicker-Addon for fanstatic.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

