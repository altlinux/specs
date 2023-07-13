Name: mricrogl
Version: 1.2.20220720
Release: alt1

Summary: MRIcroGL is a cross-platform tool for viewing DICOM and NIfTI format images. 
License: BSD-3-Clause
Group: Sciences/Medicine

Url: https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage
VCS: https://github.com/rordenlab/MRIcroGL.git
Source: %name-%version.tar
Source2: %name.watch
ExclusiveArch: x86_64

BuildRequires: lazarus

%description
MRIcroGL is medical image viewer that allows you to load overlays 
(e.g. statistical maps), draw regions of interest (e.g. create lesion maps).

The licenses for some components differ from the license for the sowtware.
See details in:
- %_datadir/MRIcroGL/license.txt
- %_datadir/MRIcroGL/Resources/matcap/license.txt

%prep
%setup

%build
lazbuild -B MRIcroGL.lpi

%install
install -m755 -d %buildroot%_bindir/
install -m755 -T MRIcroGL %buildroot%_bindir/mricrogl

install -d %buildroot%_datadir/MRIcroGL/
install -D license.txt %buildroot%_datadir/MRIcroGL/

install -d %buildroot%_datadir/MRIcroGL/Resources/

install -d %buildroot%_datadir/MRIcroGL/Resources/atlas/
install -D Resources/atlas/* %buildroot%_datadir/MRIcroGL/Resources/atlas/

install -d %buildroot%_datadir/MRIcroGL/Resources/lut/
install -D Resources/lut/* %buildroot%_datadir/MRIcroGL/Resources/lut/

install -d %buildroot%_datadir/MRIcroGL/Resources/matcap/
install -d %buildroot%_datadir/MRIcroGL/Resources/matcap/unused/
install -D Resources/matcap/*.jpg %buildroot%_datadir/MRIcroGL/Resources/matcap/
install -D Resources/matcap/license.txt %buildroot%_datadir/MRIcroGL/Resources/matcap/
install -D Resources/matcap/unused/*.jpg     %buildroot%_datadir/MRIcroGL/Resources/matcap/unused/

install -d %buildroot%_datadir/MRIcroGL/Resources/shader/
install -D Resources/shader/* %buildroot%_datadir/MRIcroGL/Resources/shader/

install -d %buildroot%_datadir/MRIcroGL/Resources/standard/
install -D Resources/standard/* %buildroot%_datadir/MRIcroGL/Resources/standard/

install -D Resources/Roboto.json %buildroot%_datadir/MRIcroGL/Resources/
install -D Resources/Roboto.png %buildroot%_datadir/MRIcroGL/Resources/
install -d %buildroot%_iconsdir/hicolor/scalable/apps/
install -D Resources/mricrogl.svg %buildroot%_iconsdir/hicolor/scalable/apps/

install -d %buildroot%_desktopdir
install -D deb/mricrogl.desktop %buildroot%_desktopdir

%files
%_bindir/*
%_datadir/MRIcroGL/
%_iconsdir/hicolor/scalable/apps/mricrogl.svg
%_desktopdir/mricrogl.desktop

%doc COMMANDS.md DOCKER.md PRIVACY.md PYTHON.md README.md

%changelog
* Thu Jun 22 2023 Alexey Shemyakin <alexeys@altlinux.org> 1.2.20220720-alt1
- Initial build for ALT.

