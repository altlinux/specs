Name: helpdeco
Version: 2.1.3
Release: alt2

Summary: Utility program to dissect Windows help files
License: GPLv2+
Group: Text tools
URL: http://sourceforge.net/projects/helpdeco/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz

%description
HELPDECO dissects HLP help files of Windows 3.0, 3.1, 3.11, and '95 and
many MVB multi media viewer titles into all files required for a rebuild
using the appropriate help compiler HC30, HC31, HCP, HCW, HCRTF, WMVC,
MMVC or MVC:
HPJ - help project file, use as parameter when calling help compiler
MVP - multi media project file, parameter for multi media help compiler
RTF - text file containing whole content of help file and all footnotes
PH  - phrases file (same as produced by help compiler)
ICO - icon of help file if embedded
BMP/WMF/SHG/MRB - embedded pictures in appropriate format
Baggage - all baggage files contained in help file

%prep
%setup -q

%build
%make_build CC="%__cc %optflags"

%install
mkdir -p %buildroot%_bindir/
install -pD -m755 helpdeco zapres splitmrb %buildroot%_bindir/

%files
%doc ChangeLog NEWS README README.de helpfile.txt
%_bindir/*

%changelog
* Tue Oct 30 2012 Igor Zubkov <icesik@altlinux.org> 2.1.3-alt2
- rebuilt for debuginfo

* Sat Nov 19 2005 Igor Zubkov <icesik@altlinux.ru> 2.1.3-alt1
- 2.1.3
- remove helpdeco-2.1.2-alt-strlcpy.patch (fixed in upstream)

* Fri Oct 21 2005 Igor Zubkov <icesik@altlinux.ru> 2.1.2-alt1
- initial build for Sisyphus.
