%define oname storages

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.dev1.git20120719.1
Summary: Storages: Abstract File Storage
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/storages/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dstufft/storages.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Storages: Abstract File Storage

%package -n python3-module-%oname
Summary: Storages: Abstract File Storage
Group: Development/Python3

%description -n python3-module-%oname
Storages: Abstract File Storage

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev1.git20120719.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev1.git20120719
- Initial build for Sisyphus

