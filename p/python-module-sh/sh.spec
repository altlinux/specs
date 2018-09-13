%define _unpackaged_files_terminate_build 1

%define oname sh

%def_with python3

Name: python-module-%oname
Version: 1.12.14
Release: alt2
Summary: Python subprocess interface
License: MIT
BuildArch: noarch
Group: Development/Python
Url: https://pypi.python.org/pypi/sh/

# https://github.com/amoffat/sh.git
Source: %name-%version.tar
Patch1: pep-0538-test-fix.patch

BuildRequires: python-devel python-module-setuptools /dev/pts
BuildRequires: python-module-coverage python-module-py
BuildRequires: python-module-tox python-module-virtualenv
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-coverage python3-module-py
BuildRequires: python3-module-tox python3-module-virtualenv
BuildRequires: python3-module-nose
%endif

%py_provides %oname

%description
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%package -n python3-module-%oname
summary: python subprocess interface
Group: Development/Python3
%py_provides %oname

%description -n python3-module-%oname
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%prep
%setup
%patch1 -p1

sed -i -e 's:==:>=:g' \
	requirements*.txt

%if_with python3
cp -fr . ../python3
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
python sh.py travis

%if_with python3
pushd ../python3
python3 sh.py travis
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%oname-%version-py*.egg-info
%endif

%changelog
* Wed Sep 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.14-alt2
- Fixed build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.12.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.14-alt1
- Updated to upstream release 1.12.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.git20150211
- Version 1.11

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2.git20141230
- Fixed Group

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1.git20141230
- Version 1.10

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1.git20130908
- Initial build for Sisyphus

