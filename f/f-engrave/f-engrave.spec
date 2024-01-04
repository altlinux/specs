Name:    f-engrave
Version: 1.75
Release: alt1

Summary: f-engrave is a text or image to g-code program for both engraving and v-carving
Summary(ru_RU.UTF8): f-engrave преобразует текст или изображение в управляющую программу для гравировки
License: GPL-3.0
Group:   Engineering
URL:     https://www.scorchworks.com/Fengrave/fengrave.html

BuildRequires(pre): rpm-build-python3
BuildRequires: hd2u
%py3_requires pyclipper tkinter

BuildArch: noarch

Source:  %name-%version.tar.gz
Source1: %name-256.png
Source2: %name-48.png
Source3: %name-docs.tar.gz
Patch0: fix_typo.patch
Patch1: fix_config.patch
Patch2: fix_python3.patch

%description
F-Engrave is a G-Code generator for Engraving and V-Carving.
Input can be text with a font (CXF or TTF font), image (bitmap, PNG etc.) or DXF data. Install
potran and ttf2cxf_stream packages for full functionality.

%description -l ru_RU.UTF8
F-Engrave это программа, которая преобразует надпись TTF/CXF шрифтом,
растровую картинку (bmp. png и т.п.) или чертеж DXF в управляющую программу для ЧПУ (G-Code). 
Установите пакеты potran и tttf2cxf_stream для полного функционала.



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

%files -n %name
%_bindir/%name
%doc %_docdir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu Jan 04 2024 Alexei Mezin <alexvm@altlinux.org> 1.75-alt1
- Initial build



