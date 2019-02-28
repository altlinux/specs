Name: epsidm24-secc0001
Version: 1.0.0
Release: alt1

Summary: Driver for EPSON 24Pin SIDM Printers
License: GPL
Group: System/Configuration/Hardware
Vendor: Seiko Epson Corporation
Packager: Leontiy Volodin <lvol@altlinux.org>
Url: http://www.epson.com
Provides: epsidm24-secc0001

Source: %name-%version.tar.gz

Patch: epsidm24-alt-makefile.patch

Requires: cups
BuildRequires: libcups-devel

%description
Supported Models:
    - EPSON PLQ-30

%prep
%setup
%patch -p2

%build
%configure
%make

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/ppd/cupsfilters
mv ./ppd/epplq30-rastertoepsidm24-secc0001.ppd %buildroot%_datadir/ppd/cupsfilters/

rm -rf %buildroot%_datadir/ppd/Epson/epplq30-rastertoepsidm24-secc0001.ppd

%files
%doc    README
#%%doc   AUTHORS
%doc    COPYING
#%%doc   ChangeLog
%doc    INSTALL
%doc    NEWS

%dir %_prefix/lib/cups/filter
%_prefix/lib/cups/filter/rastertoepsidm24-secc0001
#%%dir %%_datadir/cups/model
#%%_datadir/cups/model/*.ppd
%dir %_datadir/ppd/cupsfilters
%_datadir/ppd/cupsfilters/*.ppd


%changelog
* Thu Feb 28 2019 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- initial build for ALT Sisyphus (thanks Andrey Cherepanov)

