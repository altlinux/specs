%define module_name yolk

%def_with python3

Name: python-module-%module_name
Version: 0.4.3
Release: alt3.1
Group: Development/Python
License: BSD License
Summary: Yolk is a Python tool for obtaining information about installed Python packages
URL: https://github.com/cakebread/yolk.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Yolk is a Python tool for obtaining information about installed Python packages
and querying packages avilable on PyPI (Python Package Index).

You can see which packages are active, non-active or in development mode
and show you which have newer versions available by querying PyPI.

%package -n python3-module-%module_name
Summary: Yolk is a Python tool for obtaining information about installed Python packages
Group: Development/Python3

%description -n python3-module-%module_name
Yolk is a Python tool for obtaining information about installed Python packages
and querying packages avilable on PyPI (Python Package Index).

You can see which packages are active, non-active or in development mode
and show you which have newer versions available by querying PyPI.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|urllib2|urllib.request|g' ../python3/yolk/pypi.py
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
%doc AUTHORS COPYING FAQ README.rst THANKS ChangeLog CREDITS NEWS README TODO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/yolk*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS COPYING FAQ README.rst THANKS ChangeLog CREDITS NEWS README TODO
%_bindir/*.py3
%python3_sitelibdir/yolk*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt3
- yolk.pypi: Fixed for Python 3

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt2
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.3-alt1
- build for ALT
