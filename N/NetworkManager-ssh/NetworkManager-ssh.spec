%define nm_version 0.9.8.0
%define nm_applet_version 0.9.8.0
#define git_date %nil
%define git_date .git20130405
%define gtkver 3

Name: NetworkManager-ssh
Version: 0.0.3
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for SSH
Url: https://github.com/danfruehauf/NetworkManager-ssh
# git:git://github.com/danfruehauf/NetworkManager-ssh.git
Source0: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgnome-keyring-devel perl-XML-Parser
BuildRequires: intltool
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel

Requires: NetworkManager   >= %nm_version
Requires: openssh

%description
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager.

%package gnome
License: %gpl2plus
Summary: GNOME applications for %name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: gnome-keyring
Requires: NetworkManager-gnome >= %nm_applet_version
Requires: %name = %version-%release

%description gnome
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup
#patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--with-gtkver=%gtkver \
	--enable-more-warnings=error
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%post
if /sbin/service messagebus status &>/dev/null; then
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
else
echo "WARNING: %name requires running messagebus service." >&2
fi

%files
%doc AUTHORS README README.md
%_libexecdir/NetworkManager/nm-ssh-service
%dir %_sysconfdir/NetworkManager/VPN
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-ssh-service.name
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-ssh-service.conf

%files gnome -f %name.lang
%_libdir/NetworkManager/libnm-ssh-properties.so*
%_libexecdir/NetworkManager/nm-ssh-auth-dialog
%_datadir/gnome-vpn-properties/*

%exclude %_libdir/NetworkManager/*.la

%changelog
* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20130405
- Initial build.

