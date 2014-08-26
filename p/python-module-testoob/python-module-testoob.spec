%define oname testoob

%def_without python3

Name: python-module-%oname
Version: 1.16
Release: alt1.git20110725
Summary: Testing Out Of (The) Box

Group: Development/Python
License: Apache License, Version 2.0
URL: http://testoob.sourceforge.net/
# https://github.com/testoob/testoob.git
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
Testoob is an advanced Python unit testing framework that
integrates effortlessly with Python's standard 'unittest'
module.

%package -n python3-module-%oname
Summary: Testing Out Of (The) Box
Group: Development/Python3

%description -n python3-module-%oname
Testoob is an advanced Python unit testing framework that
integrates effortlessly with Python's standard 'unittest'
module.

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
cp -fR tests %buildroot%python3_sitelibdir/%oname/
touch %buildroot%python3_sitelibdir/%oname/tests/__init__.py
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install 
cp -fR tests %buildroot%python_sitelibdir/%oname/
touch %buildroot%python_sitelibdir/%oname/tests/__init__.py

%files
%doc README docs/CHANGELOG docs/COPYING docs/LICENSE-2.0.txt
%python_sitelibdir/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif

%if_with python3
%files -n python3-module-%oname
%doc README docs/CHANGELOG docs/COPYING docs/LICENSE-2.0.txt
%python3_sitelibdir/*
%_bindir/*.py3
%endif

%changelog
* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16-alt1.git20110725
- Version 1.16

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.15-alt1.1
- Rebuild with Python-2.7

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1
- Version 1.15

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt2
- Rebuilt with python 2.6

* Thu Oct 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1
- Initial build for Sisyphus

