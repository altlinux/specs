%define sname neutron-lbaas

Name: openstack-%sname
Version: 2015.1.1
Release: alt1
Summary: OpenStack Networking LBaaS

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar
Source1: neutron-lbaas-agent.init
Source2: neutron-lbaas-agent.service

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-six
BuildRequires: python-module-d2to1

Requires: openstack-neutron >= 2015.1.1
Requires: python-module-%sname = %version-%release

%description
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%sname
Summary: Neutron LBaaS Python libraries
Group: Development/Python
Requires: python-module-neutron >= 2015.1.1
%add_python_req_skip a10_neutron_lbaas
%add_python_req_skip brocade_neutron_lbaas
%add_python_req_skip heleosapi

%description -n python-module-%sname
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

This package contains the neutron Python library.

%prep
%setup

# Let's handle dependencies ourseleves
#rm -f requirements.txt

%build
%python_build

%install
%python_install --install-data=/

# Install sysV init scripts
install -p -D -m 755 %SOURCE1 %buildroot%_initdir/neutron-lbaas-agent
# Install systemd units
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/neutron-lbaas-agent.service

# Remove unused files

%files
%doc LICENSE
%doc README.rst
%_bindir/*
%config(noreplace) %_sysconfdir/neutron/*
%_initdir/neutron-lbaas-agent
%_unitdir/neutron-lbaas-agent.service

%files -n python-module-%sname
%doc LICENSE
%python_sitelibdir/neutron_lbaas
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron_lbaas/tests


%changelog
* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- initial build for Kilo
