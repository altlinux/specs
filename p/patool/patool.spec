Name: patool
Version: 1.5
Release: alt1

Summary: Portable command line archive file manager

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv3+
Group: Archiving/Other
Url: https://github.com/wummel/patool/

# Real URL for download
# Source-url: https://github.com/wummel/patool/archive/upstream/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
Various archive types can be created, extracted, tested and listed by
patool. The advantage of patool is its simplicity in handling archive
files without having to remember a myriad of programs and options.

The archive format is determined by the file(1) program and as a
fallback by the archive file extension.

patool supports 7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc),
ARJ (.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio),
DEB (.deb), GZIP (.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz),
LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), TAR (.tar),
XZ (.xz), ZIP (.zip, .jar) and ZOO (.zoo) formats. It relies on helper
applications to handle those archive formats (for example bzip2 for
BZIP2 archives).

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%_man1dir/%name.*
%python_sitelibdir/patoolib/
%python_sitelibdir/_Patool_configdata.py
%python_sitelibdir/Patool-*.egg-info

%changelog
* Mon May 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Tue Sep 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (with rpmrb script)

* Fri Jul 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version (1.2) with rpmgs script

* Thu Jun 13 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.13-1mdv2011.0
+ Revision: 645373
- update to new version 0.13

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.11-1mdv2011.0
+ Revision: 594246
- new version 0.11
- install files to a correct location
- fix license and clean spec

* Fri Aug 13 2010 Shlomi Fish <shlomif@mandriva.org> 0.10-2mdv2011.0
+ Revision: 569471
- Add missing BuildRequires (thanks to Anssi)
- Change to a more apprporiate group
- Correct some rpm errors - no Vendor
- Changed to the Mandriva release
- import patool


