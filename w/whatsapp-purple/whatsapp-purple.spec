Name: whatsapp-purple
Version: 0.3
Release: alt1

Summary: WhatsApp protocol implementation for libpurple (Pidgin)
License: GPLv2+
Group: Networking/Instant messaging
Url: https://github.com/davidgfnet/whatsapp-purple
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: http://github.com/davidgfnet/whatsapp-purple/releases/%name-%version.tar.gz

Requires: pidgin

# Automatically added by buildreq on Mon Jun 30 2014
# optimized out: glib2-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ libpurple-devel

%description
This is a WhatsApp plugin for Pidgin and libpurple messengers. It connects
to the WhatsApp servers using the password (which needs to be retrieved
separately). Only one client can connect at a time (including your phone).

%prep
%setup -q

%build
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_libdir/purple-2/libwhatsapp.so
%_pixmapsdir/pidgin/protocols/*/whatsapp.png

%changelog
* Mon Jun 30 2014 Mikhail Kolchin <mvk@altlinux.org> 0.3-alt1
- initial build for ALT Linux Sisyphus
