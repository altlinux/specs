Name:		opencpn
Version:	4.4.0
Release:	alt1
Summary:	A free and open source software for marine navigation

Group:		Other
License:	%gpl2only
URL:		http://opencpn.org
Source0:	OpenCPN-%{version}.tar.gz
Source1:	%name.desktop

Requires: %name-data

#Errara
#Patch100:

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Mon Mar 25 2013
# optimized out: cmake-modules fontconfig fontconfig-devel glib2-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
BuildRequires: bzlib-devel cmake gcc-c++ libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgtk+2-devel libwxGTK-devel libxkbfile-devel zlib-devel

BuildRequires: tinyxml-devel libgps-devel libportaudio2-devel libcurl-devel libexpat-devel

%description
OpenCPN is a free software (GPLv2) project to create a concise chart plotter
and navigation software, for use underway or as a planning tool. OpenCPN is
developed by a team of active sailors using real world conditions for program
testing and refinement.

%package data
Summary: Architecture independent files for OpenCPN.
Group: Other
BuildArch: noarch

%description data
Architecture independent files for OpenCPN.

%prep
%setup -q -n OpenCPN-%{version}

#patch100 -p1

#rm -f src/tinyxml*.cpp include/tinyxml.h
#rm -rf plugins/grib_pi/src/zlib-1.2.3
#rm -rf plugins/grib_pi/src/bzip2

%build
%cmake -DBUNDLE_DOCS=1 -DBUNDLE_TCDATA=1 -DBUNDLE_GSHHS=1
cd BUILD
make

%install
cd BUILD
make install DESTDIR=%{buildroot}
cp -f %{SOURCE1} %{buildroot}%{_datadir}/applications

# It is copied from %%_builddir by %%doc macro, so removed from %%buildroot
rm -rf %{buildroot}/%{_datadir}/doc
rm -rf %{buildroot}/%{_datadir}/%{name}/doc
rm -f  %{buildroot}/%{_datadir}/%{name}/license.txt

%find_lang %{name}
%find_lang --append --output=%{name}.lang %{name}-dashboard_pi
%find_lang --append --output=%{name}.lang %{name}-grib_pi
%find_lang --append --output=%{name}.lang %{name}-wmm_pi
%find_lang --append --output=%{name}.lang %{name}-chartdldr_pi

%files
%dir %{_libdir}/%{name}

%{_bindir}/opencpn
%{_libdir}/opencpn/*_pi.so

%files data -f BUILD/%{name}.lang
%doc data/doc/*
%doc data/license.txt

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/sounds
#dir %{_datadir}/%{name}/gshhs
#dir %{_datadir}/%{name}/tcdata
%dir %{_datadir}/%{name}/s57data
%dir %{_datadir}/%{name}/uidata
%dir %{_datadir}/%{name}/plugins

%{_datadir}/%{name}/sounds/*
#{_datadir}/%{name}/gshhs/*
#{_datadir}/%{name}/tcdata/*
%{_datadir}/%{name}/s57data/*
%{_datadir}/%{name}/uidata/*
%{_datadir}/%{name}/plugins/*

%{_iconsdir}/hicolor/48x48/apps/*
%{_iconsdir}/hicolor/scalable/apps/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Dec 01 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.4.0-alt1
- New version

* Sun Feb 16 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.2.2-alt1
- New version
- Moved architecture-independent data to noarch subpackage %name-data

* Wed Apr 03 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.0-alt1
- Initial build for ALT Linux

* Sun Sep 22 2012 Eric 'Sparks' Christensen <sparks@fedoraproject.org> - 3.0.2-1
- Initial package.
