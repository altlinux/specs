%define _unpackaged_files_terminate_build 1

%def_with check

Name: typstwriter
Version: 0.3
Release: alt1

Summary: An integrated editor for the typst typesetting system.
License: MIT
Group: Editors
URL: https://github.com/Bzero/typstwriter

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel 
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(flit_core)

%if_with check
BuildRequires: python3-module-qtpy
BuildRequires: python3-module-pyside6
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-qt
%endif

Requires: /usr/bin/typst
Requires: python3-module-qtpy
Requires: python3-module-pyside6
Requires: python3-module-Pygments
Requires: python3-module-platformdirs

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

# install icon and desktop file
install -m644 -D typstwriter/icons/typstwriter.svg %buildroot%_iconsdir/hicolor/scalable/apps/%{name}.svg

mkdir -p %buildroot/%_desktopdir/
cat <<EOF > %buildroot/%_desktopdir/%{name}.desktop
[Desktop Entry]
Version=1.0
Name=Typstwriter
Categories=Office;WordProcessor;
Exec=/usr/bin/typstwriter %F
Type=Application
Icon=typstwriter
Keywords=Text;Editor;
EOF

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md docs/
%_bindir/%name
%_iconsdir/hicolor/scalable/apps/%{name}.svg
%_desktopdir/%{name}.desktop
%python3_sitelibdir/%name/
%dir %python3_sitelibdir/%{name}-*.dist-info/
%python3_sitelibdir/%{name}-*.dist-info/*

%changelog
* Wed Sep 17 2025 Nikolay Strelkov <snk@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
