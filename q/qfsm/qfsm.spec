
Summary: Graphical tool for designing finite state machine
Name:    qfsm	
Version: 0.52.0
Release: alt2
Group:   Education

License: GPL
Url:     http://qfsm.sourceforge.net/
Source:  http://prdownloads.sourceforge.net/%name/%name-%version-Source.tar.gz
Patch:	 %name.desktop.patch

# Automatically added by buildreq on Mon Mar 30 2009
BuildRequires: cmake gcc-c++ libSM-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libqt4-devel

%description
Qfsm is a graphical tool for designing finite state machine.
It is written in C++ using the Qt library.
Features include:

- Drawing, Editing and Printing of states diagrams
- Binary, ASCII or "free text" condition codes
- Multiple windows
- Integrity check
- Interactive simulation
- HDL export in the file formats: AHDL, VHDL, Verilog HDL, KISS
- Diagram export in the formats: EPS and SVG
- State table export in Latex, HTML or plain text format
- Ragel file export (used for C/C++, Java or Ruby code generation)

%prep
%setup -n %name-%version-Source
%patch -p0

%build
cmake .
%make_build

%install
%makeinstall DESTDIR=%buildroot
#mkdir -p %buildroot/usr/
#make package
#cp -rp _CPack_Packages/Linux/TGZ/qfsm-0.51.0-Linux/* %buildroot/usr/
rm -rf %buildroot%_defaultdocdir/%name
ln -s %name-%version/user %buildroot%_defaultdocdir/%name
%find_lang %name

%files -f %name.lang
%doc README TODO
%doc doc/user doc/html examples
%_bindir/%name
%_defaultdocdir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/*.desktop
%_datadir/mimelnk/application/*.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 0.52.0-alt2
- Fix repocop warnings

* Wed Apr 28 2010 Fr. Br. George <george@altlinux.ru> 0.52.0-alt1
- Version up
- Desktop file fixes
- Use find_lang for .po files

* Mon Mar 30 2009 Fr. Br. George <george@altlinux.ru> 0.51.0-alt1
- Version up

* Mon Oct 15 2007 Fr. Br. George <george@altlinux.ru> 0.45-alt1
- Initial build for ALT
