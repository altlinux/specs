Name: qfsm
Version: 0.56
Release: alt1

Summary: Graphical tool for designing finite state machine
License: GPLv3
Group: Education

Url: https://github.com/AaronErhardt/qfsm
Source: %version.tar.gz
Patch: qfsm-0.56-examples.patch

# Automatically added by buildreq on Mon Jul 12 2021
# optimized out: cmake-modules fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libqt4-core libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base sh4
BuildRequires: cmake gcc-c++ libgraphviz-devel libqt4-devel

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
%setup
%patch -p1

%build
%cmake
%cmake_build
cd po
lupdate-qt4 ../src/ -ts *ts
lrelease-qt4 *ts

%install
%cmake_install
rm -rf %buildroot%_defaultdocdir/%name
ln -s %name-%version/user %buildroot%_defaultdocdir/%name
%find_lang %name

%files -f %name.lang
%doc *.md
%doc doc/user examples
%_bindir/%name
%_defaultdocdir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/*.desktop
%_datadir/mimelnk/application/*.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Fri Jul 02 2021 Fr. Br. George <george@altlinux.ru> 0.56-alt1
- Autobuild version bump to 0.56

* Wed Jun 19 2019 Fr. Br. George <george@altlinux.ru> 0.54.0-alt2
- Fix build

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.54.0-alt1
- Autobuild version bump to 0.54.0

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 0.53.0-alt1.1
- NMU: rebuilt without graphviz (cgraph support missing)

* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 0.53.0-alt1
- Autobuild version bump to 0.53.0

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
