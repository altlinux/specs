%define oname pycedict

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.git20170220.1
Summary: A library for parsing CEDict and adding tone marks to pinyin
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pycedict/

# https://github.com/jdillworth/pycedict.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides cedict
%add_python_req_skip cedict_parser pinyin

%description
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.

%if_with python3
%package -n python3-module-%oname
Summary: A library for parsing CEDict and adding tone marks to pinyin
Group: Development/Python3
%py3_provides cedict

%description -n python3-module-%oname
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.
%endif

%prep
%setup

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
python tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 tests.py -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.git20170220.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1.git20170220
- Updated to upstream version 0.9.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150113
- Initial build for Sisyphus

