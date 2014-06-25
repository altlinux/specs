%define nm_version 0.9.9.98
%define nm_applet_version 0.9.9.98
%define nm_applet_name NetworkManager-applet-gtk
%define git_date %nil
#define git_date .git20130405
%define gtkver 3

Name: NetworkManager-ssh
Version: 0.9.3
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for SSH
Url: https://github.com/danfruehauf/NetworkManager-ssh
# git:git://github.com/danfruehauf/NetworkManager-ssh.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgnome-keyring-devel perl-XML-Parser
BuildRequires: intltool
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel

Requires: NetworkManager-daemon   >= %nm_version
Requires: openssh

%description
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager.

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: gnome-keyring
Requires: %nm_applet_name >= %nm_applet_version
Requires: %name = %version-%release

Obsoletes: %name-gnome < 0.9.1-alt2
Provides: %name-gnome = %version-%release

%description gtk
This package contains applications for use with
NetworkManager panel applet.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--with-gtkver=%gtkver \
	--enable-more-warnings=no
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files
%doc AUTHORS README README.md
%_libexecdir/NetworkManager/nm-ssh-service
%dir %_sysconfdir/NetworkManager/VPN
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-ssh-service.name
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-ssh-service.conf

%files gtk -f %name.lang
%_libdir/NetworkManager/libnm-ssh-properties.so*
%_libexecdir/NetworkManager/nm-ssh-auth-dialog
%_datadir/gnome-vpn-properties/*

%exclude %_libdir/NetworkManager/*.la

%changelog
* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.3-alt1
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.
- Updated to 0.9.3.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt4
- Temporary don't treat warrnings as errors.
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt3
- Fix build: Avoid deprecation warnings.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt2
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.

* Mon Jul 22 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated from upstream git (e5e66fd96141).
- Updated to 0.9.1.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20130405
- Initial build.

