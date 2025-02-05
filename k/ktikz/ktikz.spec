%define _unpackaged_files_terminate_build 1

Name:    ktikz
Version: 0.13.2
Release: alt1

Summary: Editor for the TikZ drawing language
License: GPL-2.0-or-later
Group:   Publishing
Url:     https://github.com/fhackenberger/ktikz

Source: %name-%version.tar

ExcludeArch: ppc64le
ExcludeArch: i586

BuildRequires(pre): rpm-build-kf5

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: libpoppler-qt5-devel

# Required for LaTeX render - pgf.sty, preview.sty, tikz.sty, pdflatex, pdftops
Requires: texlive-collection-basic
Requires: texlive-dist
Requires: texlive
Requires: poppler

# Required to display help
Requires: khelpcenter
Requires: kf6-kio

%description
KtikZ is a small application to assist in the creation of diagrams and
drawings using the TikZ macros from the LaTeX package "pgf". It consists
of a text editor pane in which the TikZ code for the drawing is edited
and a preview pane showing the drawing as rendered by LaTeX. The preview
pane can be updated in real-time. Common drawing tools, options and
styles are available from the menus to assist the coding process.

TikZ is a user-friendly syntax layer for the PGF (portable graphics
format) TeX macro package. Pictures can be created within a LaTeX
document and included in the output using the most important TeX backend
drivers including pdftex and dvips.

%prep
%setup

%build
%K5build

%install
%K5install
install -pDm 644 doc/%name.1 %buildroot%_man1dir/%name.1

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc Changelog HACKING LICENSE.FDL1.2 LICENSE.GPL2 README.md TODO examples
%_K5bin/%name
%_K5plug/%{name}part.so
%_K5xdgapp/%name.desktop
%_K5cfg/%name.kcfg
%_K5icon/hicolor/*/*/*
%_K5srv/ktikzpart.desktop
%dir %_K5xmlgui/%name
%_K5xmlgui/%name/*
%_K5xdgmime/%name.xml
%dir %_datadir/%name
%dir %_datadir/%name/locale
%_datadir/%name/locale/*
%dir %_datadir/%name/templates
%_datadir/%name/templates/*
%dir %_datadir/%{name}part
%_datadir/%{name}part/*
%_datadir/metainfo/%{name}.appdata.xml
%_man1dir/%name.*

%changelog
* Wed Feb 05 2025 Nikolay Strelkov <snk@altlinux.org> 0.13.2-alt1
- Initial build for Sisyphus
