Name: purple-plugin-skypeweb
Version: 1.7
Release: alt1

Summary: SkypeWeb Plugin for Pidgin
License: GPLv3
Group: Networking/Instant messaging
URL: https://github.com/EionRobb/skype4pidgin

Source: skype4pidgin.tar

# Automatically added by buildreq on Tue Aug 25 2015
# optimized out: glib2-devel libcloog-isl4 libgio-devel libjson-glib pkg-config
BuildRequires: libjson-glib-devel libpurple-devel zlib-devel

%description
SkypeWeb Plugin for Pidgin

%prep
%setup -n skype4pidgin

%build
%make_build -C skypeweb

%install
%makeinstall_std -C skypeweb

%files
%_libdir/purple-2/libskypeweb.so
%_pixmapsdir/pidgin/protocols/*/skype*.png
/usr/share/pixmaps/pidgin/emotes/skype*

%changelog
* Wed Aug 26 2020 Ildar Mulyukov <ildar@altlinux.ru> 1.7-alt1
- new version

* Wed Oct 19 2016 Eugene Prokopiev <enp@altlinux.ru> 1.2.2-alt1
- new version

* Fri Jan 08 2016 Mikhail Kolchin <mvk@altlinux.org> 1.1-alt1
- new version

* Tue Nov 10 2015 Mikhail Kolchin <mvk@altlinux.org> 1.0-alt1
- new version

* Tue Aug 25 2015 Mikhail Kolchin <mvk@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus
