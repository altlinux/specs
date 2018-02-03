%define _unpackaged_files_terminate_build 1
%define oname glob2

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.1
Summary: Extended version of Python's builtin glob module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/glob2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/miracle2k/python-glob2.git
Source0: https://pypi.python.org/packages/53/ae/a8b28dfc011b7c645bd6aa4591ffa14db9fb48f08a32034374e01ca75ff3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Version of the glob module that can capture patterns and supports
recursive wildcards.

%package -n python3-module-%oname
Summary: Extended version of Python's builtin glob module
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Version of the glob module that can capture patterns and supports
recursive wildcards.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc CHANGES *.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140122
- Initial build for Sisyphus

