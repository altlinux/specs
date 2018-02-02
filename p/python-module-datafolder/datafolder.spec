%define _unpackaged_files_terminate_build 1
%define oname datafolder

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.1
Summary: Install and access data files (conf, json, sqlite3, ...) in an easy way
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/datafolder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xlcnd/datafolder.git
Source0: https://pypi.python.org/packages/ec/8b/cc0f6bc805e9fe56a401306126d500498d619e5b96f4d4830f62fa3a48e0/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires setuptools

%description
datafolder is a small python library that makes it very easy to install
the data files of your package and access them later.

If you want to install some data files (conf, sqlite, csv, ...) to a
place like the user's home directory and find it difficult with
setuptools, then here is some help.

%package -n python3-module-%oname
Summary: Install and access data files (conf, json, sqlite3, ...) in an easy way
Group: Development/Python3
%py3_provides %oname
%py3_requires setuptools

%description -n python3-module-%oname
datafolder is a small python library that makes it very easy to install
the data files of your package and access them later.

If you want to install some data files (conf, sqlite, csv, ...) to a
place like the user's home directory and find it difficult with
setuptools, then here is some help.

%prep
%setup -q -n %{oname}-%{version}

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
export LC_ALL=en_US.UTF-8
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc CHANGES.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20150225
- Version 0.3.5

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150210
- Version 0.2.1

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150208
- Initial build for Sisyphus

