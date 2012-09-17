Name:		python-module-warlock
Version:	0.4.0
Release:	alt1
Summary:	Python object model built on top of JSON schema

Group:		Development/Python
License:	ASL 2.0
URL:		http://pypi.python.org/pypi/warlock/0.4.0
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-distribute

Requires:	python-module-jsonschema
BuildRequires:	python-module-jsonschema

%description
Build self-validating python objects using JSON schemas

%prep
%setup -q
# Remove bundled egg-info
rm -rf warlock.egg-info

%build
%{__python} setup.py build

%check
%{__python} setup.py test

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.md LICENSE
%{python_sitelibdir}/warlock
%{python_sitelibdir}/warlock-%{version}-py?.?.egg-info

%changelog
* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.0-alt1
- Initial release for Sisyphus (based on Fedora)
