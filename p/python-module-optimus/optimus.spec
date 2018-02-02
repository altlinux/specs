%define _unpackaged_files_terminate_build 1
%define oname optimus

%def_without python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.1
Summary: Python web framework project constructor
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/py-optimus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/johndeng/optimus.git
Source0: https://pypi.python.org/packages/8e/38/c49f6c9f639e259f0558a517303fc821cc6a25ada43ea0f6bda389cd42c7/py-%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-click python-module-jinja2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-click python3-module-jinja2
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%add_findreq_skiplist %python_sitelibdir/%oname/templates/*
%add_python_compile_exclude %python_sitelibdir/%oname/templates/*

%description
Optimus is a Python web framework project constructor.

Now optimus support create Tornado project structure.

%if_with python3
%package -n python3-module-%oname
Summary: Python web framework project constructor
Group: Development/Python3
%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/templates/*
%add_python3_compile_exclude %python3_sitelibdir/%oname/templates/*

%description -n python3-module-%oname
Optimus is a Python web framework project constructor.

Now optimus support create Tornado project structure.
%endif

%prep
%setup -q -n py-%{oname}-%{version}

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
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1
- automated PyPI update

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.git20141126
- Fixed build

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141126
- Initial build for Sisyphus

