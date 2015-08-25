Name: purple-plugin-skypeweb
Version: 0.1
Release: alt1

Summary: SkypeWeb Plugin for Pidgin
License: GPLv3
Group: Networking/Instant messaging
URL: https://github.com/EionRobb/skype4pidgin
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: skype4pidgin-master.tar.gz

# Automatically added by buildreq on Tue Aug 25 2015
# optimized out: glib2-devel libcloog-isl4 libgio-devel libjson-glib pkg-config
BuildRequires: libjson-glib-devel libpurple-devel zlib-devel

%description
SkypeWeb Plugin for Pidgin

%prep
%setup -n skype4pidgin-master

%build
cd skypeweb
%make_build

%install
cd skypeweb
%makeinstall_std

%files
%_libdir/purple-2/libskypeweb.so
%_pixmapsdir/pidgin/protocols/*/skype.png

%changelog
* Tue Aug 25 2015 Mikhail Kolchin <mvk@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus
