%define origname tu154b
%define rel _feb2014

Name: FlightGear-%origname
Version: 3.1
Release: alt1

Summary: Tu-154B
License: GPL
Group: Games/Arcade

Url: http://www.flightgear.ru/tu-154b2-2/
Source: http://yurik.flightgear.ru/tu154b-release/%origname-%version%rel.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: FlightGear-data >= 3.0.0
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
mv */ *.{jpg,png,xml} Readme %buildroot%tu154root

%files
%tu154root
%doc *.pdf

%changelog
* Wed Oct 22 2014 Michael Shigorin <mike@altlinux.org> 3.1-alt1
- 3.1 (AI part has been merged upstream)

* Mon Feb 10 2014 Michael Shigorin <mike@altlinux.org> 3.0-alt2
- versioned Requires:

* Mon Feb 10 2014 Michael Shigorin <mike@altlinux.org> 3.0-alt1
- initial release (kudos to flightgear.ru guys!)

