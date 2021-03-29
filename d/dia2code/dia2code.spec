Name: dia2code
Version: 0.8.8
Release: alt2
License: GPLv2+
Group: Development/Tools
Summary: This program generates code for many languages from an UML Dia Diagram
Url: http://dia2code.sourceforge.net
Source: %name-%version.tar.gz
Source1: examples-%version.tar.gz
Patch1: %name-%version-gcc-10.patch

# Automatically added by buildreq on Thu Sep 05 2013
BuildRequires: libxml2-devel

%description
This program is a small utility that makes code from a Dia diagram.
Supported languages are: Ada, C, C++, C#, IDL, Java, PHP(4,5), Python,
Ruby, shapefiles, and SQL create statement files.

Its intended purpose is to ease the programmer's work by generating
the structure of the classes in an Object Oriented language
(like C++, Java and C#) from a graphical representation of them
(a Dia Diagram).

%prep
%setup -a1
%patch1 -p2
sed -i 's@/usr/local/bin@%_bindir@' dia2code.kaptn

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
install -D %name.1 %buildroot%_man1dir/%name.1
install -D dia2code.kaptn %buildroot%_datadir/kaptain/dia2code.kaptn

%files
%doc README AUTHORS examples*/*
%_bindir/*
%_man1dir/*
%_datadir/kaptain/dia2code.kaptn

%changelog
* Mon Mar 29 2021 Slava Aseev <ptrnine@altlinux.org> 0.8.8-alt2
- Fix build with with gcc-10 (-fno-common)

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.8.8-alt1
- Autobuild version bump to 0.8.8

* Wed Jul 09 2014 Fr. Br. George <george@altlinux.ru> 0.8.7-alt1
- Autobuild version bump to 0.8.7
- Fix kaptain location

* Thu Sep 05 2013 Fr. Br. George <george@altlinux.ru> 0.8.5-alt1
- Autobuild version bump to 0.8.5
- Examples added
