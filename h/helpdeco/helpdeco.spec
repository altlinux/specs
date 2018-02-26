Name: helpdeco
Version: 2.1.3
Release: alt1

Summary: helpdeco -- utility program to dissect Windows help files
License: GPL v2
Group: Text tools
URL: http://sourceforge.net/projects/helpdeco/
Packager: Igor Zubkov <icesik@altlinux.ru>

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
%__mkdir_p %buildroot%_bindir/
%__install -pD -m755 helpdeco zapres splitmrb %buildroot%_bindir/

%files
%doc ChangeLog helpfile.txt NEWS README.de README
%_bindir/*

%changelog
* Sat Nov 19 2005 Igor Zubkov <icesik@altlinux.ru> 2.1.3-alt1
- 2.1.3
- remove helpdeco-2.1.2-alt-strlcpy.patch (fixed in upstream)

* Fri Oct 21 2005 Igor Zubkov <icesik@altlinux.ru> 2.1.2-alt1
- initial build for Sisyphus.
