Name:		gtkperf
Summary:	GTK+ performance tester
Summary(ru_RU.UTF-8): Утилита для тестирования производительности модулей прорисовки GTK+
Version:	0.40
Release:	alt1.qa2
License:	GPLv2
Group:		System/X11
Source0:	%{name}-%{version}.tar.gz
Source1:        gtkperf.desktop
URL:		http://gtkperf.sourceforge.net/

Packager:       Denis Koryavov <dkoryavov@altlinux.org>
BuildRequires:  gcc-c++ gcc-fortran desktop-file-utils libgtk+2-devel

%description
GtkPerf is an application designed to test GTK+ performance. The point
is to create common testing platform to run predefined GTK+ widgets
and this way define the speed of device/platform.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе утилиту GtkPerf предназначенную для тестирования 
производительности модулей прорисовки GTK+. 

%prep
%setup -q

%build
%configure
# Do not run autoheader
touch ./stamp-h*

# A bug in configure.in makes CFLAGS to be overwritten with an empty string
# so set CFLAGS in make
make CFLAGS="%{optflags}"

# Changelog must be converted to utf8
rm -f ./ChangeLog.utf8
iconv -f ISO-8859-1 -t utf8 ./ChangeLog -o ChangeLog.utf8
mv -f ChangeLog.utf8 ./ChangeLog

%install
%makeinstall_std
desktop-file-install --vendor="altlinux"	\
	--dir=%{buildroot}%{_datadir}/applications\
	%{SOURCE1}
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--add-category=Development \
	--add-category=Profiling \
	%buildroot%_desktopdir/altlinux-gtkperf.desktop

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*

%changelog
* Sat May 21 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.40-alt1.qa2
- NMU: fix desktop permissions

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.40-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gtkperf
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Wed Jul 01 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.40-alt1
- First build for Sisyphus
