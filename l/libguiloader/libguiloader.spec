# ldconfig!
%define oname guiloader
Name: lib%oname
Version: 2.7.1
Release: alt0.1

Summary: A high-performance and compact GuiXml loader library

Url: http://gideon.sourceforge.net/
License: GPL
Group: Development/Other

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/gideon/%oname-%version.tar.bz2

# Automatically added by buildreq on Sun Jul 30 2006
BuildRequires: fontconfig gcc-c++ libgtk+2-devel

%description
GuiLoader is a high-performance and compact GuiXml loader library. This
library allows GTK+ applications to create GUI widgets and objects at
run-time from GuiXml resource files. GuiLoader is written in C language as
a GObject subclass and has a trivial language-independent API. GuiLoader
was designed to be easily wrapped for any language that has GTK+ bindings.

%package devel
Summary: The files needed for %oname application development
Summary(ru_RU.KOI8-R): Файлы, требующиеся для разработки приложений с использованием %oname
Group: Development/C
Requires: %name = %version-%release

%description devel
The %oname-devel package contains the necessary include files
for developing applications with %oname

%description devel -l ru_RU.KOI8-R
Пакет %oname-devel содержит необходимые заголовочные файлы
для разработки приложений, которые используют %oname.

%prep
%setup -q -n %oname-%version

%build
%configure
%make

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS README NEWS 
%_libdir/*.so

%files devel
%doc examples/
%_includedir/%oname/
%_pkgconfigdir/*

%changelog
* Sun Jul 30 2006 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt0.1
- initial build for ALT Linux Sisyphus
