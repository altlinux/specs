
Name: totem-plugins-mediaserver2
Version: 0.0.1
Release: alt1
Summary: A plugin to let you browse media content using the MediaServer2 D-BUS specification.
Group: Sound
License: LGPLv2+
Url: http://live.gnome.org/Grilo
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar

BuildRequires: gnome-common
BuildRequires: libgrilo-mediaserver2-devel
BuildRequires: libpeas-devel
BuildRequires: libtotem-devel >= 3.0.0


%description
A plugin to let you browse media content using the MediaServer2 D-BUS specification for Totem.

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING NEWS README
%_libdir/totem/plugins/mediaserver2

%changelog
* Mon May 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
