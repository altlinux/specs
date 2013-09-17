%define php5_extension cups
%define _cups_serverbin %_libexecdir/cups
Summary: OpenPrinting CUPS filters and backends
Name: cups-filters
Version: 1.0.38
Release: alt2

# For a breakdown of the licensing, see COPYING file
# GPLv2:   filters: commandto*, imagetoraster, pdftops, rasterto*,
#                   imagetopdf, pstopdf, texttopdf
#         backends: parallel, serial
# GPLv2+:  filters: textonly, texttops, imagetops
# GPLv3:   filters: bannertopdf
# MIT:     filters: pdftoijs, pdftoopvp, pdftopdf, pdftoraster
License: GPLv2 and GPLv2+ and GPLv3 and MIT

Group: System/Servers

Source: http://www.openprinting.org/download/cups-filters/cups-filters-%version.tar
Patch0: %name-alt.patch
Patch1: %name-alt-php-5.4.14-fix.patch
Url: http://www.linuxfoundation.org/collaborate/workgroups/openprinting/pdf_as_standard_print_job_format
Conflicts: cups < 1.6.1-alt1

BuildRequires: cups-devel
# pdftopdf
BuildRequires: libqpdf-devel
# pdftops
BuildRequires: poppler-utils
# pdftoijs, pdftoopvp, pdftoraster
BuildRequires: libpoppler-devel libpoppler-cpp-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libijs-devel
BuildRequires: glib2-devel
# libijs
BuildRequires: libgs-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig-devel
BuildRequires: liblcms2-devel
BuildRequires: php5-devel

# Make sure we get postscriptdriver tags.
BuildRequires: python-module-cups

Requires: poppler-utils

%package libs
Summary: OpenPrinting CUPS filters and backends - cupsfilters and fontembed libraries
Group: System/Libraries
# LGPLv2: libcupsfilters
# MIT:    libfontembed
License: LGPLv2 and MIT

%package devel
Summary: OpenPrinting CUPS filters and backends - development environment
Group: Development/C
License: LGPLv2 and MIT
Requires: cups-filters-libs = %version-%release

%description
Contains backends, filters, and other software that was
once part of the core CUPS distribution but is no longer maintained by
Apple Inc. In addition it contains additional filters developed
independently of Apple, especially filters for the PDF-centric printing
workflow introduced by OpenPrinting.

%description libs
This package provides cupsfilters and fontembed libraries.

%description devel
This is the development package for OpenPrinting CUPS filters and backends.

%package -n php5-cups
Epoch: 1
Summary: PHP5 module for the Common Unix Printing System
License: GPL
Group: System/Servers
Requires: php5 = %php5_version
BuildRequires(pre): rpm-build-php5

%description -n php5-cups
PHP5 module for the Common Unix Printing System

%package -n cups-backend-serial
Epoch: 1
Summary: serial backend for cups
License: GPL
Group: System/Servers

%description -n cups-backend-serial
serial backend for cups

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
# work-around Rpath
./autogen.sh

# --with-pdftops=pdftops - use Poppler instead of Ghostscript (see README)
%configure --disable-static \
           --disable-silent-rules \
	   --without-php \
           --with-pdftops=pdftops

%make
pushd scripting/php

phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension=%_usr
%php5_make
popd


%install
%make install DESTDIR=%buildroot
install -D -m 755 scripting/php/.libs/cups.so %buildroot/%php5_extdir/cups.so
install -D -m 644 scripting/php/php-cups.ini %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 scripting/php/php-cups-params.sh %buildroot/%php5_extconf/%php5_extension/params
mkdir -p %buildroot/%_unitdir/
install -m 644 utils/cups-browsed.service %buildroot/%_unitdir/

%post -n php5-cups
%php5_extension_postin

%preun -n php5-cups
%php5_extension_preun

%files
%doc README AUTHORS NEWS
%config(noreplace) %_sysconfdir/fonts/conf.d/99pdftoopvp.conf
%config(noreplace) %_sysconfdir/cups/cups-browsed.conf
%attr(0755,root,root) %_cups_serverbin/filter/*
%exclude %_cups_serverbin/filter/gstopxl
%exclude %_cups_serverbin/filter/gstoraster
%attr(0755,root,root) %_cups_serverbin/backend/parallel
%_datadir/cups/banners
%_datadir/cups/charsets
%_datadir/cups/data/*
%_datadir/cups/drv/cupsfilters.drv
%_datadir/cups/mime/cupsfilters.types
%_datadir/cups/mime/cupsfilters.convs
%_datadir/ppd/cupsfilters
/usr/bin/ttfread
/usr/sbin/cups-browsed
/usr/share/man/man*/*
%_unitdir/*

%files -n cups-backend-serial
%_prefix/lib/cups/backend/serial


%files -n php5-cups
%php5_extdir/cups.so
%php5_extconf/%php5_extension

%files libs
%doc COPYING fontembed/README
%attr(0755,root,root) %_libdir/libcupsfilters.so.*
%attr(0755,root,root) %_libdir/libfontembed.so.*

%files devel
%_includedir/cupsfilters
%_includedir/fontembed
%_libdir/pkgconfig/libcupsfilters.pc
%_libdir/pkgconfig/libfontembed.pc
%_libdir/libcupsfilters.so
%_libdir/libfontembed.so

%changelog
* Tue Sep 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.38-alt2
- conflict with ghostscript-cups resolved

* Mon Sep 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.38-alt1
- update to 1.0.38
- cups-browsed packaged

* Fri Jul 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt4.2
- Rebuild with php5-5.4.17.20130704

* Sat May 18 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.31-alt4.1
- Rebuild with php5-5.3.24.20130412-alt1

* Mon May 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt4
- rebuild with php5-5.3.25.20130512-alt1

* Tue Apr 23 2013 Anton Farygin <rider@altlinux.ru> 1.0.31-alt3
- rebuild with new poppler35

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt2
- rebuild with php5-5.3.24.20130412-alt1

* Wed Apr 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt1
- updated from upstream (closes: #28783)
- rebuild with php5-5.3.23.20130314-alt1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt3
- rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt2
- rebuild with php5-5.3.17.20120913-alt1

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt1
- first build for Sisyphus, based on RH spec
