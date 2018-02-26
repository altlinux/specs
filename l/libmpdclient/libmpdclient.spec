# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libmpdclient
Version: 2.5
Release: alt1.1

Summary: MPD client library
License: BSD-like
Group: System/Libraries
Url: http://mpd.wikia.com/wiki/ClientLib:libmpdclient
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://dl.sourceforge.net/musicpd/%name-%version.tar.gz

%description
Library for Music Player Daemon client development.

%package devel
Summary: Header files for the MPD client library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for MPD client library.

%prep
%setup

%build
%configure --disable-werror
%make_build --silent --no-print-directory

%check
%make_build --silent --no-print-directory check

%install
%makeinstall_std --silent --no-print-directory

%files
%doc README COPYING AUTHORS NEWS
%_libdir/%name.so.*.*.*
%ghost %_libdir/%name.so.?
%exclude %_datadir/doc/%name/
%exclude %_libdir/%name.a

%files devel
%_libdir/%name.so
%_includedir/mpd/
%_pkgconfigdir/%name.pc

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Fixed build

* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 2.5-alt1
- Updated to 2.5

* Sat Jan 15 2011 Slava Semushin <php-coder@altlinux.ru> 2.4-alt1
- Updated to 2.4

* Sat Oct 30 2010 Slava Semushin <php-coder@altlinux.ru> 2.3-alt1
- Updated to 2.3
- Enable -Werror compiler flag
- Run make check

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 2.1-alt1
- Initial build for ALT Linux Sisyphus (based on spec from PLD Linux)

* Sun Jan 17 2010 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: libmpdclient.spec,v $
Revision 1.2  2009/10/06 18:54:12  wiget
- rel 1

Revision 1.1  2009/10/06 18:47:31  wiget
- initial, based on libmpd.spec

