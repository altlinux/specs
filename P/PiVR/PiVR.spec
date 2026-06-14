Name:    PiVR
Version: 1.8.4
Release: alt1

Summary: PiVR tracks animals in real time and delivers light stimuli
License: BSD-3-Clause
Group:   Sciences/Biology
URL:     https://pivr.readthedocs.io
VCS:     https://gitlab.com/LouisLab/pivr.git

Source: %name-%version.tar
Patch0: PiVR-1.8.4-settings-user-config.patch
Patch1: PiVR-1.8.4-window-icon.patch

BuildRequires: python3-dev
BuildRequires: desktop-file-utils
BuildRequires: python3-module-pillow

Requires: python3
Requires: python3-module-matplotlib
Requires: python3-module-matplotlib-tk
Requires: python3-module-numpy
Requires: python3-module-pandas
Requires: python3-module-pillow
Requires: python3-module-opencv
Requires: python3-module-scipy
Requires: python3-module-scikit-image
Requires: python3-module-imageio
Requires: python3-module-natsort
Requires: python3-modules-tkinter

BuildArch: noarch

%description
PiVR - virtual reality for small animals.
PiVR is a virtual reality system for small animals with a dedicated website: www.PiVR.org
It creates virtual realities by detecting the position of an animal in real space (left)
and depending on the position of the animal in virtual space (center) presents the
appropriate stimulus (right).

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
# Python project, no configure/make needed

%install
mkdir -p %buildroot%_datadir/%name
cp -a PiVR %buildroot%_datadir/%name/

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
# Use system site-packages only, ignore user-local ~/.local/lib/python3
exec python3 -s %_datadir/%name/PiVR/start_GUI.py "$@"
EOF
chmod 755 %buildroot%_bindir/%name

# Desktop entry and icon
cat > %name.desktop <<'EOF'
[Desktop Entry]
Name=PiVR
Comment=Virtual reality system for small animals
Exec=PiVR
Icon=PiVR
StartupWMClass=PiVR
Type=Application
Terminal=false
Categories=Science;Education;Biology;
Keywords=biology;neuroscience;tracking;virtual;reality;experiment;
EOF
desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

# Icon
mkdir -p %buildroot%_iconsdir/hicolor/256x256/apps
python3 -c "from PIL import Image; \
img = Image.open('PiVR/pics/PiVRLogoDesktop.ico'); \
img = img.resize((256, 256), Image.LANCZOS); \
img.save('%buildroot%_iconsdir/hicolor/256x256/apps/%name.png')"

%files
%doc LICENSE.* README.*
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/256x256/apps/%name.png

%changelog
* Sun Jun 14 2026 Sergey Palcheh <minergenon@altlinux.org> 1.8.4-alt1
- Initial build for Sisyphus
