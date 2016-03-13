%define oname prettytable

%def_with python3

Name:		python-module-%oname
Version:	0.7.2
Release:	alt2.1
Summary:	Python library to display tabular data in tables

Group:		Development/Python
License:	BSD
Source0:	%{name}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/PrettyTable

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:	python3-devel
BuildRequires:	python3-module-setuptools
%endif

%py_provides %oname

%description
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%package -n python3-module-%oname
Summary:	Python library to display tabular data in tables
Group:		Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%prep
%setup

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

%check
export LC_ALL=en_US.UTF-8
python prettytable_test.py
%if_with python3
pushd ../python3
python3 prettytable_test.py
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README COPYING CHANGELOG
%{python_sitelibdir}/prettytable.py*
%{python_sitelibdir}/prettytable-%{version}*

%if_with python3
%files -n python3-module-%oname
%doc README COPYING CHANGELOG
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2
- Added provides: %oname

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2
- Added module for Python 3

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.1-alt1
- Initial release for Sisyphus (based on Fedora)
