%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-saveforweb
Version: 0.29.3
Release: alt1

Summary: GIMP "Save for Web" plugin
License: LGPLv2+
Group: Graphics

Url: http://registry.gimp.org/node/33
Source: http://registry.gimp.org/files/gimp-save-for-web-%version.tar.bz2

Requires: gimp
# Automatically added by buildreq on Fri Feb 05 2010
BuildRequires: intltool libgimp-devel

%description
Save for Web allows to find compromise between minimal file size and acceptable
quality of image quickly. While adjusting various settings, you may explore how
image quality and file size change. Options to reduce file size of an image
include setting compression quality, number or colors, resizing, cropping, Exif
information removal, etc.

%prep
%setup -n gimp-save-for-web-%version

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang gimp20-save-for-web

%files -f gimp20-save-for-web.lang
%gimpplugindir/plug-ins/*
# Now only dummy template for help here, so exclude it...
%exclude %_datadir/gimp-save-for-web

%changelog
* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 0.29.3-alt1
- 0.29.3

* Fri Feb 05 2010 Victor Forsiuk <force@altlinux.org> 0.29.0-alt1
- 0.29.0

* Wed Sep 24 2008 Victor Forsyuk <force@altlinux.org> 0.28.6-alt1
- 0.28.6

* Wed Aug 20 2008 Victor Forsyuk <force@altlinux.org> 0.28.5-alt1
- Initial build.
