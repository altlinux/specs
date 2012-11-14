%define php5_extension cups
%define _cups_serverbin %_libexecdir/cups
Summary: OpenPrinting CUPS filters and backends
Name: cups-filters
Version: 1.0.24
Release: alt3

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
Patch0: %name-%version-%release.patch
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
%patch0 -p1

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

%post -n php5-cups
%php5_extension_postin

%preun -n php5-cups
%php5_extension_preun

%files
%doc README AUTHORS NEWS
%config(noreplace) %_sysconfdir/fonts/conf.d/99pdftoopvp.conf
%attr(0755,root,root) %_cups_serverbin/filter/*
%attr(0755,root,root) %_cups_serverbin/backend/parallel
%_datadir/cups/banners
%_datadir/cups/charsets
%_datadir/cups/data/*
%_datadir/cups/drv/cupsfilters.drv
%_datadir/cups/mime/cupsfilters.types
%_datadir/cups/mime/cupsfilters.convs
%_datadir/ppd/cupsfilters

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
* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt3
- rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt2
- rebuild with php5-5.3.17.20120913-alt1

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt1
- first build for Sisyphus, based on RH spec
