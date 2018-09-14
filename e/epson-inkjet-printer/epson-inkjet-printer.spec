%set_verify_elf_method relaxed

Name:     epson-inkjet-printer
Version:  1.0.0
Release:  alt1.gitb36bfa8

Summary:  Collection of Epson ESC/P CUPS raster drivers for Linux
License:  LGPL
Group:    System/Configuration/Printing
Url:      https://github.com/endlessm/epson-inkjet-printer

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

ExclusiveArch: %ix86 x86_64

Provides:  printer-driver-escp = %EVR
Obsoletes: printer-driver-escp < %EVR

BuildRequires: gcc-c++
BuildRequires: libcups-devel
BuildRequires: libjpeg-devel

Requires: epson-inkjet-printer-filter
Requires: epson-inkjet-printer-l100l200
Requires: epson-inkjet-printer-201207w
Requires: epson-inkjet-printer-201215w
Requires: epson-inkjet-printer-201310w
Requires: epson-inkjet-printer-201401w
Requires: epson-inkjet-printer-201601w

%description
Printer driver for Epson Inkjet that use ESC/P This metapackage will
install the CUPS filter ESC/P driver and every related driver for
specific printers depending on it.

%package filter
Summary: CUPS filter - Epson Inkjet Printer Driver
Group: System/Configuration/Printing

%description filter
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

%package l100l200
Summary: Epson L100/L200 Series drivers
Group: System/Configuration/Printing
Requires: epson-inkjet-printer-filter = %EVR
Provides: printer-driver-l100l200 = %EVR
Obsoletes: printer-driver-l100l200 < %EVR

%description l100l200
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

This printer driver is supporting the following printers.
- L100
- L101
- L200
- L201

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%package 201601w
Summary: Epson L380/L382 Series drivers
Group: System/Configuration/Printing
Requires: epson-inkjet-printer-filter = %EVR
Provides: printer-driver-201601w = %EVR
Obsoletes: printer-driver-201601w < %EVR

%description 201601w
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

This printer driver is supporting the following printers.
- L380
- L382

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%package 201401w
Summary: Epson L455_L456_L36x_L22x_L31x_L13x Series drivers
Group: System/Configuration/Printing
Requires: epson-inkjet-printer-filter = %EVR
Provides: printer-driver-201401w = %EVR
Obsoletes: printer-driver-201401w < %EVR

%description 201401w
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

This printer driver is supporting the following printers.
- L456
- L455
- L366
- L365
- L362
- L360
- L312
- L310
- L222
- L220
- L132
- L130

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%package 201310w
Summary: Epson L120 Series drivers
Group: System/Configuration/Printing
Requires: epson-inkjet-printer-filter = %EVR
Provides: printer-driver-201310w = %EVR
Obsoletes: printer-driver-201310w < %EVR

%description 201310w
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

This printer driver is supporting the following printers.
- L120

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%package 201215w
Summary: Epson M100/M200 Series drivers
Group: System/Configuration/Printing
Requires: epson-inkjet-printer-filter = %EVR
Provides: printer-driver-201215w = %EVR
Obsoletes: printer-driver-201215w < %EVR

%description 201215w
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

This printer driver is supporting the following printers.
- M100
- M101
- M105
- M200
- M201
- M205

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%package 201207w
Summary: Epson L110/210/300/350/355/550/555 Series drivers
Group: System/Configuration/Printing
Requires: epson-inkjet-printer-filter = %EVR
Provides: printer-driver-201207w = %EVR
Obsoletes: printer-driver-201207w < %EVR

%description 201207w
This software is a filter program used with Common UNIX Printing System
(CUPS) from the Linux. This can supply the high quality print with Seiko
Epson Color Ink Jet Printers.

