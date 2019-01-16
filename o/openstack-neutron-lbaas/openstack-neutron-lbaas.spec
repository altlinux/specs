%define oname neutron-lbaas

Name: openstack-%oname
Version: 13.0.0
Release: alt1
Epoch: 1
Summary: OpenStack Networking LBaaS

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: neutron-lbaasv2-agent.init
Source2: neutron-lbaasv2-agent.service

BuildArch: noarch

Requires: openstack-neutron
Requires: python3-module-%oname = %EVR
Requires: haproxy


BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-neutron-lib >= 1.18.0
BuildRequires: python-module-neutron >= 1:12.0.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-alembic >= 0.8.10
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.messaging >= 5.29.0
BuildRequires: python-module-oslo.reports >= 1.18.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.service >= 1.24.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-barbicanclient >= 4.5.2
BuildRequires: python-module-pyasn1 >= 0.1.8
BuildRequires: python-module-pyasn1-modules >= 0.0.6
BuildRequires: python-module-pymysql >= 0.7.6
BuildRequires: python-module-OpenSSL >= 17.1.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-keystoneauth1 >= 3.4.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-neutron-lib >= 1.18.0
BuildRequires: python3-module-neutron >= 1:12.0.0
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-alembic >= 0.8.10
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.reports >= 1.18.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-barbicanclient >= 4.5.2
BuildRequires: python3-module-pyasn1 >= 0.1.8
BuildRequires: python3-module-pyasn1-modules >= 0.0.6
BuildRequires: python3-module-pymysql >= 0.7.6
BuildRequires: python3-module-OpenSSL >= 17.1.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-keystoneauth1 >= 3.4.0

%description
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%oname
Summary: Neutron LBaaS Python libraries
Group: Development/Python
Requires: python-module-neutron
Requires: python-module-neutron-lib
%add_python_req_skip a10_neutron_lbaas
%add_python_req_skip brocade_neutron_lbaas
%add_python_req_skip heleosapi
%add_python_req_skip kemptech_openstack_lbaas
%add_python_req_skip f5lbaasdriver

%description -n python-module-%oname
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

This package contains the neutron Python library.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Neutron LBaaS Python3 libraries
Group: Development/Python3
Requires: python3-module-neutron
Requires: python3-module-neutron-lib
%add_python3_req_skip a10_neutron_lbaas
%add_python3_req_skip brocade_neutron_lbaas
%add_python3_req_skip heleosapi
%add_python3_req_skip kemptech_openstack_lbaas
%add_python3_req_skip f5lbaasdriver
%add_python3_req_skip f5lbaasdriver.v2.bigip.driver_v2

%description -n python3-module-%oname
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

This package contains the neutron Python3 library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let's handle dependencies ourseleves
#rm -f requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
PYTHONPATH=. tools/generate_config_file_samples.sh
popd


%install
%python_install --install-data=/

for f in $(ls -1 %buildroot%_bindir)
    do mv %buildroot%_bindir/$f %buildroot%_bindir/$f.py2
done

pushd ../python3
%python3_install --install-data=/
# configuration files
install -p -D -m 644 etc/neutron_lbaas.conf.sample %buildroot%_sysconfdir/neutron/neutron_lbaas.conf
install -p -D -m 644 etc/lbaas_agent.ini.sample %buildroot%_sysconfdir/neutron/lbaas_agent.ini
install -p -D -m 644 etc/services_lbaas.conf.sample %buildroot%_sysconfdir/neutron/services_lbaas.conf
popd


# Install sysV init scripts
install -p -D -m 755 %SOURCE1 %buildroot%_initdir/neutron-lbaasv2-agent
# Install systemd units
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/neutron-lbaasv2-agent.service

# Remove unused files

%post
%post_service neutron-lbaasv2-agent

%preun
%preun_service neutron-lbaasv2-agent

%files
%doc LICENSE
%doc README.rst
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.conf
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/*.filters
%_initdir/neutron-lbaasv2-agent
%_unitdir/neutron-lbaasv2-agent.service

%files -n python-module-%oname
%_bindir/*.py2
%doc LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files -n python-module-%oname-tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc LICENSE
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 1:13.0.0-alt1
- 13.0.0
- switch to python3

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 1:10.0.1-alt2
- Fixed FTBFS (remove python-module-setuptools-tests from BR).

* Wed Jul 19 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.1-alt1
- 10.0.1

* Wed Jun 07 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.0-alt1
- 10.0.0

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:9.2.0-alt1
- 9.2.0

* Thu Nov 10 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.0-alt2
- add read config /etc/sysconfig/neutron for start daemon
- add pre,post service

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.0-alt1
- 9.1.0
- drop support lbaas v1

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.3-alt1
- 7.0.3

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt1
- 7.0.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- initial build for Kilo
