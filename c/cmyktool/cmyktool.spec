Name: cmyktool
Version: 0.1.5
Release: alt1

Summary: CMYK separation utility
License: GPLv3+
Group: Graphics

URL: http://www.blackfiveimaging.co.uk/index.php?article=02Software/05CMYKTool
Source: http://www.blackfiveimaging.co.uk/cmyktool/cmyktool-%version.tar.gz

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: gcc-c++ libgtk+2-devel libjpeg-devel liblcms-devel libnetpbm-devel libtiff-devel

# External program for devicelink: collink from argyllcms package
Requires: argyllcms
# Make use of gs utility (now in ghostscript-classic subpackage but is is safer
# not to rely on current ghostscript package splittiing, hence path requirement)
Requires: /usr/bin/gs

%description
CMYKTool is a new utility intended to build on the functionality of old CMYK separation plugin for the GIMP.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_liconsdir/*
%_desktopdir/*

%changelog
* Tue Jan 04 2011 Victor Forsiuk <force@altlinux.org> 0.1.5-alt1
- 0.1.5

* Tue Aug 17 2010 Victor Forsiuk <force@altlinux.org> 0.1.4a-alt1
- 0.1.4a

* Fri Jun 11 2010 Victor Forsiuk <force@altlinux.org> 0.1.3-alt1
- 0.1.3

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 0.1.2-alt1
- 0.1.2

* Wed Mar 03 2010 Victor Forsiuk <force@altlinux.org> 0.1.1-alt1
- Initial build.
