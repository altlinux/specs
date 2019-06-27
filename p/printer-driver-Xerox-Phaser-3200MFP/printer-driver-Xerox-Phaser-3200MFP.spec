%define rname Xerox-Phaser-3200MFP
Name:     printer-driver-%rname
Version:  1.0
Release:  alt1

Summary:  Postscript printer driver ppd for Xerox Phaser 3200MFP
License:  GPL v2
Group:    System/Configuration/Printing
Url:      https://www.openprinting.org/ppd-o-matic.php?driver=Postscript&printer=Xerox-Phaser_3200MFP&show=0

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Postscript printer driver ppd for Xerox Phaser 3200MFP

%prep
%setup -n %name-%version

%install
install -d  %buildroot%_datadir/cups/model/%rname
install -m 0644 *.ppd %buildroot%_datadir/cups/model/%rname/

%files
%_datadir/cups/model/%rname/

%changelog
* Thu Jun 27 2019 Denis Medvedev <nbr@altlinux.org> 1.0-alt1
Initial Sisyphus version
