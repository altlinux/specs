Name: eaglemode
Version: 0.83.0
Release: alt1
Group: Graphical desktop/Other
Summary: Futuristic desktop allowing user to visit almost everything by zooming in
Packager: Fr. Br. George <george@altlinux.ru>
License: GPL
Source: %name-%version.tar.bz2
Source1: %name-install.sed
Source2: %name.wrapper
Url: http://eaglemode.sourceforge.net/index.html

Requires: arj p7zip lzop lha zip unzip unrar htmldoc

%set_perl_req_method relaxed
#set_verify_elf_method unresolved=relaxed

BuildRequires:	libpoppler-glib-devel

# Automatically added by buildreq on Thu Jun 24 2010
BuildRequires: gcc-c++ libgio-devel libgtk+2-common-devel libjpeg-devel librsvg-devel libtiff-devel libxine-devel perl-threads libpng-devel

%description
Eagle Mode is an advanced solution for a futuristic style of man-machine communication, in which the user can visit almost everything simply by zooming in. It has a professional file manager, file viewers and players for most of the common file types, a chess game, a 3D mines game, a multi-function clock and some fractal fun, all integrated in a virtual cosmos. By featuring a separate popup-zoomed control view, help texts in the things they are describing, editable bookmarks, multiple input methods, fast anti-aliased graphics, a virtually unlimited depth of panel tree, and by its portable C++ API, Eagle Mode aims to be a cutting edge of zoomable user interfaces.

%package devel
Group: Graphical desktop/Other
Summary: Header files for eaglemode desktop

%description devel
Header files for Eagle Mode desktop API

%prep
%setup

%build
echo "## $((%__nprocs+1))"
perl make.pl build cpus=$((%__nprocs+1)) continue=no

%install
perl make.pl install root=%buildroot dir=%_libdir/%name menu=yes bin=yes
mv %buildroot%_libdir/%name/lib/libemCore.so %buildroot%_libdir/libemCore.so
ln -s ../../libemCore.so %buildroot%_libdir/%name/lib
mv %buildroot%_libdir/%name/lib/libemFileMan.so %buildroot%_libdir/libemFileMan.so
ln -s ../../libemFileMan.so %buildroot%_libdir/%name/lib
mkdir -p %buildroot%_sysconfdir %buildroot%_datadir/%name %buildroot%_includedir
mv %buildroot%_libdir/%name/etc %buildroot%_sysconfdir/%name && ln -s %_sysconfdir/%name %buildroot%_libdir/%name/etc
mv %buildroot%_libdir/%name/res %buildroot%_datadir/%name/res && ln -s %_datadir/%name/res %buildroot%_libdir/%name/res
mv %buildroot%_libdir/%name/doc %buildroot%_datadir/%name/doc && ln -s %_datadir/%name/doc %buildroot%_libdir/%name/doc
mv %buildroot%_libdir/%name/include %buildroot%_includedir/%name && ln -s %_includedir/%name %buildroot%_libdir/%name/include

%files
%doc README src/*/*.README
%_bindir/*
%_sysconfdir/%name
%_datadir/%name
%_libdir/%name
%_libdir/lib*.so*
%_desktopdir/*
%dir %_includedir/%name

%files devel
%_includedir/%name/*

%changelog
* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 0.83.0-alt1
- Autobuild version bump to 0.83.0
- Buildreq fix

* Mon Jun 27 2011 Fr. Br. George <george@altlinux.ru> 0.82.0-alt1
- Autobuild version bump to 0.82.0

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 0.81.0-alt1
- Autobuild version bump to 0.81.0

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 0.80.0-alt1
- Autobuild version bump to 0.80.0

* Fri Jun 25 2010 Fr. Br. George <george@altlinux.ru> 0.78.0-alt1
- Version up

* Wed May 05 2010 Fr. Br. George <george@altlinux.ru> 0.77.0-alt1
- Version up

* Sun Sep 06 2009 Fr. Br. George <george@altlinux.ru> 0.75.1-alt1
- Version up

* Mon Nov 03 2008 Fr. Br. George <george@altlinux.ru> 0.72.0-alt1
- Version up

* Tue Jul 15 2008 Fr. Br. George <george@altlinux.ru> 0.71.0-alt1
- Version up

* Wed May 14 2008 Fr. Br. George <george@altlinux.ru> 0.70.0-alt1
- Initial try
- FHS scatter and $HOME installer invented

