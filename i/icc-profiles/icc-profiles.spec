Name: icc-profiles
Version: 1.0.1
Release: alt1

Summary: ICC color profiles
License: distributable
Group: Graphics

Source: %name-%version.tar.bz2

Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildArch: noarch

%description
ICC color profiles for use with Scribus, Gimp, CinePaint, and
other color profile aware software.

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/color/icc
install -m644 *.ic{c,m} %buildroot%_datadir/color/icc/

%files
%doc ECI_Offset_2004_ENG.pdf ECI-RGB_BitteLesen ECI-RGB_ReadMe ISOcoated_info.pdf
%doc ISOuncoated_info.pdf ISOuncoatedyellow_info.pdf ISOwebcoated_info.pdf
%doc GenericCMYK.txt debian/copyright
%dir %_datadir/color
%dir %_datadir/color/icc
%_datadir/color/icc/*

%changelog
* Mon Jan 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- initial release

