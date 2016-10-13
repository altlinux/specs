Name: libxmp
Version: 4.4.1
Release: alt1

Summary: Module Player library for MOD, S3M, IT and others
License: LGPLv2.1
Group: System/Libraries

Url: http://xmp.sf.net/
Source0: http://downloads.sf.net/xmp/%name-%version.tar.gz
Source100: %name.watch

%description
libxmp is a module player library which supports many module formats,
including MOD, S3M and IT. Possible applications for libxmp include
standalone module players, module player plugins for other players,
module information extractors, background music replayers for games
and other applications, converters, etc.

%package devel
Summary: Development files for libxmp, a MOD/S3M/IT/etc. module player library
Group: Development/C
Requires: %name = %version

%description devel
libxmp is a module player library which supports many module formats,
including MOD, S3M and IT. Possible applications for libxmp include
standalone module players, module player plugins for other players,
module information extractors, background music replayers for games
and other applications, converters, etc.

This subpackage contains headers and library development files for
libxmp.

%prep
%setup

%build
%configure
%make_build

%install
b="%buildroot"
make install DESTDIR="$b"
mkdir -p "$b/%_mandir/man3" "$b/%_docdir/%name"
install -pm0644 docs/Changelog docs/[a-z]* "$b/%_docdir/%name/"
# Remove file due to bnc#808655, and because they are hardware-specific
# and should not have much relevance for developers anyhow.
rm -f "$b/%_docdir/%name"/{adlib*,ay*.txt}
mv "$b/%_docdir/%name/libxmp.3" "$b/%_man3dir/"

%files -n %name
%_libdir/libxmp.so.4*
%doc docs/COPYING.LIB

%files devel
%_includedir/xmp.h
%_libdir/libxmp.so
%_libdir/pkgconfig/libxmp.pc
%_mandir/man3/libxmp.3*
%_docdir/%name/

%changelog
* Thu Oct 13 2016 Michael Shigorin <mike@altlinux.org> 4.4.1-alt1
- new version (watch file uupdate)

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 4.4.0-alt1
- new version (watch file uupdate)

* Fri Apr 22 2016 Michael Shigorin <mike@altlinux.org> 4.3.13-alt1
- new version (watch file uupdate)

* Mon Mar 07 2016 Michael Shigorin <mike@altlinux.org> 4.3.12-alt1
- added watch file
- new version (watch file uupdate)
  + includes fixes for problems found by Coverity Scan and OpenMPT tests

* Thu Jun 11 2015 Motsyo Gennadi <drool@altlinux.ru> 4.3.8-alt1
-initial build for ALT Linux from OpenSUSE
