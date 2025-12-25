%define _unpackaged_files_terminate_build 1

%define appname org.cvfosammmm.Setzer

Name: setzer
Version: 66
Release: alt1

Summary: simple yet full-featured LaTeX editor
License: GPL-3.0-or-later
Group: Publishing
Url: https://github.com/cvfosammmm/setzer

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: libadwaita-gir
Requires: libgtk4-gir
Requires: libgtksourceview5-gir
Requires: libpango-gir
Requires: libpoppler-gir
Requires: libwebkitgtk6.0-gir
Requires: libportal-gir

# need l3backend-xetex.def, l3backend-pdftex.def, l3backend-luatex.def
Requires: texlive-dist
# tools, which are used in the sources
Requires: /usr/bin/xelatex
Requires: /usr/bin/pdflatex
Requires: /usr/bin/lualatex
Requires: /usr/bin/synctex
Requires: /usr/bin/latexmk
Requires: /usr/bin/makeindex
Requires: /usr/bin/biber
Requires: /usr/bin/bibtex
Requires: /usr/bin/inkscape
Requires: /usr/bin/file

BuildArch: noarch

%description
Setzer features shortcuts for many LaTeX elements and symbols, a document
creation wizard, a dark mode, a high screen to content ratio and a good
side-by-side PDF viewer.

%prep
%setup
sed -i "s|Categories=.*|Categories=GNOME;GTK;Office;Publishing;|" data/org.cvfosammmm.Setzer.desktop

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING README.md
%_bindir/setzer
%_desktopdir/%{appname}.desktop
%_man1dir/setzer.1.*
%python3_sitelibdir/setzer/
%dir %_datadir/Setzer
%_datadir/Setzer/*
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/mime/packages/%{appname}.mime.xml

%changelog
* Wed Dec 24 2025 Nikolay Strelkov <snk@altlinux.org> 66-alt1
- Initial build for Sisyphus
