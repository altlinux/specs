Summary: The simple LaTeX editor
Name: gummi
Version: 0.8.1
Release: alt1
License: MIT
Group: Development/Tools
Url: https://github.com/alexandervdm/gummi
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Nikita Ermakov <arei@altlinux.org>

BuildRequires: glib2-devel libgtk+3 libgtkspell3-devel libsynctex-devel libgtksourceview3-devel libpoppler-glib-devel gettext intltool

# For pdflatex.fmt
Requires: texlive-texmf

%description
The simple, graphical LaTeX editor based on GTK with spell checking and live
preview features.

%prep
%setup
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
* Mon Oct 26 2020 Nikita Ermakov <arei@altlinux.org> 0.8.1-alt1
- Initial build for ALT Sisyphus.
