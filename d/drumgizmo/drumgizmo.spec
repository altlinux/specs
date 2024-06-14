Name: drumgizmo
Version: 0.9.20
Release: alt1

Summary: Multichannel drum plugin 
License: LGPLv3
Group: Sound
Url: https://www.drumgizmo.org/

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(alsa)

%package -n lv2-drumgizmo-plugin
Summary: Surge XT synthesizer as LV2 plugin
Group: Sound

%define desc\
DrumGizmo is an open source, multichannel, multilayered, cross-platform drum\
plugin and stand-alone application. It enables you to compose drums in midi and\
mix them with a multichannel approach. It is comparable to that of mixing a\
real drumkit that has been recorded with a multimic setup.

%description %desc

%description -n lv2-drumgizmo-plugin %desc
This package contains LV2 version of DrumGizmo.

%prep
%setup
tar ixf %SOURCE1
sed -i '/^#include <cstdlib>/ a#include <cstdint>' \
	plugin/plugingizmo/plugin.h

%build
%autoreconf
%configure --enable-lv2 --disable-editor --disable-cli
%make_build

%install
%makeinstall_std

%global _customdocdir %_defaultdocdir/drumgizmo

%files -n lv2-drumgizmo-plugin
%_libdir/lv2/*

%changelog
* Fri Jun 14 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.20-alt1
- initial

