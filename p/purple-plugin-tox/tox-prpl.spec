%define origname tox-prpl

Name: purple-plugin-tox
Version: 0.4.1
Release: alt1

Summary: Tox Protocol Plugin For Pidgin / libpurple
License: GPLv3+
Group: Networking/Instant messaging
URL: https://github.com/jin-eld/tox-prpl
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %origname-%version.tar.gz

Requires: libtoxcore0

# Automatically added by buildreq on Fri Aug 08 2014
# optimized out: glib2-devel libsodium-devel pkg-config
BuildRequires: libpurple-devel toxcore-devel

%description
Tox Protocol Plugin For Pidgin / libpurple.

%prep
%setup -n %origname-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README.md
%_libdir/purple-2/libtox.so
%_pixmapsdir/pidgin/protocols/*/tox.png

%changelog
* Fri Aug 08 2014 Mikhail Kolchin <mvk@altlinux.org> 0.4.1-alt1
- initial build for ALT Linux Sisyphus
