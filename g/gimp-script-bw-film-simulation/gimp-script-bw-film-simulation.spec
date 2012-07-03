%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-script-bw-film-simulation
Version: 1.1
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Gimp script for B/W Film Simulation
License: GPLv2+
Group: Graphics

Url: http://serge.mankovski.com/photoblog/bw-film-simulation-in-gimp/
Source: http://serge.mankovski.com/photoblog/wp-content/uploads/BW-Film-Simulation-1-1.zip
# Fixes found in Debian:
Patch0: gimp-bw-film-simulation-mixerfix.patch
Patch1: gimp-bw-film-simulation-menu.patch

BuildArch: noarch
Requires: gimp >= 2.2

# Automatically added by buildreq on Tue Oct 07 2008
BuildRequires: libgimp-devel unzip

%description
Converts selected layer into Black and White using channel mixer. Uses channel
presets found on Internet and by all appearances resembling tonal qualities of
various films.

%prep
%setup -a 0 -c -T
%patch0 -p0
%patch1 -p0

%build

%install
install -d %buildroot%gimpdatadir/scripts
install -p -m644 *.scm %buildroot%gimpdatadir/scripts/

%files
%gimpdatadir/scripts/*

%changelog
* Tue Oct 07 2008 Victor Forsyuk <force@altlinux.org> 1.1-alt2
- Fix build with rpm that unzip sources without lowercasing filenames.
- Better location in gimp's menu structure.
- Fix bug in defining parameters for "50-50" and "Kodak HIE" film.

* Fri Sep 07 2007 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- Initial build.
