%define oname TAP

%def_with python3

Name: python-module-%oname
Version: 0.001
Release: alt1.git20110216.1
Summary: Test Anything Protocol
License: MIT/X11
Group: Development/Python
Url: http://testanything.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.codesimply.com/PyTAP.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%py_provides %oname

%description
TAP, the Test Anything Protocol, is a simple text-based interface
between testing modules in a test harness.

%package -n python3-module-%oname
Summary: Test Anything Protocol
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
TAP, the Test Anything Protocol, is a simple text-based interface
between testing modules in a test harness.

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

%files
%doc examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.001-alt1.git20110216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.001-alt1.git20110216
- Initial build for Sisyphus

