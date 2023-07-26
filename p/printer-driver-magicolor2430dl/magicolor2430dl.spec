%define rname magicolor2430dl

Summary: Cups Driver for KONICA MINOLTA magicolor 2430 DL
Name: printer-driver-%rname
Version: 1.6.1
Release: alt2
License: GPLv2
Group: System/Configuration/Printing
Url: http://printer.konicaminolta.net/
# site dead
Source: %rname-%version.tar
Patch1: magicolor2430DL-shared_system_libs.patch
Patch2: magicolor2430DL-1.6.1-cups-2.2.patch

BuildRequires: automake libcups-devel libjbig-devel liblcms-devel
Requires: cups

%description
This package contains KONICA MINOLTA CUPS LavaFlow stream(PCL-like) filter
rastertokm2430dl and the PPD file. The filter converts CUPS raster data to
KONICA MINOLTA LavaFlow stream.

This package contains CUPS drivers (PPD) for the following printers:

 o KONICA MINOLTA magicolor 2430 DL printer

%prep
%setup -n %rname-%version
%patch1
%patch2 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog
%_libdir/cups/filter/rastertokm2430dl
%_datadir/KONICA_MINOLTA/mc2430DL
%_datadir/cups/model/KONICA_MINOLTA/km2430dl.ppd*

%changelog
* Wed Jul 26 2023 Oleg Solovyov <mcpain@altlinux.org> 1.6.1-alt2
- use autoreconf

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.6.1-alt1
- Initial build for ALT

