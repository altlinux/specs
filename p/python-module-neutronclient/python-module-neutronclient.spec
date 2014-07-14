Name:       python-module-neutronclient
Version:    2.3.4
Release:    alt1
Summary:    Python API and CLI for OpenStack Neutron
Group:      Development/Python

License:    ASL 2.0
URL:        http://launchpad.net/python-neutronclient/
Source0:    %{name}-%{version}.tar

#
# patches_base=2.3.4
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr

%description
Client library and command line utility for interacting with Openstack
Neutron's API.

%prep
%setup

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATNEUTRONCLIENTVERSION/%{version}/ neutronclient/version.py

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python_build

%install
%python_install

# Install other needed files
install -p -D -m 644 tools/neutron.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/neutron.bash_completion

# Remove unused files
rm -rf %{buildroot}%{python_sitelibdir}/neutronclient/tests

%files
%doc LICENSE
%doc README.rst
%{_bindir}/neutron
%{python_sitelibdir}/neutronclient
%{python_sitelibdir}/*.egg-info
%{_sysconfdir}/bash_completion.d

%changelog
* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.4-alt1
- First build for ALT (based on Fedora 2.3.4-1.fc21.src)
