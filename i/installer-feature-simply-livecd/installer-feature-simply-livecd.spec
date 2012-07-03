Name: installer-feature-simply-livecd
Version: 0.7.6
Release: alt4

Summary: LiveCD install hooks for Simply Linux.
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-livecd >= 0.5
Conflicts: installer-common-stage2
Conflicts: livecd-install < 0.6-alt2
Provides: installer-features-simply-livecd
Obsoletes: installer-features-simply-livecd < 0.3

Requires: libshell

# Run installer features while install from LiveCD.
Requires: livecd-installer-features

# Installer fearures for Simply Linux.
Requires: installer-feature-autohostname-stage2
Requires: installer-feature-setup-network-stage3
Requires: installer-feature-samba-usershares-stage2
Requires: installer-feature-desktop-other-fs-stage2
Requires: installer-feature-sudo-enable-by-default-stage2
Requires: installer-feature-nfs-client-stage3
Requires: installer-feature-online-repo
Requires: installer-feature-bell-off-stage3
Requires: installer-feature-cpufreq-stage3
Requires: installer-feature-hdd-pm-disable-stage3

%description
LiveCD install hooks for Simply Linux.

%prep
%setup

%install
%define init_hookdir %_libexecdir/alterator/hooks/livecd-initinstall.d
%define pre_hookdir %_libexecdir/alterator/hooks/livecd-preinstall.d
%define post_hookdir %_libexecdir/alterator/hooks/livecd-postinstall.d
mkdir -p %buildroot%init_hookdir
mkdir -p %buildroot%pre_hookdir
mkdir -p %buildroot%post_hookdir
install -pm755 livecd-initinstall.d/* %buildroot%init_hookdir/
install -pm755 livecd-preinstall.d/* %buildroot%pre_hookdir/
install -pm755 livecd-postinstall.d/* %buildroot%post_hookdir/

%files
%init_hookdir/*
%pre_hookdir/*
%post_hookdir/*

%changelog
* Fri Dec 23 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt4
- Add disable-whatis hook.
- Drop updatedb.sh.

* Thu Nov 24 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt3
- Use installer-feature-hdd-pm-disable-stage3.

* Thu Nov 03 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt2
- Use installer-feature-cpufreq-stage3.

* Thu Sep 22 2011 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt1
- services: Turn on crond, anacron and dnsmasq.
- Use own setup-resume install hook.
- Use installer-feature-bell-off-stage3.
- gdm: Set SoundOnLogin=false.

* Thu Aug 25 2011 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt1
- setup-user-groups hook: Add vboxusers group.

* Mon Aug 22 2011 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- gdm: Simplify greeter.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Install all hooks.
- Set gdm theme 'simply' again.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Return gdm theme 'simple'.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Change gdm-theme: simple -> simply.
- Rename hook: gdm-simple -> gdm-theme.

* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Add vm-profile hook.
- Add setup-user-groups hook.
- Use installer-feature-online-repo instead of own hook.
- Add dependences on installer-features for Simply.

* Wed Jul 20 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Add updatedb hook.
- Kill polkit agent before install.

* Mon Jun 20 2011 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Map hostname to 127.0.0.1.

* Thu Jun 16 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt1
- Drop remove-installer-pkgs hook.

* Mon Jun 06 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- Use digital prefix for hooks.
- Add remove-installer-pkgs hook.

* Thu Jun 02 2011 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- livecd-postinstall.d -> livecd-preinstall.d.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Rename package.
- Disable zram-swap.

* Tue May 24 2011 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Add online-repo hook.

* Fri May 20 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build

