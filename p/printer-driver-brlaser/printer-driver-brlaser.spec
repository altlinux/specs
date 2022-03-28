%define _cmake__builddir BUILD

Name: printer-driver-brlaser
Version: 6
Release: alt3

Source: %name-%version.tar

Summary: Brother laser printer driver
Url: https://github.com/pdewacht/brlaser
License: GPL-2.0-or-later
Group: System/Configuration/Printing

BuildRequires: cmake libcups-devel gcc-c++
BuildRequires: cups

%description
brlaser is a CUPS driver for Brother laser printers.

Although most Brother printers support a standard
printer language such as PCL or PostScript, not all do.
If you have a monochrome Brother laser printer (or multi-function device)
and the other open source drivers don't work, this one might help.

This driver has been reported to work with these printers:

Brother DCP-1510 series
Brother DCP-1600 series
Brother DCP-7030
Brother DCP-7040
Brother DCP-7055
Brother DCP-7055W
Brother DCP-7060D
Brother DCP-7065DN
Brother DCP-7080
Brother DCP-L2500D series
Brother DCP-L2520D series
Brother DCP-L2540DW series
Brother HL-1110 series
Brother HL-1200 series
Brother HL-2030 series
Brother HL-2140 series
Brother HL-2220 series
Brother HL-2270DW series
Brother HL-5030 series
Brother HL-L2300D series
Brother HL-L2320D series
Brother HL-L2340D series
Brother HL-L2360D series
Brother MFC-1910W
Brother MFC-7240
Brother MFC-7360N
Brother MFC-7365DN
Brother MFC-7840W
Brother MFC-L2710DW series
Lenovo M7605D

%prep
%setup

%build
%cmake
%cmake_build
pushd BUILD
    ppdc brlaser.drv
popd

%install
%cmakeinstall_std
# using compiled ppds
rm %buildroot%_datadir/cups/drv/brlaser.drv
# install compiled ppds
install -Dm644 BUILD/ppd/* -t %buildroot/%_datadir/cups/model/brlaser

%files
%_libexecdir/cups/filter/rastertobrlaser
%_datadir/cups/model/brlaser

%changelog
* Mon Mar 28 2022 Sergey V Turchin <zerg@altlinux.org> 6-alt3
- update to 9d7ddda8383bfc4d205b5e1b49de2b8bcd9137f1 from master branch
- precompile ppds (closes: 42098)

* Tue Mar 24 2020 Grigory Maksimov <zacat@altlinux.org> 6-alt2
- Added patch:
  * printer-driver-brlaser-max_lines_per_block_.patch

* Tue Oct 15 2019 Grigory Maksimov <zacat@altlinux.org> 6-alt1
- Initial build for ALT
