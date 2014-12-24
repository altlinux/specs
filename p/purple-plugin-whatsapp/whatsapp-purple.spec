%define origname whatsapp-purple

Name: purple-plugin-whatsapp
Version: 0.6
Release: alt1

Summary: WhatsApp protocol implementation for libpurple (Pidgin)
License: GPLv2+
Group: Networking/Instant messaging
URL: https://github.com/davidgfnet/whatsapp-purple
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %origname-%version.tar.gz

# Automatically added by buildreq on Mon Jun 30 2014
# optimized out: glib2-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ libpurple-devel

%description
This is a WhatsApp plugin for Pidgin and libpurple messengers. It connects
to the WhatsApp servers using the password (which needs to be retrieved
separately). Only one client can connect at a time (including your phone).

%prep
%setup -n %origname-%version

%build
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_libdir/purple-2/libwhatsapp.so
%_pixmapsdir/pidgin/protocols/*/whatsapp.png

%changelog
* Wed Dec 24 2014 Mikhail Kolchin <mvk@altlinux.org> 0.6-alt1
- new version

* Mon Sep 22 2014 Mikhail Kolchin <mvk@altlinux.org> 0.5-alt2
- package renamed to purple-plugin-whatsapp

* Sat Jul 12 2014 Mikhail Kolchin <mvk@altlinux.org> 0.5-alt1
- new version

* Mon Jun 30 2014 Mikhail Kolchin <mvk@altlinux.org> 0.3-alt1
- initial build for ALT Linux Sisyphus
