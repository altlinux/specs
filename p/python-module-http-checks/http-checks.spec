%define _unpackaged_files_terminate_build 1
%define oname http-checks

%def_without python3

Name: python-module-%oname
Version: 0.1.8
Release: alt1
Summary: Test a couple of hundred urls in seconds
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/http-checks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Hipo/http-checks.git
Source0: https://pypi.python.org/packages/17/0b/b1fcad012963b5b275a7ca6b4675b4e76dfef3b6f6479b936c5418247cf3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-module-requests
BuildPreReq: python-module-gevent python-module-BeautifulSoup4
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml python3-module-requests
BuildPreReq: python3-module-gevent python3-module-BeautifulSoup4
%endif

%py_provides httpchecks
%py_requires yaml gevent bs4

%description
http-checks is an application that can test a couple of hundred urls in
seconds.

%if_with python3
%package -n python3-module-%oname
Summary: Test a couple of hundred urls in seconds
Group: Development/Python3
%py3_provides httpchecks
%py3_requires yaml gevent bs4

%description -n python3-module-%oname
http-checks is an application that can test a couple of hundred urls in
seconds.
%endif

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
export PATH=$PATH:%buildroot%_bindir
python setup.py test
export PYTHONPATH=$PWD
#http-checks -c check_sample.yml
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
#http-checks.py3 -c check_sample.yml
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
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1
- automated PyPI update

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.git20150106
- Version 0.1.7

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141127
- Version 0.1.6

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141126
- Initial build for Sisyphus

