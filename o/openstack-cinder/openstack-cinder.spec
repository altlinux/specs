
%add_python_req_skip hp3parclient

Name: openstack-cinder
Version: 2015.1.0
Release: alt0.b2.0
Summary: OpenStack Volume service

Group: System/Servers
License: ASL 2.0
Url: http://www.openstack.org/software/openstack-storage/
Source0: %name-%version.tar
Source1: cinder-dist.conf
Source2: cinder.logrotate
Source3: cinder-tgt.conf
Source4: %name.tmpfiles
Source5: cinder.conf.sample

Source10: openstack-cinder-api.service
Source11: openstack-cinder-scheduler.service
Source12: openstack-cinder-volume.service
Source13: openstack-cinder-backup.service

Source110: openstack-cinder-api.init
Source111: openstack-cinder-scheduler.init
Source112: openstack-cinder-volume.init
Source113: openstack-cinder-backup.init

Source20: cinder-sudoers

#
# patches_base=2014.1.1
#
Patch0002: 0002-Remove-runtime-dep-on-python-pbr-python-d2to1.patch

BuildArch: noarch
BuildRequires: python-module-d2to1
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr
BuildRequires: python-module-sphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-netaddr
BuildRequires: crudini

BuildRequires: graphviz
BuildRequires: python-module-eventlet
BuildRequires: python-module-routes
BuildRequires: python-module-SQLAlchemy
BuildRequires: python-module-webob
BuildRequires: python-module-migrate
BuildRequires: python-module-iso8601

Requires: openstack-utils
Requires: python-module-cinder = %version-%release

Requires(pre): shadow-utils

Requires: lvm2
Requires: scsitarget-utils
Requires: targetcli
Requires: python-module-rtslib
Requires: sysfsutils
Requires: sudo
Requires: qemu-img

%description
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

%package -n       python-module-cinder
Summary: OpenStack Volume Python libraries
Group: System/Servers

%description -n   python-module-cinder
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the cinder Python library.

%package doc
Summary: Documentation for OpenStack Volume
Group: Development/Documentation

%description doc
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains documentation files for cinder.

%prep
%setup

%patch0002 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find cinder -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# We add REDHATCINDERVERSION/RELEASE with the pbr removal patch
sed -i s/REDHATCINDERVERSION/%version/ cinder/version.py
sed -i s/REDHATCINDERRELEASE/%release/ cinder/version.py

install -p -D -m 640 %SOURCE5 etc/cinder/cinder.conf.sample

%build
%python_build

%install
%python_install

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-build -b man -c source source/man build/man
mkdir -p %buildroot%_mandir/man1
install -p -D -m 644 build/man/*.1 %buildroot%_mandir/man1/

popd

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/cinder
install -d -m 755 %buildroot%_sharedstatedir/cinder/tmp
install -d -m 755 %buildroot%_logdir/cinder

# Install config files
install -d -m 755 %buildroot%_sysconfdir/cinder
install -p -D -m 640 %SOURCE1 %buildroot%_datadir/cinder/cinder-dist.conf
install -p -D -m 640 etc/cinder/cinder.conf.sample %buildroot%_sysconfdir/cinder/cinder.conf
install -d -m 755 %buildroot%_sysconfdir/cinder/volumes
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/tgt/conf.d/cinder.conf
install -p -D -m 640 etc/cinder/rootwrap.conf %buildroot%_sysconfdir/cinder/rootwrap.conf
install -p -D -m 640 etc/cinder/api-paste.ini %buildroot%_sysconfdir/cinder/api-paste.ini
install -p -D -m 640 etc/cinder/policy.json %buildroot%_sysconfdir/cinder/policy.json

# Install initscripts for services
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/openstack-cinder-api.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/openstack-cinder-scheduler.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/openstack-cinder-volume.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/openstack-cinder-backup.service
install -p -D -m 644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf

install -p -D -m 755 %SOURCE110 %buildroot%_initdir/openstack-cinder-api
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/openstack-cinder-scheduler
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/openstack-cinder-volume
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/openstack-cinder-backup

# Install sudoers
install -p -D -m 400 %SOURCE20 %buildroot%_sysconfdir/sudoers.d/cinder

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/openstack-cinder

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/cinder

# Install rootwrap files in /usr/share/cinder/rootwrap
mkdir -p %buildroot%_datadir/cinder/rootwrap/
install -p -D -m 644 etc/cinder/rootwrap.d/* %buildroot%_datadir/cinder/rootwrap/

# Remove unneeded in production stuff
rm -f %buildroot%_bindir/cinder-debug
rm -fr %buildroot%python_sitelibdir/cinder/tests
rm -f %buildroot%python_sitelibdir/cinder/openstack/common/test.*
rm -f %buildroot%python_sitelibdir/cinder/test.*
rm -fr %buildroot%python_sitelibdir/run_tests.*
rm -f %buildroot/usr/share/doc/cinder/README*

%pre
# 165:165 for ceilometer (openstack-cinder)
%_sbindir/groupadd -r -g 165 -f cinder 2>/dev/null ||:
%_sbindir/useradd -r -u 165 -g cinder -G cinder,nobody,wheel  -c 'OpenStack Cinder Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/cinder cinder 2>/dev/null ||:


%post
%post_service %name-volume
%post_service %name-api
%post_service %name-scheduler
%post_service %name-backup

%preun
%preun_service %name-volume
%preun_service %name-api
%preun_service %name-scheduler
%preun_service %name-backup

%files
%doc LICENSE
%dir %_sysconfdir/cinder
%config(noreplace) %attr(-, root, cinder) %_sysconfdir/cinder/cinder.conf
%config(noreplace) %attr(-, root, cinder) %_sysconfdir/cinder/api-paste.ini
%config(noreplace) %attr(-, root, cinder) %_sysconfdir/cinder/rootwrap.conf
%config(noreplace) %attr(-, root, cinder) %_sysconfdir/cinder/policy.json
%config(noreplace) %_sysconfdir/logrotate.d/openstack-cinder
%config(noreplace) %_sysconfdir/sudoers.d/cinder
%config(noreplace) %_sysconfdir/tgt/conf.d/cinder.conf
%attr(-, root, cinder) %_datadir/cinder/cinder-dist.conf

%dir %attr(0750, cinder, root) %_logdir/cinder
%dir %attr(0755, cinder, root) %_runtimedir/cinder
%dir %attr(0755, cinder, root) %_sysconfdir/cinder/volumes

%_bindir/cinder-*
%_unitdir/*
%_initdir/*
%_tmpfilesdir/*
%_datadir/cinder
%_man1dir/cinder*.1.*

%defattr(-, cinder, cinder, -)
%dir %_sharedstatedir/cinder
%dir %_sharedstatedir/cinder/tmp

%files -n python-module-cinder
%python_sitelibdir/*

%files doc
%doc doc/build/html

%changelog
* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- 2014.1.1

* Sat Aug 09 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt3
- sysfsutils added to Requires: warning about systool

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt2
- user cinder added to wheel group, for cinder-rootwrap

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- Initial build for Sisyphus (based on Fedora)
- New version - icehouse

