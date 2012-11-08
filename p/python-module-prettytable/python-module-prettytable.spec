Name:		python-module-prettytable
Version:	0.6.1
Release:	alt1
Summary:	Python library to display tabular data in tables

Group:		Development/Python
License:	BSD
Source0:	%{name}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/PrettyTable

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-distribute

%description
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%prep
%setup -q

%build
%{__python} setup.py build

%check
%{__python} prettytable_test.py

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc README COPYING CHANGELOG
%{python_sitelibdir}/prettytable.py*
%{python_sitelibdir}/prettytable-%{version}*

%changelog
* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.1-alt1
- Initial release for Sisyphus (based on Fedora)
