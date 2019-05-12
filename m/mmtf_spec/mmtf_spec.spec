Name: mmtf_spec
Version: 1.0.head
Release: alt1

Summary: The specification of the MMTF format for biological structures

License: MIT/X11
Group: System/Libraries
Url: http://mmtf.rcsb.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

##Source-url: https://github.com/rcsb/mmtf/archive/v%version.tar.gz
# Source-url: https://github.com/rcsb/mmtf/archive/master.zip
Source: %name-%version.tar

BuildArch: noarch

%description
The specification of the MMTF format for biological structures.

The MacroMolecular Transmission Format (MMTF) is a binary encoding of biological structures.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/mmtf_spec/
cp -a * %buildroot%_datadir/mmtf_spec/

%files
%_datadir/mmtf_spec/

%changelog
* Sun May 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.head-alt1
- new version (git HEAD baa2beaa9af5393adc2c6b22f9b39fc78a269a9f) with rpmgs script

* Sun May 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
