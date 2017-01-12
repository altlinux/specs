%define _unpackaged_files_terminate_build 1
%define oname crank

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1
Summary: Generalization of dispatch mechanism for use across frameworks
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/crank/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/59/9b/5df0c3319f0c4de5a8fc428243487750bbd9e96646b5aa435494e724a1c5/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Generalization of dispatch mechanism for use across frameworks.

%package -n python3-module-%oname
Summary: Generalization of dispatch mechanism for use across frameworks
Group: Development/Python3

%description -n python3-module-%oname
Generalization of dispatch mechanism for use across frameworks.

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

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

