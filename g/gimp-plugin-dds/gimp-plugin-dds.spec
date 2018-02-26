%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-dds
Version: 2.0.9
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: GIMP plugin for working with images in DDS format
License: GPLv2+
Group: Graphics

Url: http://nifelheim.dyndns.org/~cocidius/dds/
Source: http://nifelheim.dyndns.org/~cocidius/files/gimp-dds-%version.tar.bz2

Requires: gimp >= 2.6
# Automatically added by buildreq on Fri Feb 26 2010
BuildRequires: libgimp-devel

%description
This is a plugin for GIMP that allows you to load and save images in DirectDraw
Surface (DDS) format.

%prep
%setup -n gimp-dds-%version

%build
%make_build CC="gcc %optflags"

%install
export DESTDIR=%buildroot
gimptool-2.0 --install-admin-bin dds

%files
%doc doc/gimp-dds.pdf README
%gimpplugindir/plug-ins/*

%changelog
* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 2.0.9-alt1
- 2.0.9

* Fri Feb 26 2010 Victor Forsiuk <force@altlinux.org> 2.0.8-alt1
- 2.0.8

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Tue Sep 02 2008 Victor Forsyuk <force@altlinux.org> 2.0.6-alt1
- Initial build.
