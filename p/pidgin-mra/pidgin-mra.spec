Name: pidgin-mra
Version: 0.1.4.1
Release: alt1

Summary: Mail.ru Agent protocol plugin for Pidgin IM
License: GPLv2+
Group: Networking/Instant messaging
Url: http://github.com/dreadatour/pidgin-mra
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: http://github.com/dreadatour/pidgin-mra/downloads/%name-%version.tar.gz
Patch0: pidgin-mra-0.1.4.1-alt-add_zodiak.patch
Patch1: pidgin-mra-0.1.4.1-alt-makefile.patch

Requires: pidgin

# Automatically added by buildreq on Wed Jul 16 2010 (-bi)
BuildRequires: libpurple-devel

%description
This is Mail.ru Agent protocol plugin for Pidgin IM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
%make_install DESTDIR=%buildroot install
%ifarch x86_64
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/lib/purple-2/ %buildroot%_libdir/
%endif

%files
%doc README ChangeLog INSTALL TODO
%_libdir/purple-2/libmra.so
%_pixmapsdir/pidgin/protocols/*/mra.png

%changelog
* Mon Apr 18 2011 Mikhail Kolchin <mvk@altlinux.org> 0.1.4.1-alt1
- initial build for ALT Linux Sisyphus
