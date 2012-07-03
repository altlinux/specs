Name: libgmtk
Version: 1.0.6
Release: alt1

Summary: a set of gtk widgets to use with gnome-mplayer
License: GPLv2
Group: System/Libraries

Url: http://code.google.com/p/gmtk/
Source: %name-%version.tar

BuildRequires: intltool libgtk+3-devel libgio-devel libdconf-devel libalsa-devel libpulseaudio-devel

%description
%summary

%package devel
Summary: development files for gmtk library
Group: Development/C
Requires: %name = %version-%release
Requires: libgmlib-devel = %version-%release

%description devel
%summary

%package -n libgmlib
Summary: a set of functions that support non-graphical operations for gnome-mplayer
Group: System/Libraries

%description -n libgmlib
%summary

%package -n libgmlib-devel
Summary: development files for gmlib library
Group: Development/C
Requires: libgmlib = %version-%release

%description -n libgmlib-devel
%summary

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall_std
rm -r %buildroot%_datadir/doc/gmtk

%find_lang gmtk

%files -f gmtk.lang
%_libdir/%name.so.*
%doc COPYING ChangeLog AUTHORS

%files devel
%_libdir/%name.so
%_libdir/pkgconfig/gmtk.pc
%_includedir/gmtk/gmtk*

%files -n libgmlib
%_libdir/libgmlib.so.*

%files -n libgmlib-devel
%_libdir/libgmlib.so
%_libdir/pkgconfig/gmlib.pc
%dir %_includedir/gmtk
%_includedir/gmtk/gm_*
%_includedir/gmtk/gmlib.h

%changelog
* Thu Jun 14 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.6-alt1
- Initial build for Sisyphus

