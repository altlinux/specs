%define ver_major 0.4
%define xdg_name org.pantheon.terminal

Name: pantheon-terminal
Version: %ver_major.3
Release: alt2

Summary: Pantheon Terminal
Group: Terminals
License: GPLv3
Url: https://github.com/elementary/terminal

Source: %url/archive/%version/terminal-%version.tar.gz

BuildRequires: cmake gcc-c++ intltool libappstream-glib-devel libnotify-devel
BuildRequires: libvte3-devel libgranite-devel libpixman-devel
BuildRequires: libXdmcp-devel vala libgranite-vala

%description
Pantheon Terminal (referred to simply as "Terminal" when installed) is a super
lightweight, beautiful, and simple terminal.

It's designed to be setup with sane defaults and little to no configuration.
It's just a terminal, nothing more, nothing less.

%package vala
Summary: Vala language bindings for the %name
Group: Development/Other
BuildArch: noarch
#Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the %name.


%prep
%setup -n terminal-%version

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DGSETTINGS_COMPILE:BOOL=OFF \
	-DGSETTINGS_LOCALINSTALL:BOOL=OFF
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS README*
%_bindir/*
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_desktopdir/open-%name-here.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%name.appdata.xml

%if 0
%files vala
%_vapidir/*
%endif

%changelog
* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt2
- rebuilt against libgranite.so.4

* Mon Jul 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu May 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Sat Mar 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.4-alt1
- 0.4.0.4

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.3-alt1
- 0.4.0.3

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1.3-alt1
- 0.3.1.3

* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4.1-alt1
- 0.2.3 -> 0.2.4.1

* Mon Aug 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

