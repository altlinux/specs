%define oname itsdangerous

%def_with python3

Name: python-module-%oname
Version: 0.24
Release: alt1.git20140328.1
Summary: Various helpers to pass trusted data to untrusted environments and back
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/itsdangerous/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/itsdangerous.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
It's Dangerous
   ... so better sign this

Various helpers to pass data to untrusted environments and to get it
back safe and sound.

%package -n python3-module-%oname
Summary: Various helpers to pass trusted data to untrusted environments and back
Group: Development/Python3

%description -n python3-module-%oname
It's Dangerous
   ... so better sign this

Various helpers to pass data to untrusted environments and to get it
back safe and sound.

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
%doc CHANGES README docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24-alt1.git20140328.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1.git20140328
- Initial build for Sisyphus

