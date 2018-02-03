%define _unpackaged_files_terminate_build 1
%define oname openpyxl
%def_with python3

Name:    python-module-%oname
Version: 2.4.1
Release: alt2.1
Summary: A Python library to read/write Excel 2007 xlsx/xlsm files
License: MIT/Expat
Group:   Development/Python
Url:     http://openpyxl.readthedocs.io
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: https://pypi.python.org/packages/dc/f2/c57f9f00f8ae5e1a73cb096dbf600433724f037ffcbd51c456f89da5efd9/%{oname}-%{version}.tar.gz
Patch1: %oname-%version-alt-python3-compat.patch

BuildArch: noarch

%py_requires jdcal json et_xmlfile

BuildRequires: python-module-jdcal
BuildRequires: python-module-setuptools
BuildRequires: python-modules-json
BuildRequires: python-module-memory_profiler
BuildRequires: python-module-et_xmlfile
BuildRequires: python-module-numpy
BuildRequires: python-module-pandas

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-test
BuildRequires: python3-module-jdcal
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-memory_profiler
BuildRequires: python3-module-et_xmlfile
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pandas
%endif

%py_provides %oname

%description
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

%package -n python3-module-%oname
Summary: A Python library to read/write Excel 2007 xlsx/xlsm files
Group: Development/Python3
%py3_provides %oname
%py3_requires jdcal et_xmlfile

%description -n python3-module-%oname
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p2

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- automated PyPI update

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.b1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.b1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.b1
- Version 2.3.0-b1

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Initial build for Sisyphus

