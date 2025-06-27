%define _unpackaged_files_terminate_build 1

Name: nwg-readme-browser
Version: 0.1.7
Release: alt2

Summary: WebKitGTK-based README file browser
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/nwg-readme-browser

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: typelib(WebKit2)
Requires: typelib(GtkLayerShell)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Nwg-readme-browser was conceived as rtfm with a graphical user interface.
It searches the /usr/share/doc path for README.* files, and displays them
in WebKit2.WebView. It supports .md, .rst, .html and plain text. It does
not support .pdf format. Although the program was written with nwg-shell
for sway and Hyprland in mind, it may also be used standalone.

%prep
%setup -n %name-%version
%patch -p1
sed -i 's|^Categories=.*|Categories=Utility;Documentation;|' nwg-readme-browser.desktop

%build
%pyproject_build

%install
%pyproject_install

# installing additional files
install -Dm 644 %{name}.desktop %buildroot/%_desktopdir/%{name}.desktop
install -Dm 644 *.svg -t %buildroot/%_pixmapsdir/

%files
%doc LICENSE README.md nwg-readme-browser.svg
%python3_sitelibdir/nwg_readme_browser/
%python3_sitelibdir/%{pyproject_distinfo nwg_readme_browser}
%_bindir/*
%_desktopdir/%{name}.desktop
%_pixmapsdir/*

%changelog
* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.7-alt2
- Applied repocop fix for freedesktop-categories

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus
