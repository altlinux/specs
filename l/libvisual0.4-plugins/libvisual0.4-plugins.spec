%define _name libvisual
%def_disable static

Name: %{_name}0.4-plugins
Version: 0.4.0
Release: alt3

Summary: Libvisual library plugins
License: LGPL
Group: Sound
Url: http://%name.sourceforge.net
Source: %_name-plugins-%version.tar.bz2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%define libvisual_ver 0.4.0

Requires: %name-morph = %version-%release
Requires: %name-input = %version-%release
Requires: %name-actor = %version-%release

# Automatically added by buildreq on Mon May 29 2006
BuildRequires: gcc-c++ gstreamer-devel libXt-devel libXxf86vm-devel libalsa-devel
BuildRequires: libgtk+2-devel libpopt-devel libvisual0.4-devel
BuildRequires: libxml2-devel zlib-devel esound-devel jackit-devel

BuildPreReq: flex libGL-devel libGLU-devel

%description
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

This package contains various libvisual plugins.

%package -n %name-morph
Summary: %name morph plugins 
Group: Sound
PreReq: %{_name}0.4 = %libvisual_ver

%description -n %name-morph
This package contains various %_name plugins that morph between two or
more video sources using different metods.

%package -n %name-input
Summary: %_name plugins to capture PCM data from the different audio sources
Group: Sound
Requires: %name-input-alsa = %version-%release %name-input-mplayer = %version-%release

%description -n %name-input
This package contains various %_name plugins to capture PCM data from
the different audio sources.

%package -n %name-actor
Summary: %_name actor plugins
Group: Sound
PreReq: %{_name}0.4 = %libvisual_ver

%description -n %name-actor
This package contains various %_name actor plugins.

%package -n %name-input-alsa
Summary: The %_name ALSA capture plugin
Group: Sound
PreReq: %{_name}0.4 = %libvisual_ver

%description -n %name-input-alsa
This package contains %_name input plugin to capture PCM data from the
ALSA record device.

%package -n %name-input-mplayer
Summary: The %_name input plugin for use data exported from MPlayer
Group: Sound
PreReq: %{_name}0.4 = %libvisual_ver

%description -n %name-input-mplayer
This package contains %_name input plugin that uses data exported from
'mplayer -af export'.

%prep
%setup -n %_name-plugins-%version

subst 's,0\.8,0.10,g' configure

%build
%configure \
    %{subst_enable static}

%make_build

%install
%makeinstall_std

find %buildroot%_libdir/%_name-0.4 -depth -name \*.la -exec rm -f {} \;

rm -f %buildroot%_libdir/%_name-0.4/actor/actor_gstreamer.so

%files
%doc AUTHORS ChangeLog NEWS README TODO

%files -n %name-actor
%_libdir/%_name-0.4/actor/*.so
%_datadir/%_name-plugins-0.4

%files -n %name-morph
%_libdir/%_name-0.4/morph/*.so

%files -n %name-input

%files -n %name-input-alsa
%_libdir/%_name-0.4/input/input_alsa.so

%files -n %name-input-mplayer
%_libdir/%_name-0.4/input/input_mplayer.so

%changelog
* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Rebuilt for debuginfo
- BuildRequires: added flex and replaced libmesa-devel by libGL-devel
  and libGLU-devel
- Disabled actor_gstreamer.so (bad_elf_symbols detected)

* Sat Dec 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt2
- updated build dependencies
- fixed build for gstreamer-0.10

* Mon May 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Nov 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.7-alt1
- First build for Sisyphus. 
