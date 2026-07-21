%define _unpackaged_files_terminate_build 1

Name: hfcmystran
Version: 0.1.0
Release: alt1

Summary: Bring Mystran into FreeCAD
License: GPL-3.0
Group: Engineering
URL: https://github.com/ceanwang/hfcMystran

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

AutoProv: yes,nopython
AutoReq: yes,nopython

Requires: freecad
Requires: mystran
Requires: /usr/bin/xdg-open

Source: %name-%version.tar

# no freecad
ExcludeArch: %ix86

%description
Pre/Post processor for Mystran within FreeCAD.

%prep
%setup
sed -i "s|https://github.com/ceanwang/hfcMystran/blob/master/||" README.md
sed -i "s|\./resources/|/resources/|" *.py
mv -v resources/NEU.svg resources/neu.svg
mv -v resources/NeuW.svg resources/neuw.svg
mv -v resources/F06.svg resources/f06.svg
sed -i "s|notepad|xdg-open|" hfcMystranF06In.py \
                             hfcMystranLogIn.py \
                             hfcMystranErrIn.py \
                             hfcMystranOpenDat.py

%install
mkdir -p %buildroot%_libdir/freecad/Mod/hfcMystran
cp -avp *.py %buildroot%_libdir/freecad/Mod/hfcMystran/
cp -arvp QuickStart %buildroot%_libdir/freecad/Mod/hfcMystran/
cp -arvp resources %buildroot%_libdir/freecad/Mod/hfcMystran/

%files
%doc LICENSE README.md Screenshot
%_libdir/freecad/Mod/hfcMystran

%changelog
* Mon Jul 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
