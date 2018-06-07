# lsb.spec.in -- an rpm spec file templete for LSB package
# Epson Inkjet Printer Driver (ESC/P-R) for Linux
# Copyright (C) Seiko Epson Corporation 2014.
#  This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110, USA.

%define pkg     epson-inkjet-printer-escpr
%define ver     1.6.20
%define rel     1

# used in RPM macro set for the LSB Driver Development Kit
%define drivername      epson-inkjet-printer-escpr
%define driverstr       epson-inkjet-printer-escpr
%define distribution    LSB
%define manufacturer    EPSON
%define supplier        %{drivername}
%define lsbver          3.2

%define extraversion    -%{rel}lsb%{lsbver}
%define supplierstr     Seiko Epson Corporation

AutoReqProv: no

Name: %{pkg}
Version: %{ver}
Release: alt1
License: GPL
URL: http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
Group: System/Configuration/Hardware
Summary: Epson Inkjet Printer Driver (ESC/P-R) for Linux

Source0: %{name}-%{version}.tar.gz

BuildRequires: libcups-devel

%description
This software is a filter program used with Common UNIX Printing
System (CUPS) from the Linux. This can supply the high quality print
with Seiko Epson Color Ink Jet Printers.

This product supports only EPSON ESC/P-R printers. This package can be
used for all EPSON ESC/P-R printers.

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

# Packaging settings
%prep
%setup -q

%build
%undefine _configure_gettext
%autoreconf
%configure \
	--disable-static \
        --with-cupsfilterdir=%_libexecdir/cups/filter \
        --with-cupsppddir=%_datadir/cups/model
make pkgdatadir=%_datadir

%install
make install-strip DESTDIR=%buildroot pkgdatadir=%_datadir

%files
%doc README README.ja COPYING AUTHORS NEWS
%_libdir/libescpr.so*
%_libexecdir/cups/filter/epson-escpr*
%_datadir/cups/model/%name

%changelog
* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.20-alt1
- Initial build in Sisyphus (imported from epson-inkjet-printer-escpr-1.6.20-1lsb3.2.src.rpm)
