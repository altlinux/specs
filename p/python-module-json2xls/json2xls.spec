%define oname json2xls

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150116
Summary: Generate excel by json
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/json2xls/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/axiaoxin/json2xls.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-click
BuildPreReq: python-module-xlwt
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-click
BuildPreReq: python3-module-xlwt-future
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires json requests click xlwt

%description
json2xls: Generate Excel by JSON data.

%package -n python3-module-%oname
Summary: Generate excel by json
Group: Development/Python3
%py3_provides %oname
%py3_requires json requests click xlwt

%description -n python3-module-%oname
json2xls: Generate Excel by JSON data.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150116
- Initial build for Sisyphus

