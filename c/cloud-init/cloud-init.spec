Name: cloud-init
Version: 0.6.3
Release: alt1
Summary: Cloud instance init scripts

Group: System/Configuration/Boot and Init
License: GPLv3
Url: http://launchpad.net/cloud-init

Source0: %name-%version.tar
Source1: %name-alt.cfg

Patch1: %name-0.6.3-lp970071.patch
Patch2: %name-0.6.3-alt-sshd-config.patch

BuildArch: noarch
BuildRequires: python-devel python-module-distribute python-module-nose python-module-mocker python-module-yaml python-module-cheetah python-module-oauth

Requires: systemd-sysvinit sudo

%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%python_build

%check
make test

%install
%python_install

for x in %buildroot/%_bindir/*.py; do mv "$x" "${x%%.py}"; done
chmod +x %buildroot/%python_sitelibdir/cloudinit/SshUtil.py
mkdir -p %buildroot/%_sharedstatedir/cloud

# We supply our own config file since our software differs from Ubuntu's.
cp -p %SOURCE1 %buildroot/%_sysconfdir/cloud/cloud.cfg

# Install the systemd bits
mkdir -p        %buildroot/%systemd_unitdir
cp -p systemd/* %buildroot/%systemd_unitdir

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
%doc ChangeLog TODO
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
* Thu May 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.3-alt1
- initial

