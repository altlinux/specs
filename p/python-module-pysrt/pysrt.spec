%define _unpackaged_files_terminate_build 1
%define oname pysrt

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt2.1
Summary: SubRip (.srt) subtitle parser and writer
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pysrt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/byroot/pysrt.git
Source0: https://pypi.python.org/packages/f6/33/16ad65a8973cb8bcb494af09ee1b9ab5ffdd6ff300bce5d3ac7d3cb1f2cc/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-chardet python-module-nose
BuildPreReq: python-module-coverage
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-chardet python3-module-nose
BuildPreReq: python3-module-coverage
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires chardet

%description
pysrt is a Python library used to edit or create SubRip files.

%package -n python3-module-%oname
Summary: SubRip (.srt) subtitle parser and writer
Group: Development/Python3
%py3_provides %oname
%py3_requires chardet

%description -n python3-module-%oname
pysrt is a Python library used to edit or create SubRip files.

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
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test3
popd
%endif

%files
%doc *.rst PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Fixed build spec with py.test3

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20140527.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140527
- Initial build for Sisyphus

