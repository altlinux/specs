Name: pidgin-mra
Version: 0.1.4.2
Release: alt2

Summary: Mail.ru Agent protocol plugin for Pidgin IM
License: GPLv2+
Group: Networking/Instant messaging

Url: http://github.com/dreadatour/pidgin-mra
Source: http://github.com/dreadatour/pidgin-mra/downloads/%name-%version.tar.gz
Packager: Mikhail Kolchin <mvk@altlinux.org>

Requires: pidgin

# Automatically added by buildreq on Wed Jul 16 2010 (-bi)
BuildRequires: libpurple-devel

%description
This is Mail.ru Agent protocol plugin for Pidgin IM.

%prep
%setup

%build
%make_build

%install
%makeinstall_std
%if "%_lib" == "lib64"
mkdir -p %buildroot%_libdir
mv %buildroot/usr/lib/purple-2 %buildroot%_libdir/
%endif

%files
%doc README ChangeLog INSTALL TODO
%_libdir/purple-2/libmra.so
%_pixmapsdir/pidgin/protocols/*/mra.png

%changelog
* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 0.1.4.2-alt2
- fixed build on non-x86 64-bit arches
- minor spec cleanup

* Mon Oct 14 2013 Mikhail Kolchin <mvk@altlinux.org> 0.1.4.2-alt1
- New version

* Mon Apr 18 2011 Mikhail Kolchin <mvk@altlinux.org> 0.1.4.1-alt1
- initial build for ALT Linux Sisyphus
