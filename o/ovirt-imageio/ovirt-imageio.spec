

Name: ovirt-imageio
Version: 2.4.7
Release: alt1
Summary: oVirt imageio
Group: System/Configuration/Other

License: GPLv2+
Url: https://github.com/oVirt/%name
Source: %name-%version.tar
Patch: %name-%version.patch

%global ovirtimg_user ovirtimg
%global srcname ovirt_imageio
%global logdir %_logdir/%name
%global admin_confdir %_sysconfdir/%name
%global vendor_confdir %prefix/lib/%name


BuildRequires(pre): rpm-build-python3 rpm-macros-systemd
BuildRequires: python3-devel python3-module-setuptools

%description
Transfer disk images on oVirt system.

%package -n python3-module-%name
Summary: oVirt imageio common resources
Group: Development/Python3
Provides: %name-common = %EVR
Provides: python3-module-%name-common = %EVR

%description -n python3-module-%name
Common resources used by oVirt imageio server and client

%package -n python3-module-%name-client
Summary: oVirt imageio client library
Group: Development/Python3
Provides: %name-client = %EVR

Requires: python3-module-%name = %EVR
# For "qemu:allocation-depth" meta context.
Requires: qemu-img >= 5.2.0

%description -n python3-module-%name-client
Python client library for accessing imageio server on oVirt hosts.

%package daemon
Summary: oVirt imageio daemon
Group: System/Servers
# NOTE: keep in sync with automation/check.packages
Requires: python3-module-%name = %EVR

%description daemon
Daemon providing image transfer service on oVirt hosts.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install
install -D -m 0755 --directory %buildroot%logdir
# Create a dummy log file to make rpm happy during build
touch %buildroot%logdir/daemon.log
install -D -m 0755 --directory %buildroot%vendor_confdir/conf.d
install -D -m 0755 --directory %buildroot%admin_confdir/conf.d
install -D -m 0644 data/README %buildroot%admin_confdir
install -D -m 0644 data/%name.service %buildroot%_unitdir/%name.service

%pre daemon
groupadd -r -f %ovirtimg_user >/dev/null 2>&1 ||:
useradd -r -g %ovirtimg_user -d /run/%name \
        -s /sbin/nologin -c "oVirt imageio" %ovirtimg_user >/dev/null 2>&1 ||:

%post daemon
# After installation, synchronize service state with preset files.
%systemd_post %name.service

%preun daemon
# Before uninstalling, stop and disable the service.
%systemd_preun %name.service

%postun daemon
# After upgrading, restart the service.
%systemd_postun_with_restart %name.service

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%srcname/client
%exclude %python3_sitelibdir/%srcname/admin

%files -n python3-module-%name-client
%python3_sitelibdir/%srcname/client
%_bindir/ovirt-img

%files daemon
%python3_sitelibdir/%srcname/admin
%_bindir/%name
%_bindir/%{name}ctl
%_unitdir/%name.service
%dir %admin_confdir
%dir %admin_confdir/conf.d
%dir %vendor_confdir
%dir %vendor_confdir/conf.d
%admin_confdir/README
%dir %attr(775, root, %ovirtimg_user) %logdir
%ghost %attr(644, %ovirtimg_user, %ovirtimg_user) %logdir/daemon.log*

%changelog
* Wed Mar 01 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.7-alt1
- 2.4.7

* Sat Aug 28 2021 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- Initial build.

