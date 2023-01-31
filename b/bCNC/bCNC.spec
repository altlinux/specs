# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    bCNC
Version: 0.9.14.318
Release: alt3

Summary: GRBL CNC command sender, autoleveler and g-code editor
License: GPL-2.0
Group:   Engineering
URL:     https://github.com/vlachoudis/bCNC

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: ImageMagick-tools
%py3_requires tkinter serial

BuildArch: noarch

Source:  %name-%version.tar
# Source-url: https://files.pythonhosted.org/packages/source/b/%name/%name-%version.tar.gz

%add_python3_req_skip CNC CNCCanvas CNCList CNCRibbon Camera ControlPage EditorPage FilePage Helpers Pendant ProbePage Ribbon Sender TerminalPage ToolsPage Unicode Updates Utils _GenericController _GenericGRBL bFileDialog bmath bpath bstl dxf imageToGcode lib.log meshcut rexx spline svg_elements svgcode tkDialogs tkExtra undo log

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -r %buildroot%python3_sitelibdir/tests/

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

for i in 16 32 48 64 96 128; do
	mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps/
	convert bCNC/bCNC.png -resize "$i"x"$i" \
		%buildroot%_iconsdir/hicolor/"$i"x"$i"/apps/%name.png
done

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version.dist-info/
%doc *.md
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*.png

%changelog
* Tue Jan 31 2023 Anton Midyukov <antohami@altlinux.org> 0.9.14.318-alt3
- add %%py3_requires serial (Closes:45081)

* Tue Jan 31 2023 Anton Midyukov <antohami@altlinux.org> 0.9.14.318-alt2
- add %%py3_requires tkinter (Closes:45080)

* Sat Dec 17 2022 Anton Midyukov <antohami@altlinux.org> 0.9.14.318-alt1
- Initial build for Sisyphus
