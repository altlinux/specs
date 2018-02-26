Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define Name TclTutor
Name: tcltutor
Version: 3.0
Release: alt0.1.1
Summary: Teach the Tcl programming language in a quick and easy manner
License: %bsdstyle
Group: Education
URL: http://www.msen.com/~clif/%Name.html
Requires: tk >= 8.4
BuildArch: noarch
Source0: http://www.msen.com/~clif/%{name}3_0b2.tar
Source1: %Name-16.png
Source2: %Name-32.png
Source3: %Name-48.png
Patch0: %name-3.0beta2-shebang.patch
Patch1: %name-3.0beta2-paths.patch
Provides: %Name = %version-%release
Obsoletes: %Name < %version-%release

BuildRequires: rpm-build-licenses

%description
This is a package designed to teach the Tcl programming language in a
quick and easy manner. The goal is to teach the minimal amount of Tcl
syntax, commands and options that are necessary to write useful
programs.
You are encouraged to use the man pages and books to augment this
tutorial.
This version covers all of the commands in the Tcl language, as of
version 7.4, and most of the commands added in later Tcl revisions.


%prep
%setup -n %Name
%patch0 -p1
%patch1 -p1


%build


%install
install -d -m 0755 %buildroot{%_datadir/%Name/lessons,%_bindir,%_niconsdir,%_miconsdir,%_liconsdir}
install -m 0755 %Name.tcl %buildroot/%_bindir/
ln -s %Name.tcl %buildroot/%_bindir/%name
cp -Tr lesson %buildroot%_datadir/%Name/lessons
rm -rf %buildroot%_datadir/%Name/Tcl_*/CVS
install -m 0644 [a-z]*.tcl %buildroot/%_datadir/%Name/
install -m 0644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 0644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -m 0644 %SOURCE3 %buildroot%_liconsdir/%name.png

# menu
install -d -m 0755 %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Version=1.0
Name=%Name
Exec=%Name.tcl
Comment=Teach the Tcl programming language
Comment[uk]=Навчання мови програмування Tcl
X-MultipleArgs=true
Icon=%name
Terminal=false
Type=Application
StartupNotify=false
Categories=Education;ComputerScience;
__MENU__


%files
%doc NOTICE README
%dir %_datadir/%Name
%_datadir/%Name/*.tcl
%dir %_datadir/%Name/lessons
%_datadir/%Name/lessons/Tcl_English
%lang(pt) %_datadir/%Name/lessons/Tcl_Portuguese
%_bindir/*
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*
%_desktopdir/*


%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for tcltutor

* Fri Aug 08 2008 Led <led@altlinux.ru> 3.0-alt0.1
- 3.0 Beta 2
- fixed %name.desktop

* Mon Jul 24 2006 Led <led@altlinux.ru> 2.0-alt0.2
- fixed URL

* Tue Jun 06 2006 Led <led@altlinux.ru> 2.0-alt0.1
- initial build
- added %name-2.0beta4-paths.patch
