%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define gimpdatadir %(gimptool-2.0 --gimpdatadir)
%define origname gimp-lqr-plugin

Name: gimp-plugin-lqr
Version: 0.7.0
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Liquid Rescale GIMP plugin
License: GPLv2+
Group: Graphics

Url: http://liquidrescale.wikidot.com
Source: %url/local--files/en:download-page-sources/%origname-%version.tar.bz2

# Automatically added by buildreq on Mon Jul 13 2009
BuildRequires: intltool libgimp-devel liblqr-devel

BuildRequires: liblqr-devel >= 0.4.1

Requires: gimp

%description
Liquid Rescale GIMP plugin aims at resizing pictures non uniformly while
preserving their features, i.e. avoiding distortion of the important parts. It
supports manual feature selection, and can also be used to remove portions of
the picture in a consistent way.

%prep
%setup -n %origname-%version

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang --output=%name.lang gimp20-lqr-plugin

%files -f %name.lang
%_datadir/gimp-lqr-plugin
%gimpplugindir/plug-ins/*
%gimpdatadir/scripts/*

%changelog
* Wed May 26 2010 Victor Forsiuk <force@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Jul 13 2009 Victor Forsyuk <force@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Nov 10 2008 Victor Forsyuk <force@altlinux.org> 0.5.1-alt1
- 0.5.1

* Mon Apr 07 2008 Victor Forsyuk <force@altlinux.org> 0.4.0-alt1
- 0.4.0-4

* Sat Oct 20 2007 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- 0.3.0-2

* Wed Oct 03 2007 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- built for ALT Linux
- thanks Andrey Novosyolov <ksynolog ukr net> for a tip
- spec partially based on gimp-plugin-wideangle.spec
