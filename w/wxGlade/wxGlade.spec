%define name wxGlade

Name: wxGlade
Summary: A GUI builder for wxWindows/wxPython
Version: 1.0.4
Release: alt1
License: MIT
Group: Development/Other
Url: http://wxglade.sourceforge.net/
Packager: Konstantin Artyushkin <akv@altlinux.org>

# Source-url: https://github.com/wxGlade/wxGlade/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: ImageMagick-tools
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: rpm-build-python3
BuildArch: noarch

%add_python3_self_prov_path %buildroot%python3_sitelibdir/wxglade/

%description
wxGlade is a GUI designer written in Python with the popular GUI toolkit
wxPython, that helps you create wxWindows/wxPython user interfaces. At the
moment it can generate Python, C++ and XRC (wxWindows' XML resources) code.

As you can guess by the name, its model is Glade, the famous GTK+/GNOME
GUI builder, with which wxGlade shares the philosophy and the look & feel
(but not a line of code).

It is not (and will never be) a full featured IDE, but simply a "designer":
the generated code does nothing apart from displaying the created widgets.
If you are looking for a complete IDE, maybe Boa Constructor or PythonCard
is the right tool.

%prep
%setup

%build
%python3_build

%install
%python3_install

# create run script
cat > %buildroot%_bindir/wxglade << EOF
#!/bin/sh
%__python3 %python3_sitelibdir/wxglade/wxglade.py
EOF

# icons
mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
convert -resize 32x32 icons/icon.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 icons/icon.png %buildroot%_miconsdir/%name.png
convert -resize 48x48 icons/icon.png %buildroot%_liconsdir/%name.png

# menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=%name
Comment=A GUI builder for wxWindows/wxPython
Exec=%_bindir/wxglade
Icon=%name
Terminal=false
Type=Application
Categories=Development;GUIDesigner;
EOF

# docs handled by doc section
rm -rf %buildroot%_docdir/wxglade/*
cp -r docs/html %buildroot%_docdir/wxglade/

# remove script for windows
rm %buildroot/%python3_sitelibdir/wxglade/msw.py

%files
%doc README.txt
%doc %_docdir/wxglade/
%_bindir/wxglade
%python3_sitelibdir/wxglade
%python3_sitelibdir/%name-%version-py%__python3_version.egg-info
%_desktopdir/%name.desktop
%_iconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_datadir/wxglade

%changelog
* Mon Jan 16 2023 Anton Midyukov <antohami@altlinux.org> 1.0.4-alt1
- new version (1.0.4) with rpmgs script

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue May 18 2021 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1
- new version (1.0.2) with rpmgs script
- cleanup spec

* Sat May 02 2020 Anton Midyukov <antohami@altlinux.org> 0.7.2-alt3
- Fix shebang python2

* Sun Aug 05 2018 Anton Midyukov <antohami@altlinux.org> 0.7.2-alt2
- Cleanup no actual requires
- fix desktop categories

* Tue Jul 19 2016 Konstantin Artyushkin <akv@altlinux.org> 0.7.2-alt1
- new version

* Tue Jul 19 2016 Konstantin Artyushkin <akv@altlinux.org> 0.6.8-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.6.8-2
+ Revision: 0083787
- MassBuild#464: Increase release tag
