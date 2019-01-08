Name:     elogind
Version:  239.3
Release:  alt2
Summary:  The systemd project's "logind", extracted to a standalone package
Group:    System/Configuration/Boot and Init
License:  GPL2, LGPL2.1
URL:      https://github.com/elogind/elogind
Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source1: elogind-dbus-helper
Source2: elogind.init
Source3: elogind.sysconfig

Patch0: elogind-fix-stale-pidfile.patch
Patch1: elogind-dbus-activation-helper.patch
Patch2: elogind-create-run-systemd-system.patch

Conflicts: ConsoleKit2
Conflicts: ConsoleKit2-x11
Conflicts: systemd
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

Conflicts: libsystemd-devel


%description devel
Header and Library files for doing development with the elogind.


%package -n bash-completion-%name
Summary: Bash completion for %name utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %version-%release

%description -n bash-completion-%name
Bash completion for %name.


%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1


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
	%buildroot/%_datadir/zsh \
	%buildroot/%_datadir/factory \
	%buildroot/%_datadir/doc

# rule in the udev-rules
rm -f -- %buildroot/lib/udev/rules.d/70-power-switch.rules

install -m755 -pD %SOURCE1 %buildroot/lib/%name/elogind-dbus-helper
install -m755 -pD %SOURCE2 %buildroot/%_initdir/elogind
install -m644 -pD %SOURCE3 %buildroot/%_sysconfdir/sysconfig/elogind


for f in %buildroot/lib/udev/rules.d/*.rules; do
	n="${f##*/}"
	mv -f -- "$f" "${f%%/*}/${n%%%%-*}-elogind-${n#*-}"
done

for f in \
	%_bindir/busctl /bin/loginctl \
	%_man1dir/busctl.1 %_man1dir/loginctl.1 %_man5dir/logind.conf.5 \
	;
do
	n="${f##*/}"
	d="${f%%/*}"

	mv -f -- "%buildroot/$f" "%buildroot/$d/e$n"
	ln -s -- "e$n" "%buildroot/$f"

	sed -i \
		-e "s#/$n#/e$n#g" \
		%buildroot/lib/udev/rules.d/*.rules
done

sed -i \
	-e '/^complete -F _loginctl loginctl/a \
complete -F _loginctl eloginctl' \
	%buildroot/%_datadir/bash-completion/completions/loginctl
ln -s loginctl %buildroot/%_datadir/bash-completion/completions/eloginctl


%files -f %name.lang
%config(noreplace) %_sysconfdir/%name/logind.conf
%config(noreplace) %_sysconfdir/pam.d/elogind-user
%config(noreplace) %_sysconfdir/sysconfig/elogind
%_initdir/elogind
/bin/elogind-inhibit
/bin/loginctl
/bin/eloginctl
%_bindir/busctl
%_bindir/ebusctl
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


%files -n bash-completion-%name
%_datadir/bash-completion/completions/*


%changelog
* Mon Jan 07 2019 Alexey Gladkov <legion@altlinux.ru> 239.3-alt2
- Add sysv init-script;
- Add bash-completion sub-package;
- Make dbus activation optional;
- Rename some files to reduce conflicts;
- Increase compatibility with systemd-logind.

* Wed Jan 02 2019 Alexey Gladkov <legion@altlinux.ru> 239.3-alt1
- New version (239.3).

* Thu Mar 22 2018 Alexey Gladkov <legion@altlinux.ru> 235.3-alt1
- First build.

