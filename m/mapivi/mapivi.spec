Name: mapivi
Version: 0.9.7
Release: alt1

Summary: Feature-rich picture manager/organizer that supports IPTC metadata
License: GPL
Group: Graphics

Url: http://mapivi.sourceforge.net/mapivi.shtml
Source: http://downloads.sourceforge.net/mapivi/mapivi097.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Mar 06 2008 (-bi)
BuildRequires: perl-Image-Info perl-Image-MetaData-JPEG perl-Log-Agent perl-Storable perl-Tk perl-devel

%description

Mapivi is a cross-platform picture manager/organizer, viewer, and batch
processor. It is able to display and edit JPEG meta-information, including
IPTC/IIM information, EXIF data, and embedded comments. Pictures can be
organized by adding them to virtual folders (using hierarchical keywords).
It also serves as a frontend for performing lossless rotation, lossless
cropping, resizing, and filtering, and can display images as thumbnails.
It has a fast and powerful picture search feature that can search in all
picture meta-information.

%prep
%setup -n mapivi097

%build
%__subst 's/gimp-remote -n/gimp-remote/' mapivi
%__subst 's!$configdir/icons!%_datadir/mapivi/icons!' mapivi

%install
install -d -m755 %buildroot%_datadir/mapivi %buildroot%_bindir
cp -a . %buildroot%_datadir/mapivi

cat <<EOF >%buildroot%_bindir/mapivi
#!/bin/sh
exec %_datadir/mapivi/mapivi
EOF

chmod 755 %buildroot%_bindir/mapivi

%files
%_bindir/mapivi
%_datadir/mapivi

%changelog
* Thu Mar 06 2008 Victor Forsyuk <force@altlinux.org> 0.9.7-alt1
- 0.9.7

* Fri Apr 06 2007 Victor Forsyuk <force@altlinux.org> 0.9.1-alt1
- Initial build.
