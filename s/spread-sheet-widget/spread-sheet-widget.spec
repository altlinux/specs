Summary: Library for Gtk+ which provides a widget for viewing and manipulating 2 dimensional tabular data
Name: spread-sheet-widget
Version: 0.8
Release: alt1
License: GPLv3+
Group: System/Libraries
Source0: http://alpha.gnu.org/gnu/ssw/%name-%version.tar.gz
Patch0: %name-am.patch
Url: https://www.gnu.org/software/ssw/

BuildRequires: libgtk+3-devel makeinfo

%description
Demo binaries for lib%name, %summary

%package -n lib%name
Summary: Library for Gtk+ which provides a widget for viewing and manipulating 2 dimensional tabular data
Group: System/Libraries

%description -n lib%name
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget
for viewing and manipulating 2 dimensional tabular data in a manner
similar to many popular spread sheet programs.

The design follows the model-view-controller paradigm and is of
complexity O(1) in both time and space. This means that it is
efficient and fast even for very large data.

Features commonly found in graphical user interfaces such as cut and
paste, drag and drop and row/column labelling are also included.

%package -n lib%name-devel
Summary: Header files for %name library
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n lib%name-devel
Header files for %name library.

%prep
%setup -n %name-%version
%patch0 -p1

%build
%autoreconf
%configure --disable-static
%make_build
make doc/spread-sheet-widget.info

%install
%makeinstall
install -D doc/.libs/prog2 %buildroot%_bindir/%name-prog2
install -D doc/.libs/prog1 %buildroot%_bindir/%name-prog1
install -D demo/.libs/demo %buildroot%_bindir/%name-demo

%files
%_bindir/*

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/ssw*.h
%_pkgconfigdir/*.pc
%_infodir/*.info*

%changelog
* Wed Apr 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.8-alt1
- Updated to version 0.8

* Thu Aug 27 2020 Fr. Br. George <george@altlinux.ru> 0.6-alt1
- Autobuild version bump to 0.6

* Wed Feb 06 2019 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build from PLD

* Fri Nov 09 2018 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/spread-sheet-widget.git;a=log;h=master

* Fri Nov 09 2018 Adam Gołębiowski <adamg@pld-linux.org> 0b13181
- new

