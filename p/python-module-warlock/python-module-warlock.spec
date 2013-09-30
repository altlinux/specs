Name:		python-module-warlock
Version:	0.4.0
Release:	alt2
Summary:	Python object model built on top of JSON schema

Group:		Development/Python
License:	ASL 2.0
URL:		http://pypi.python.org/pypi/warlock/0.4.0
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-distribute
BuildRequires:	python-module-nose
BuildRequires:	python-module-jsonschema

Requires:	python-module-jsonschema

%description
Build self-validating python objects using JSON schemas

%prep
%setup -q
# Remove bundled egg-info
rm -rf warlock.egg-info

%build
%python_build

%check
nosetests

%install
%python_install

%files
%doc README.md LICENSE
%{python_sitelibdir}/warlock
%{python_sitelibdir}/warlock-%{version}-py?.?.egg-info

%changelog
* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 0.4.0-alt2
- Fix check section in spec

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.0-alt1
- Initial release for Sisyphus (based on Fedora)
