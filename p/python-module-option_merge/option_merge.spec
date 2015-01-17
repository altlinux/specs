%define oname option_merge

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20150103
Summary: Code to deeply merge multiple python dictionaries
License: WTFPL
Group: Development/Python
Url: https://pypi.python.org/pypi/option_merge/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/delfick/option_merge.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-delfick_error
BuildPreReq: python-module-namedlist python-module-noseOfYeti
BuildPreReq: python-module-nose python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-delfick_error
BuildPreReq: python3-module-namedlist python3-module-noseOfYeti
BuildPreReq: python3-module-nose python3-module-mock
%endif

%py_provides %oname
%py_requires six delfick_error namedlist

%description
This provides the option_merge.MergedOptions class, which allows you to
treat multiple python dictionaries as one.

%package -n python3-module-%oname
Summary: Code to deeply merge multiple python dictionaries
Group: Development/Python3
%py3_provides %oname
%py3_requires six delfick_error namedlist

%description -n python3-module-%oname
This provides the option_merge.MergedOptions class, which allows you to
treat multiple python dictionaries as one.

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
./test.sh -v
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' test.sh
./test.sh -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150103
- Initial build for Sisyphus

