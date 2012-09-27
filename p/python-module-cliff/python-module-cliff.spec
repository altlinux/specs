Name:		python-module-cliff
Version:	1.0
Release:	alt1
Summary:	Command Line Interface Formulation Framework

Group:		Development/Python
License:	ASL 2.0
URL:		http://pypi.python.org/pypi/cliff
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-distribute
BuildRequires:	python-module-prettytable
BuildRequires:	python-module-cmd2
BuildRequires:	python-module-tablib

Requires:	python-module-distribute
Requires:	python-module-prettytable
Requires:	python-module-cmd2
Requires:	python-module-tablib

%description
cliff is a framework for building command line programs. It uses
setuptools entry points to provide subcommands, output formatters, and
other extensions.

Documentation for cliff is hosted on readthedocs.org at
http://readthedocs.org/docs/cliff/en/latest/

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%check
%{__python} setup.py test

%files
%doc docs/
%{python_sitelibdir}/cliff
%{python_sitelibdir}/cliff-%{version}*

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt1
- Initial release for Sisyphus (based on Fedora)
