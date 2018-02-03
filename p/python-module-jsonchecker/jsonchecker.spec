%define oname jsonchecker

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20150109.1.1
Summary: A script that validates JSON files and checks for duplicate keys
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonchecker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/legoktm/jsonchecker.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires json

%description
Checks a JSON file for any duplicate keys, which would be ignored by the
normal parser.

%package -n python3-module-%oname
Summary: A script that validates JSON files and checks for duplicate keys
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Checks a JSON file for any duplicate keys, which would be ignored by the
normal parser.

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
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1.git20150109.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20150109.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150109
- Initial build for Sisyphus

