Name: purple-plugin-skypeweb
Version: 1.1
Release: alt1

Summary: SkypeWeb Plugin for Pidgin
License: GPLv3
Group: Networking/Instant messaging
URL: https://github.com/EionRobb/skype4pidgin
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: skype4pidgin-%version.tar.gz

# Automatically added by buildreq on Tue Aug 25 2015
# optimized out: glib2-devel libcloog-isl4 libgio-devel libjson-glib pkg-config
BuildRequires: libjson-glib-devel libpurple-devel zlib-devel

%description
SkypeWeb Plugin for Pidgin

%prep
%setup -n skype4pidgin-%version/skypeweb

%build
%make_build

%install
%makeinstall_std

%files
%_libdir/purple-2/libskypeweb.so
%_pixmapsdir/pidgin/protocols/*/skype.png

%changelog
* Fri Jan 08 2016 Mikhail Kolchin <mvk@altlinux.org> 1.1-alt1
- new version

* Tue Nov 10 2015 Mikhail Kolchin <mvk@altlinux.org> 1.0-alt1
- new version

* Tue Aug 25 2015 Mikhail Kolchin <mvk@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus
