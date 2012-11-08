Name:		python-module-quantumclient
Version:	2.1.1
Release:	alt1
Summary:	Python API and CLI for OpenStack Quantum

Group:		Development/Python
License:	ASL 2.0
URL:		https://github.com/openstack/python-quantumclient
BuildArch:	noarch

Source0:	%{name}-%{version}.tar.gz

Requires:	python-module-cliff >= 1.0
Requires:	python-module-httplib2
Requires:	python-module-prettytable >= 0.6
Requires:	python-module-distribute
Requires:	python-module-simplejson

BuildRequires:	python-devel
BuildRequires:	python-module-distribute

%description
Client library and command line utility for interacting with Openstack
Quantum's API.

%prep
%setup -q

# Change cliff version requirement (https://bugs.launchpad.net/python-quantumclient/+bug/1049989)
sed -i 's/cliff>=1.2.1/cliff>=1.0/' tools/pip-requires

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove unused files
rm -rf %{buildroot}%{python_sitelibdir}/quantumclient/tests

%files
%doc LICENSE
%doc README
%{_bindir}/quantum
%{python_sitelibdir}/quantumclient
%{python_sitelibdir}/*.egg-info

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.1.1-alt1
- Initial release for Sisyphus (based on Fedora)
