Name: zcad
Summary: General purpose CAD system
Summary(ru_RU.UTF-8): Система автоматизированного проектирования общего назначения
Version: 0.9.16.2
Release: alt1
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/zamtmn/zcad
Vcs: https://github.com/zamtmn/zcad.git

Source: %name-%version.tar
Source1: agraphlaz.tar
Source2: callstack_memprofiler.tar
Source3: fpdwg.tar
Source4: fphunspell.tar
Source5: fpspreadsheet.tar
Source6: lape.tar
Source7: metadarkstyle.tar
Source8: zmacros.tar
Source9: zreaders.tar
Source10: ztoolbars.tar
Source11: nodetree.tar

Patch: %name-%version-%release.patch

Requires: libGLU

BuildRequires: lazarus
BuildRequires: ImageMagick-tools
BuildRequires: pkgconfig(dri)
BuildRequires: qt5pas-devel

ExclusiveArch: x86_64

%description
ZCAD is a CAD program written in FreePascal/Lazarus. It supports DXF file format
and provides various CAD tools for 2D/3D design. The program includes features
for technical drawing, entity manipulation, and layer management.

%description -l ru_RU.UTF-8
ZCAD - это САПР программа, написанная на FreePascal/Lazarus. Поддерживает формат
файлов DXF и предоставляет различные инструменты САПР для 2D/3D проектирования.
Программа включает функции для технического черчения, манипулирования объектами
и управления слоями.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11

# Remove all binaries
find . -name \*.dll -delete

%build
make installpkgstolaz
# build with debug information
make cleanzcad \
	BUILDMODE=Debug_Linux_X86_64_qt5 \
	INSTALLPREFIX=%_prefix/libexec/zcad

%install
mkdir -p %buildroot%_prefix/libexec/zcad/
cp -r cad/data/* %buildroot%_prefix/libexec/zcad/
mkdir -p %buildroot%_prefix/libexec/zcad/bin/
cp -r cad/bin/* %buildroot%_prefix/libexec/zcad/bin/
rm -r %buildroot%_prefix/libexec/zcad/bin/i386-win32
rm -r %buildroot%_prefix/libexec/zcad/bin/x86_64-win64

mkdir -p %buildroot%_bindir
# create run script
cat > %buildroot%_bindir/zcad << EOF
#!/bin/sh
[ -z "\$WAYLAND_DISPLAY" ] || export QT_QPA_PLATFORM=xcb
%_prefix/libexec/zcad/bin/x86_64-linux/zcad
EOF
chmod +x %buildroot%_bindir/zcad

mkdir -p %buildroot%_sysconfdir/zcad/
cp -r cad/cfg/* %buildroot%_sysconfdir/zcad/

# install menu icons
for N in 16 32 48; do
	convert cad_source/zcad.ico -scale ${N}x${N} $N.png;
	install -D -m 0644 $N-0.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/zcad.png
done

mkdir -p %buildroot%_desktopdir
# Create desktop file
cat > %buildroot%_desktopdir/zcad.desktop << EOF
[Desktop Entry]
Name=ZCAD
Comment=General purpose CAD system
Comment[ru]=Система автоматизированного проектирования общего назначения
Exec=zcad
Icon=zcad
Terminal=false
Type=Application
Categories=Graphics;Engineering;
EOF

%files
%doc README.md
%_bindir/zcad
%_sysconfdir/zcad
%_prefix/libexec/zcad
%_desktopdir/zcad.desktop
%_iconsdir/hicolor/*/apps/zcad.png

%changelog
* Wed Apr 16 2025 Anton Midyukov <antohami@altlinux.org> 0.9.16.2-alt1
- initial build (Closes: 53614)
