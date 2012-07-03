%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-plugin-exif-browser
Version: 0.1.0
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: GIMP plugin that permits the user to view EXIF data from jpeg files
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/node/8839
Source:  http://registry.gimp.org/files/exif-browser.tar.gz

Requires: gimp >= 2.2
# Automatically added by buildreq on Fri Oct 17 2008
BuildRequires: libexif-devel libgimp-devel

%description
GIMP plugin that permits the user to view EXIF data from jpeg files.

%prep
%setup -n exif-browser

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%gimpplugindir/plug-ins/*
# Help and i18n files not packaged 'cause they just stubs now...

%changelog
* Fri Oct 17 2008 Victor Forsyuk <force@altlinux.org> 0.1.0-alt1
- Initial build.
