# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _pkgdocdir %_docdir/%name-%version

Name: gspiceui
Version: 1.2.36
Release: alt1
Summary: A frontend to Spice circuit similators

Group: Engineering
License: GPL-2.0-or-later
Url: http://sourceforge.net/projects/gspiceui
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
#Source-url: http://downloads.sourceforge.net/%name/%name-v%version.tar.gz
Source1: %name.desktop
Source2: %name-32x32.xpm

BuildRequires: gcc-c++
BuildRequires: libwxGTK3.0-devel desktop-file-utils
Requires: ngspice geda-gnetlist geda-gschem geda-gattrib gnucap
#Requires: gwave

%description
GspiceUI is listed among the Fedora Electronic Lab (FEL) packages.

GNU Spice GUI is intended to provide a GUI to freely available
Spice electronic cicuit simulators eg.GnuCAP, Ng-Spice.
It uses gNetList to convert schematic files to net list files
and gWave to display simulation results.
gSchem is used as the schematic generation/viewing tool.

%prep
%setup

# fix PATH to doc
%__subst "s|/gspiceui/html|/doc/gspiceui-%version|" src/main/HelpTasks.cpp

#wrong-file-end-of-line-encoding
%__subst 's/\r//' lib/*/*.mod

#spurious-executable-perm
chmod 0644 lib/*/*.mod
chmod 0644 sch/*/*.sch

reldocdir=$(echo %_pkgdocdir | sed -e 's|^%prefix||')
%__subst "s|/share/gspiceui/html/gSpiceUI\.html|$reldocdir/gSpiceUI.html|g" src/main/HelpTasks.cpp

%__subst "s|/usr/X11R6/include|%_includedir/X11/|" src/Makefile

%build
%make_build CXXFLAGS="%optflags $(wx-config --cxxflags) -DNDEBUG" GSPICEUI_DBG=0 GSPICEUI_WXLIB=3.0

%install
install -d %buildroot%_bindir
install -pm 755 bin/%name %buildroot%_bindir/%name

install -d %buildroot%_man1dir/
install -pm 644 %name.1 %buildroot%_man1dir/%name.1

# Add/Manage desktop file
install -d %buildroot%_iconsdir/hicolor/32x32/apps
install -d %buildroot%_iconsdir/hicolor/48x48/apps
install -pm 0644 %SOURCE2 \
%buildroot%_iconsdir/hicolor/32x32/apps/%name.xpm
install -pm 0644 src/icons/%name-48x48.xpm \
%buildroot%_iconsdir/hicolor/48x48/apps/%name.xpm

desktop-file-install --vendor "" \
    --dir %buildroot%_desktopdir \
    %SOURCE1

# Adding gspiceui in the geda symbols directory structure

install -d %buildroot%_datadir/gEDA/sym/%name
cp -p lib/symbols/* %buildroot%_datadir/gEDA/sym/%name

# Creating a gafrc file which can automatically load those sym from the
# above directory structure
mkdir -p examples
cat > examples/gafrc << EOF
; gspiceui documentation symbols
(component-library "%_datadir/gEDA/sym/%name")
EOF

# Preparing examples
cp -pr lib/ examples
cp -pr sch/ examples

# Cleaning %%doc files
rm -f examples/*/Makefile
rm -rf examples/lib/sym

# Fix desktop entry categories
subst 's/^Categories=.*$/Categories=Science;Engineering;/' %buildroot%_desktopdir/%name.desktop

%files
%doc Authors License ReadMe ChangeLog ToDo
%doc examples html/*.html
%_bindir/%name
%_iconsdir/hicolor/??x??/apps/*.xpm
%_desktopdir/%name.desktop
%_man1dir/%name.1.*
%_datadir/gEDA/sym/%name

%changelog
* Wed Jun 03 2020 Anton Midyukov <antohami@altlinux.org> 1.2.36-alt1
- New version

* Sun Oct 28 2018 Anton Midyukov <antohami@altlinux.org> 1.1.00-alt1
- Initial build for ALT
