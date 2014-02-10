%define origname tu154b

Name: FlightGear-%origname
Version: 3.0
Release: alt1

Summary: Tu-154B
License: GPL
Group: Games/Arcade

Url: http://www.flightgear.ru/tu-154b2-2/
Source: http://yurik.flightgear.ru/tu154b-release/tu154b-3.0_jul2013.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: FlightGear-data
AutoReqProv: no

%set_fixup_method skip
%set_cleanup_method skip
%set_compress_method none
%set_verify_elf_method skip

%define fgroot %_datadir/flightgear/
%define tu154root %fgroot/Aircraft/%origname

%description
Tu-154B2 model for FlightGear is a complex high-quality aircraft model
for the adequate flight sim.

This package includes Russian instrument labels, please see the source
for English ones (not grafted yet).

%prep
%setup -n %origname
mv Docs/*.pdf .
rmdir Docs

%build

%install
mkdir -p %buildroot%tu154root
mv AI/ %buildroot%fgroot/
mv */ *.{jpg,png,xml} Readme TODO %buildroot%tu154root

%files
%tu154root
%fgroot/AI/*/*
%doc *.pdf

%changelog
* Mon Feb 10 2014 Michael Shigorin <mike@altlinux.org> 3.0-alt1
- initial release (kudos to flightgear.ru guys!)

