Name: spatialite-gui
Version: 1.6.0
Release: alt2
Summary: GUI to manage Spatialite databases

Group: Databases
License: GPLv3+
Url: https://www.gaia-gis.it/fossil/spatialite_gui
Source0: http://www.gaia-gis.it/gaia-sins/spatialite_gui-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>

# Link geos_c
# Taken as a part from
# https://www.gaia-gis.it/fossil/spatialite_gui/ci/594d7d5a92?sbs=0
Patch0: %name-1.6.0-geos-c.patch

BuildRequires: desktop-file-utils
BuildRequires: freexl-devel
BuildRequires: libspatialite-devel
BuildRequires: libgaiagraphics-devel
BuildRequires: libwxGTK-devel
BuildRequires: sqlite-devel
BuildRequires: libgeos-devel
BuildRequires: libproj-devel gcc-c++ gcc

%description
GUI to manage Spatialite databases.

%prep
%setup -n spatialite_gui-%version

%patch0 -p1 -b .geos-c

# Delete shebang from desktop file
#TODO: Clarify
sed -i '1d' gnome_resource/%name.desktop

# Remove existing Makefiles
rm -f Makefile-static*

%build
%configure  \
        --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot

# Install icon and desktop file
# Mailed the author
mkdir -p %buildroot%_datadir/pixmaps
install -pm 0644 gnome_resource/%name.png %buildroot%_datadir/pixmaps

desktop-file-install                               \
    --dir=%buildroot%_datadir/applications         \
    gnome_resource/%name.desktop

%files
%doc COPYING AUTHORS
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Fri Feb 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Rebuild with new geos

* Sat Feb 02 2013 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- Build for Sisyphus

* Sun Jan  6 2013 Volker Frohlich <volker27@gmx.at> 1.6.0-1
- New upstream release
- Patch missing linking instruction

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> 1.5.0-5
- Rebuild for libspatialite soname bump

* Fri Jul  6 2012 Volker Frohlich <volker27@gmx.at> 1.5.0-2
- Add forgotten BR freexl-devel

* Wed Jan 11 2012 Volker Frohlich <volker27@gmx.at> 1.5.0-1
- Update for new release
- Update URL and source URL
- Correct license to GPLv3+
- Drop patch for wxwidget (solved)
- Use upstreams desktop file and icon
- Don't modify linker flags anymore (solved)

* Mon Jan  9 2012 Volker Frohlich <volker27@gmx.at> 1.4.0-3
- Exclude ppc64 architecture

* Sun Jan  8 2012 Volker Frohlich <volker27@gmx.at> 1.4.0-2
- Remove post and postun sections with useless ldconfig

* Sun Dec  4 2011 Volker Frohlich <volker27@gmx.at> 1.4.0-1
- Initial packaging
