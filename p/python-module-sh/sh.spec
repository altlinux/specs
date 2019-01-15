%define _unpackaged_files_terminate_build 1

%define oname sh
%def_with check

Name: python-module-%oname
Version: 1.12.14
Release: alt3
Summary: Python subprocess interface
License: MIT
BuildArch: noarch
Group: Development/Python
Url: https://pypi.org/project/sh/

# https://github.com/amoffat/sh.git
Source: %name-%version.tar
Patch1: pep-0538-test-fix.patch
Patch2: 1.12.14-sh-alt-fix-test_piped_exceptionX.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
BuildRequires: python-module-coverage
BuildRequires: python3-module-coverage
%endif

%description
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%package -n python3-module-%oname
summary: python subprocess interface
Group: Development/Python3

%description -n python3-module-%oname
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i -e 's:==:>=:g' \
	requirements*.txt

cp -fr . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python sh.py travis

pushd ../python3
python3 sh.py travis
popd

%files
%doc *.md
%python_sitelibdir/sh.py*
%python_sitelibdir/sh-%version-py*.egg-info/

%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/sh.py
%python3_sitelibdir/__pycache__/sh.cpython-*.py*
%python3_sitelibdir/sh-%version-py*.egg-info/

%changelog
* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 1.12.14-alt3
- Fixed build.

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

