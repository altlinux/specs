%global modname cliff

Name:             python-module-cliff
Version:          1.6.1
Release:          alt1
Summary:          Command Line Interface Formulation Framework

Group:            Development/Python
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/cliff
Source0:          %{name}-%{version}.tar

BuildArch:        noarch

BuildRequires:    python-devel
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
BuildRequires:    python-module-prettytable
BuildRequires:    python-module-cmd2 >= 0.6.7
BuildRequires:    python-module-stevedore
BuildRequires:    python-module-six

# Required for the test suite
BuildRequires:    python-module-nose
BuildRequires:    python-module-mock
BuildRequires:    bash
BuildRequires:    bash-completion

Requires:         python-module-setuptools
Requires:         python-module-prettytable
Requires:         python-module-cmd2 >= 0.6.7
Requires:         python-module-stevedore
Requires:         python-module-six

BuildRequires:    python-module-argparse
Requires:         python-module-argparse


%description
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

Documentation for cliff is hosted on readthedocs.org at
http://readthedocs.org/docs/cliff/en/latest/

%prep
%setup

# Remove bundled egg info
rm -rf *.egg-info

%build
%python_build

%install
%python_install

%check
PYTHONPATH=. nosetests

%files
%doc docs/
%{python_sitelibdir}/%{modname}
%{python_sitelibdir}/%{modname}-%{version}*

%changelog
* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 1.6.1-alt1
- New version

* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt2
- Remove distribute bootstrap
- Fix check section in spec

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt1
- Initial release for Sisyphus (based on Fedora)
