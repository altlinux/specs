%define oname zopeproject

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt2.1
Summary: Tools for creating development sandboxes for web applications that primarily use Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zopeproject/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Tools and scripts for creating development sandboxes for web
applications that primarily use Zope.

%package -n python3-module-%oname
Summary: Tools for creating development sandboxes for web applications that primarily use Zope
Group: Development/Python3

%description -n python3-module-%oname
Tools and scripts for creating development sandboxes for web
applications that primarily use Zope.

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

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

