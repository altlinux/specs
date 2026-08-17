%define _unpackaged_files_terminate_build 1

Summary: Simple LaTeX editor with live preview
Name: gummi
Version: 0.8.3
Release: alt1
License: MIT
Group: Publishing
Url: https://github.com/alexandervdm/gummi
Source: %name-%version.tar

# sync with version 0.8.3+really0.8.3-6 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: libgtk+3-devel
BuildRequires: libgtksourceview4-devel
BuildRequires: libpoppler-glib-devel
BuildRequires: libgtkspell3-devel
BuildRequires: libsynctex-devel

# For pdflatex.fmt
Requires: texlive-texmf
# For dvipdf
Requires: ghostscript-utils

%description
Gummi is a LaTeX editor based on GTK3.

The basic features are:
- Live preview pane for the compiled document,
- BibTeX integration,
- Helpers for tables and matrices,
- Exporting to PDF,
- Error checking,
- Syntax highlighting,
- Spellchecking,
- Document statistics,
- Persistent configuration.

%prep
%setup
sed -i "s|^Categories=.*|Categories=Office;Publishing;|" ./data/misc/gummi.desktop.in
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_man1dir/%name.1.xz

%changelog
* Mon Aug 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.3-alt1
- Fixed FTBFS.
- Spec cleanup.

* Mon Oct 26 2020 Nikita Ermakov <arei@altlinux.org> 0.8.1-alt1
- Initial build for ALT Sisyphus.
