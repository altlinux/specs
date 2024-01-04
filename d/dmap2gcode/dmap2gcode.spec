Name:    dmap2gcode
Version: 0.13
Release: alt1

Summary: dmap2gcode converts depth maps to G-Code
Summary(ru_RU.UTF8): dmap2gcode создает программу для ЧПУ на основе карты глубины
License: GPL-3.0
Group:   Engineering
URL:     https://www.scorchworks.com/Dmap2gcode/dmap2gcode.html

BuildRequires(pre): rpm-build-python3
BuildRequires: hd2u
%py3_requires tkinter


BuildArch: noarch

Source:  %name-%version.tar.gz
Source1: %name-256.png
Source2: %name-48.png
Source3: %name-docs.tar.gz
Patch0: fix_typo.patch
Patch1: fix_configfile.patch
Patch2: fix_python3.patch

%description
Dmap2gcode is a depth map cutting program. It generates G-Code for engraving or v-carving
from gray scale image. It is based on image-to-gcode from LinuxCNC.

%description -l ru_RU.UTF8
Dmap2gcode это программа, которая преобразует карту глубины (графический файл в оттенках серого)
в управляющую программу для ЧПУ (G-Code). Программа основана на компоненте imge-to-gcode из проекта 
LinuxCNC.

%prep
%setup
dos2unix %name.py
%patch0 -p1
%patch1 -p1
%patch2 -p1


%install

install -D -m0755 %name.py %buildroot/%_bindir/%name
install -D -m0644 %{SOURCE2} %buildroot/%_liconsdir/%name.png
install -D -m0644 %{SOURCE1} %buildroot/%_iconsdir/hicolor/256x256/apps/%name.png

install -m 755 -d %buildroot/%_docdir/
tar zxf %{SOURCE3} -C %buildroot/%_docdir



### == desktop file
mkdir -p %buildroot%_desktopdir
cat>%buildroot%_desktopdir/%name.desktop<<END
[Desktop Entry]
Name=%name
GenericName=%name
Exec=%name
Icon=%name.png
Terminal=false
Type=Application
Categories=Development;Engineering;
END

%files
%_bindir/%name
%doc %_docdir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/*.png
%_iconsdir/hicolor/*/apps/*.png

%changelog
* Thu Jan 04 2024 Alexei Mezin <alexvm@altlinux.org> 0.13-alt1
- Initial build


