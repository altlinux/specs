Name:     elogind
Version:  239.3
Release:  alt1
Summary:  The systemd project's "logind", extracted to a standalone package
Group:    System/Configuration/Boot and Init
License:  GPL2, LGPL2.1
URL:      https://github.com/elogind/elogind
Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

Conflicts: ConsoleKit2 ConsoleKit2-x11
Conflicts: systemd-services

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gperf
BuildRequires: xsltproc
BuildRequires: docbook-xsl
BuildRequires: libacl-devel
BuildRequires: libaudit-devel
BuildRequires: libblkid-devel
BuildRequires: libcap-devel
BuildRequires: libkeyutils-devel
BuildRequires: libmount-devel
BuildRequires: libpam0-devel
BuildRequires: libpolkit-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: libudev-devel

%description
Elogind is the systemd project's "logind", extracted out to be a
standalone daemon.  It integrates with PAM to know the set of users
that are logged in to a system and whether they are logged in
graphically, on the console, or remotely.


%package devel
Summary:  Development libraries for elogind
Group:    Development/C


%description devel
Header and Library files for doing development with the elogind.


%prep
%setup


%build
%meson \
 -Drootlibdir=/%_lib \
 -Dpamlibdir=/%_lib/security \
 -Dcgroup-controller=%name \
 -Ddefault-hierarchy=hybrid \
 -Ddefault-kill-user-processes=false \
 -Dtty-gid=5 \
 -Dsystem-uid-max=499 \
 -Dsystem-gid-max=499 \
 -Dsplit-usr=true \
 -Dman=true \
 -Dutmp=true \
 -Dpolkit=true \
 -Dacl=true \
 -Daudit=true \
 -Dpam=true \
 -Dselinux=true \
 -Dhalt-path=/sbin/halt \
 -Dreboot-path=/sbin/reboot \
 -Dtests=false \
#
%meson_build


%install
%meson_install
%find_lang %name

rm -rf -- \
	%buildroot/%_datadir/bash-completion \
	%buildroot/%_datadir/zsh \
	%buildroot/%_datadir/factory \
	%buildroot/%_datadir/doc

# rule in the udev-rules
rm -f -- %buildroot/lib/udev/rules.d/70-power-switch.rules


%files -f %name.lang
%config(noreplace) %_sysconfdir/%name/logind.conf
%config(noreplace) %_sysconfdir/pam.d/elogind-user
/bin/elogind-inhibit
/bin/loginctl
%_bindir/busctl
/lib/%name
/lib/udev/rules.d/*.rules
/%_lib/*.so.*
/%_lib/security/pam_elogind.so
%_datadir/dbus-1/system-services/org.freedesktop.login1.service
%_datadir/dbus-1/system.d/org.freedesktop.login1.conf
%_datadir/polkit-1/actions/org.freedesktop.login1.policy
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*


%files devel
%_includedir/%name
/%_lib/*.so
%_pkgconfigdir/libelogind.pc
%_man3dir/*


%changelog
* Wed Jan 02 2019 Alexey Gladkov <legion@altlinux.ru> 239.3-alt1
- New version (239.3).

* Thu Mar 22 2018 Alexey Gladkov <legion@altlinux.ru> 235.3-alt1
- First build.

