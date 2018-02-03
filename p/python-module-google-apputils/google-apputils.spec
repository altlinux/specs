%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.1
%define gname google
%define oname %gname-apputils

%def_with python3

Name: python-module-%oname
Version: 0.4.2
#Release: alt2.1
Summary: Google Application Utilities for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/google-apputils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/69/66/a511c428fef8591c5adfa432a257a333e0d14184b6c5d03f1450827f7fe7/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%gname = %EVR

%description
This project is a small collection of utilities for building Python
applications. It includes some of the same set of utilities used to
build and run internal Python apps at Google.

%package -n python-module-%gname
Summary: Core files of %gname
Group: Development/Python

%description -n python-module-%gname
Core files of %gname.

%package -n python3-module-%oname
Summary: Google Application Utilities for Python
Group: Development/Python3
Requires: python3-module-%gname = %EVR
%py3_provides %gname.apputils

%description -n python3-module-%oname
This project is a small collection of utilities for building Python
applications. It includes some of the same set of utilities used to
build and run internal Python apps at Google.

%package -n python3-module-%gname
Summary: Core files of %gname
Group: Development/Python3
%py3_provides %gname

%description -n python3-module-%gname
Core files of %gname.

%prep
%setup -q -n %{oname}-%{version}
find . -type f -exec chmod go+r {} \;
find . -type d -exec chmod go+rx {} \;

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
install -p -m644 google/__init__.py \
	%buildroot%python_sitelibdir/%gname/

%if_with python3
pushd ../python3
%python3_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
install -p -m644 google/__init__.py \
	%buildroot%python3_sitelibdir/%gname/
popd
%endif

%files
%doc LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/%gname/__init__.py*

%files -n python-module-%gname
%python_sitelibdir/%gname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%gname/__init__.py
%exclude %python3_sitelibdir/%gname/__pycache__/__init__.*

%files -n python3-module-%gname
%python3_sitelibdir/%gname/__init__.py
%python3_sitelibdir/%gname/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2
- fixed permissions (closes: #33008)

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Set as archdep

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

