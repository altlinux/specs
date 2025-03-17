%define rname magicolor5430dl

Summary: Cups Driver for KONICA MINOLTA magicolor 5430 DL
Name: printer-driver-%rname
Version: 1.8.1
Release: alt3
License: GPLv2
Group: System/Configuration/Printing
Url: http://printer.konicaminolta.net/
# site dead
Source: %rname-%version.tar
Patch1: magicolor2430DL-shared_system_libs.patch
Patch2: magicolor5430DL-1.8.1-cups-2.2.patch
# https://raw.githubusercontent.com/OpenMandrivaAssociation/cups-drivers-magicolor5430dl/master/magicolor5430DL-lcms2.patch
Patch3: magicolor5430DL-lcms2.patch

BuildRequires: automake
BuildRequires: libcups-devel
BuildRequires: libjbig-devel
BuildRequires: liblcms2-devel

Requires: cups

%description
This package contains KONICA MINOLTA CUPS LavaFlow stream(PCL-like) filter
rastertokm5430dl and the PPD file. The filter converts CUPS raster data to
KONICA MINOLTA LavaFlow stream.

This package contains CUPS drivers (PPD) for the following printers:

 o KONICA MINOLTA magicolor 5430 DL printer

%prep
%setup -n %rname-%version
%patch1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog
%_libdir/cups/filter/rastertokm5430dl
%_datadir/KONICA_MINOLTA/mc5430DL
%_datadir/cups/model/KONICA_MINOLTA/km5430dl.ppd*

%changelog
* Mon Mar 17 2025 Constantin Sunzow <protvin@altlinux.org> 1.8.1-alt3
- Rebuild with liblcms2.

* Wed Jul 26 2023 Oleg Solovyov <mcpain@altlinux.org> 1.8.1-alt2
- use autoreconf

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.8.1-alt1
- Initial build for ALT

