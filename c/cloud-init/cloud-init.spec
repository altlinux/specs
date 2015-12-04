Name:    cloud-init
Version: 0.7.6
Release: alt2.20151202

Summary: Cloud instance init scripts
Group:   System/Configuration/Boot and Init
License: GPLv3
Url:     http://launchpad.net/cloud-init

Source0: %name-%version.tar

Patch1: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: python-devel python-module-distribute python-module-nose python-module-mocker
BuildRequires: python-module-yaml python-module-cheetah python-module-oauth
# For tests
BuildRequires: python-modules-json python-module-requests python-module-jsonpatch python-module-configobj python-module-mock python-module-oauthlib
BuildRequires: python-module-httpretty python-module-serial iproute2 util-linux net-tools python-module-jinja2 python-module-contextlib2 python-module-prettytable

Requires: sudo
Requires: e2fsprogs
Requires: cloud-utils-growpart
Requires: procps
Requires: iproute net-tools
Requires: shadow-utils
Requires: /bin/run-parts
# add not autoreq'ed
%py_requires Cheetah
%py_requires jinja2

%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.

%prep
%setup
%patch1 -p1

%build
%python_build

%install
%python_install --init-system=systemd

install -pD -m644 altlinux/cloud-init-alt.cfg %buildroot%_sysconfdir/cloud/cloud.cfg
install -pD -m644 altlinux/cloud-init-tmpfiles.conf %buildroot%_tmpfilesdir/cloud-init.conf
install -pD -m755 altlinux/cloud-config %buildroot%_initdir/cloud-config
install -pD -m755 altlinux/cloud-final %buildroot%_initdir/cloud-final
install -pD -m755 altlinux/cloud-init %buildroot%_initdir/cloud-init
install -pD -m755 altlinux/cloud-init-local %buildroot%_initdir/cloud-init-local

mkdir -p %buildroot%_libexecdir
mv %buildroot/usr/libexec/%name %buildroot%_libexecdir/
mkdir -p %buildroot%_sharedstatedir/cloud

# Don't ship the tests
rm -r %buildroot%python_sitelibdir/tests

# Remove non-ALTLinux templates
rm -f %buildroot%_sysconfdir/cloud/templates/*.debian.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.freebsd.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.redhat.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.suse.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.ubuntu.*

%check
export PATH=/sbin:/usr/sbin:/bin:/usr/bin:$PATH
# Ignore test_netconfig.py because test_simple_write_freebsd is broken
make test noseopts="-I test_cloudstack.py"

%post
%post_service cloud-config
%post_service cloud-final
%post_service cloud-init
%post_service cloud-init-local

%preun
%preun_service cloud-config
%preun_service cloud-final
%preun_service cloud-init
%preun_service cloud-init-local

%files
%doc ChangeLog TODO.rst
%config(noreplace) %_sysconfdir/cloud/cloud.cfg
%dir               %_sysconfdir/cloud/cloud.cfg.d
%config(noreplace) %_sysconfdir/cloud/cloud.cfg.d/*.cfg
%doc               %_sysconfdir/cloud/cloud.cfg.d/README
%dir               %_sysconfdir/cloud/templates
%config(noreplace) %_sysconfdir/cloud/templates/*
/lib/udev/rules.d/66-azure-ephemeral.rules
%_initdir/*
%_unitdir/*
%_tmpfilesdir/*
%python_sitelibdir/*
%_libexecdir/%name
%_bindir/cloud-init*
%doc %_datadir/doc/%name
%dir %_sharedstatedir/cloud

%changelog
* Wed Dec 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.6-alt2.20151202
- upstream snapshot
- add ALTLinux support
- add SysV init scripts
- don't add ec2-user user

* Thu May 28 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Thu May 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.3-alt1
- initial

