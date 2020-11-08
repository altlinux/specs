Name: inkscape-open-symbols
Version: 1.2.1
Release: alt1

Summary: Open source SVG symbol sets that can be used as Inkscape symbols

License: MIT
Group: Graphics
Url: https://github.com/Xaviju/inkscape-open-symbols

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Xaviju/inkscape-open-symbols/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArchitectures: noarch

%description
Symbol libraries are sets of SVG symbols located in one SVG document.
For the more technical audience, Inkscape searches for any valid SVG file
with symbols (<symbol> element) in your system configuration directory %_datadir/inkscape)

%prep
%setup

%install
mkdir -p %buildroot%_datadir/inkscape/symbols/
cp -a . %buildroot%_datadir/inkscape/symbols/
rm -fv %buildroot%_datadir/inkscape/symbols/*.*

%files
%doc LICENSE.txt README.md
%_datadir/inkscape/symbols/

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Sisyphus
