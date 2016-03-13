%define module_name cl

%def_with python3

Name: python-module-%module_name
Version: 0.0.3
Release: alt2.1
Group: Development/Python
License: BSD License
Summary: Actor framework for Kombu
URL: http://github.com/ask/cl/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
cl is an actor framework for Kombu.

%package -n python3-module-%module_name
Summary: Actor framework for Kombu
Group: Development/Python3

%description -n python3-module-%module_name
cl is an actor framework for Kombu.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc AUTHORS Changelog README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/cl*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog README.rst
%_bindir/*.py3
%python3_sitelibdir/cl*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt2
- Added module for Python 3

* Sat May 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.3-alt1
- build for ALT
