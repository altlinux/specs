Name:    SkelForm
Version: 0.7.0
Release: alt1

Summary: 2D skeletal animation editor
License: GPL-3.0-only
Group:   Graphics
URL:     https://skelform.org
VCS:     https://github.com/Retropaint/SkelForm

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: %name-development-%version.tar
Patch0: SkelForm-0.7.0-fix-render-target-format.patch
Patch1: SkelForm-0.7.0-set-app-id.patch
Patch2: SkelForm-0.7.0-exit-without-segfault.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: glib2-devel libgtk+3-devel

%description
SkelForm is a 2D skeletal animator, designed for quick and easy
integrationinto games or other software with simple techniques
and developer-curated runtime documentation.

%prep
%setup -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%rust_prep

%build
%rust_build

%install
%rust_install

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<'EOF'
[Desktop Entry]
Name=SkelForm
Comment=2D skeletal animation editor
Exec=SkelForm %F
Icon=SkelForm
Terminal=false
Type=Application
Categories=Graphics;2DGraphics;RasterGraphics;
StartupNotify=true
StartupWMClass=SkelForm
MimeType=application/x-skelform;
EOF

mkdir -p %buildroot%_datadir/mime/packages
cat > %buildroot%_datadir/mime/packages/%name.xml <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-skelform">
    <comment>SkelForm animation project</comment>
    <glob pattern="*.skf"/>
    <icon name="SkelForm"/>
  </mime-type>
</mime-info>
EOF

mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
mkdir -p %buildroot%_iconsdir/hicolor/256x256/apps
cp assets/skf_icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
cp assets/skf_icon.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png

%files
%doc LICENSE.md readme.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/256x256/apps/%name.png

%changelog
* Thu Jul 02 2026 Sergey Palcheh <minergenon@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
