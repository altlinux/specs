%define oname servicemanager

%def_with python3

Name: python-module-%oname
Version: 0.0.16
Release: alt1.git20141007.1
Summary: A python tool to manage developing and testing with lots of microservices
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/servicemanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hmrc/service-manager.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires pymongo

%description
A set of utilities to run applications and micro services during the
development and testing phase... and make development easier in a micro
service environment.

%package -n python3-module-%oname
Summary: A python tool to manage developing and testing with lots of microservices
Group: Development/Python3
%py3_provides %oname
%py3_requires pymongo

%description -n python3-module-%oname
A set of utilities to run applications and micro services during the
development and testing phase... and make development easier in a micro
service environment.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.16-alt1.git20141007.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20141007
- Initial build for Sisyphus

