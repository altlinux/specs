%define _unpackaged_files_terminate_build 1
%define pypi_name gResistor3
%define src_name gResistor

Name: gresistor3
Version: 3.2.5
Release: alt1
Summary: Identification resistors are usually marked with colored bands
License: LGPL
Group: Development/Python3
Url: https://pypi.org/project/%pypi_name
BuildArch: noarch
Source: %src_name-%version.tar
# Source-url: https://github.com/stethewwolf/gResistor/archive/refs/tags/%version.tar.gz

Patch: gresistor3-alt.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-gir
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(gi)
BuildRequires: typelib(Gtk) = 3.0
BuildRequires: python3(cairo)
BuildRequires: ImageMagick-tools
Requires: typelib(Gtk) = 3.0

%description
To allow for identification, resistors are usually marked with colored bands.
Often refered to as color codes, these markings are indicative of their
resistance, tolerance and temperature coefficient. gResistor helps you
translate resistor color codes into a readable value. All you have to do is
watch the colors on the resistor and then enter them in the program. As you
enter colours you'll see that the resistor value is changing accordingly.

%prep
%setup -n %src_name-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# fix install icons
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
        convert %buildroot%_iconsdir/eu.stethewwolf.gresistor.png -resize $x'x'$x %buildroot%_iconsdir/hicolor/$x'x'$x/apps/eu.stethewwolf.gresistor.png
done
rm %buildroot%_iconsdir/eu.stethewwolf.gresistor.png

%files
%doc README.*
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%src_name-%version.dist-info
%_datadir/gresistor
%_datadir/metainfo/eu.stethewwolf.gresistor.metainfo.xml
%_desktopdir/eu.stethewwolf.gresistor.desktop
%_iconsdir/hicolor/*/apps/eu.stethewwolf.gresistor.png

%changelog
* Sun May 14 2023 Anton Midyukov <antohami@altlinux.org> 3.2.5-alt1
- initial build