This printer driver is supporting the following printers.
- L110
- L111
- L210
- L211
- L300
- L301
- L303
- L350
- L351
- L353
- L355
- L356
- L550
- L551
- L555

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
subst 's,^/usr/lib,%_libdir,' %buildroot%_sysconfdir/ld.so.conf.d/*.conf
rm -rf %buildroot%_prefix/doc
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_datadir/cups/model/%name
mkdir -p %buildroot%_datadir/%name/resource
for dir in l100l200 201207w 201215w 201310w 201401w 201601w
do
	pushd $dir
	# Install PPDs
	cp -av ppds/* %buildroot%_datadir/cups/model/%name
	# Install prebuilt libraries
%ifarch %ix86
	cp -av lib/*.so* %buildroot%_libdir/%name
%else
	cp -av lib64/*.so* %buildroot%_libdir/%name
%endif
	# Install resource
	mkdir -p %buildroot%_datadir/%name/$dir
	cp -av resource/*.data %buildroot%_datadir/%name/resource
	# Install watermarks
	mkdir -p %buildroot%_datadir/%name/$dir/watermark
	cp -av watermark/* %buildroot%_datadir/%name/$dir/watermark
	popd
done
chmod +x %buildroot%_libdir/%name/*
# Compress all ppds
gzip -n9 %buildroot%_datadir/cups/model/%name/*.ppd

%files filter
%doc AUTHORS README COPYING*
%_libexecdir/cups/filter/epson_inkjet_printer_filter
%_sysconfdir/ld.so.conf.d/*.conf
%dir %_datadir/%name
%dir %_datadir/%name/resource
%dir %_libdir/%name

%files l100l200
%doc l100l200/AUTHORS l100l200/README l100l200/COPYING*
%_datadir/%name/l100l200
%_datadir/%name/resource/Epson_l100l200*.data
%_libdir/%name/libEpson_l100l200.*
%_datadir/cups/model/%name/EPSON_L100_Series.ppd*
%_datadir/cups/model/%name/EPSON_L200_Series.ppd*

%files 201207w
%doc 201207w/AUTHORS 201207w/README 201207w/COPYING*
%_datadir/%name/201207w
%_datadir/%name/resource/Epson_201207w*.data
%_libdir/%name/libEpson_201207w.*
%_datadir/cups/model/%name/EPSON_L110.ppd*
%_datadir/cups/model/%name/EPSON_L210.ppd*
%_datadir/cups/model/%name/EPSON_L300.ppd*
%_datadir/cups/model/%name/EPSON_L350.ppd*
%_datadir/cups/model/%name/EPSON_L355.ppd*
%_datadir/cups/model/%name/EPSON_L550.ppd*
%_datadir/cups/model/%name/EPSON_L555.ppd*

%files 201215w
%doc 201215w/AUTHORS 201215w/README 201215w/COPYING*
%_datadir/%name/201215w
%_datadir/%name/resource/Epson_201215w*.data
%_libdir/%name/libEpson_201215w.*
%_datadir/cups/model/%name/EPSON_M100.ppd*
%_datadir/cups/model/%name/EPSON_M105.ppd*
%_datadir/cups/model/%name/EPSON_M200.ppd*
%_datadir/cups/model/%name/EPSON_M205.ppd*

%files 201310w
%doc 201310w/AUTHORS 201310w/README 201310w/COPYING*
%_datadir/%name/201310w
%_datadir/%name/resource/Epson_201310w*.data
%_libdir/%name/libEpson_201310w.*
%_datadir/cups/model/%name/EPSON_L120.ppd*

%files 201401w
%doc 201401w/AUTHORS 201401w/README 201401w/COPYING*
%_datadir/%name/201401w
%_datadir/%name/resource/Epson_201401w*.data
%_libdir/%name/libEpson_201401w.*
%_datadir/cups/model/%name/EPSON_L130.ppd*
%_datadir/cups/model/%name/EPSON_L132.ppd*
%_datadir/cups/model/%name/EPSON_L220.ppd*
%_datadir/cups/model/%name/EPSON_L222.ppd*
%_datadir/cups/model/%name/EPSON_L310.ppd*
%_datadir/cups/model/%name/EPSON_L312.ppd*
%_datadir/cups/model/%name/EPSON_L360.ppd*
%_datadir/cups/model/%name/EPSON_L362.ppd*
%_datadir/cups/model/%name/EPSON_L365.ppd*
%_datadir/cups/model/%name/EPSON_L366.ppd*
%_datadir/cups/model/%name/EPSON_L455.ppd*
%_datadir/cups/model/%name/EPSON_L456.ppd*

%files 201601w
%doc 201601w/AUTHORS 201601w/README 201601w/COPYING*
%_datadir/%name/201601w
%_datadir/%name/resource/Epson_201601w*.data
%_libdir/%name/libEpson_201601w.*
%_datadir/cups/model/%name/Epson-L380_Series-epson-driver.ppd*
%_datadir/cups/model/%name/Epson-L382_Series-epson-driver.ppd*

%changelog
* Wed Sep 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.gitb36bfa8
- Initial build for Sisyphus
