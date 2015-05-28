Name:    cloud-init
Version: 0.7.6
Release: alt1

Summary: Cloud instance init scripts
Group:   System/Configuration/Boot and Init
License: GPLv3
Url:     http://launchpad.net/cloud-init

Source0: %name-%version.tar
Source1: %name-alt.cfg

Patch1: %name-0.7.6-alt-sshd-config.patch
Patch2: %name-add-alt-distro.patch
Patch3: %name-0.7.6-alt-blkid-path.patch

BuildArch: noarch
BuildRequires: python-devel python-module-distribute python-module-nose python-module-mocker
BuildRequires: python-module-yaml python-module-cheetah python-module-oauth
# For tests
BuildRequires: python-modules-json python-module-requests python-module-jsonpatch python-module-configobj
BuildRequires: python-module-httpretty python-module-serial iproute2 util-linux net-tools python-module-jinja2

Requires: systemd-sysvinit sudo

%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%python_build

%check
# Ignore test_netconfig.py because test_simple_write_freebsd is broken
make test noseopts="-I test_netconfig.py"

%install
%python_install --init-system=systemd

# We supply our own config file since our software differs from Ubuntu's.
cp -p %SOURCE1 %buildroot/%_sysconfdir/cloud/cloud.cfg

mkdir -p %buildroot/%_sharedstatedir/cloud

%pre
%_sbindir/useradd -G wheel -c "EC2 administrative account" ec2-user >/dev/null 2>&1 ||:

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    # Enabled by default per "runs once then goes away" exception
    /bin/systemctl enable cloud-config.service     >/dev/null 2>&1 || :
    /bin/systemctl enable cloud-final.service      >/dev/null 2>&1 || :
    /bin/systemctl enable cloud-init.service       >/dev/null 2>&1 || :
    /bin/systemctl enable cloud-init-local.service >/dev/null 2>&1 || :
    echo "%%wheel ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable cloud-config.service >/dev/null 2>&1 || :
    /bin/systemctl --no-reload disable cloud-final.service  >/dev/null 2>&1 || :
    /bin/systemctl --no-reload disable cloud-init.service   >/dev/null 2>&1 || :
    /bin/systemctl --no-reload disable cloud-init-local.service >/dev/null 2>&1 || :
    # One-shot services -> no need to stop
fi

%files
%doc ChangeLog TODO.rst
%config(noreplace) %_sysconfdir/cloud/cloud.cfg
%dir               %_sysconfdir/cloud/cloud.cfg.d
%config(noreplace) %_sysconfdir/cloud/cloud.cfg.d/*.cfg
%doc               %_sysconfdir/cloud/cloud.cfg.d/README
%dir               %_sysconfdir/cloud/templates
%config(noreplace) %_sysconfdir/cloud/templates/*
%systemd_unitdir/cloud-config.service
%systemd_unitdir/cloud-config.target
%systemd_unitdir/cloud-final.service
%systemd_unitdir/cloud-init-local.service
%systemd_unitdir/cloud-init.service
%python_sitelibdir/*
/usr/lib/%name
%_bindir/cloud-init*
%doc %_datadir/doc/%name
%dir %_sharedstatedir/cloud

%changelog
* Thu May 28 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Thu May 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.3-alt1
- initial

