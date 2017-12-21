%define _unpackaged_files_terminate_build 1
%define oname pies

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.6.7
Release: alt2
Summary: The simplest way to write one program that runs on both Python 2 and Python 3
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pies/

# https://github.com/timothycrosley/pies.git
Source: %oname-%version.tar

BuildRequires: python-module-enum34 python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-enum34 python3-module-pytest
%endif

%py_provides %oname

%description
The simplest (and tastiest) way to write one program that runs on both
Python 2 and Python 3.

%if_with python3
%package -n python3-module-%oname
Summary: The simplest way to write one program that runs on both Python 2 and Python 3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The simplest (and tastiest) way to write one program that runs on both
Python 2 and Python 3.
%endif

%prep
%setup -n %oname-%version

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
py.test
%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.7-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.3-alt2.git20141225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.3-alt2.git20141225
- cleanup buildreq

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.3-alt1.git20141225
- Version 2.6.3

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.git20140224
- Initial build for Sisyphus

