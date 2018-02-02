%define oname zptlint

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.1.1
Summary: Utility to debug Zope Page Templates
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zptlint/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-transaction
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.pagetemplate
BuildPreReq: python3-module-zope.contentprovider
BuildPreReq: python3-module-zope.traversing
BuildPreReq: python3-module-transaction python-tools-2to3
%endif

%py_provides %oname
%py_requires zope.pagetemplate zope.contentprovider zope.traversing

%description
Script that runs the pagetemplate parser and output errors.

%package -n python3-module-%oname
Summary: Utility to debug Zope Page Templates
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.pagetemplate zope.contentprovider zope.traversing

%description -n python3-module-%oname
Script that runs the pagetemplate parser and output errors.

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
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus

