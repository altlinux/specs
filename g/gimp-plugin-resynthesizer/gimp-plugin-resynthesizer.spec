%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-plugin-resynthesizer
Version: 1.0
Release: alt1.1

Summary: Gimp plug-in for manipulating textures
License: GPLv3+
Group: Graphics

Url: https://github.com/bootchk/resynthesizer
#Original author's version was at http://logarithmic.net/pfh/resynthesizer
Source: bootchk-resynthesizer-0db24a9.tar.gz

Requires: gimp

# Automatically added by buildreq on Tue Apr 26 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel perl-XML-Parser pkg-config
BuildRequires: intltool libgimp-devel

%description
Resynthesizer is a Gimp plug-in that when given a sample of a texture can
synthesize more of that texture. It can also be used to create tiling patterns,
to remove an object from am image by inventing a plausable background, or to
apply a theme to an image (for example to make an image look as though it were
painted).

%prep
%setup -n bootchk-resynthesizer-0db24a9

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang resynthesizer

%files -f resynthesizer.lang
%gimpplugindir/plug-ins/*
%_datadir/resynthesizer

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Apr 26 2011 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0 (new upstream).

* Tue Oct 07 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt2
- Install all by hand due to broken gimp-2.6's gimptool.

* Fri Mar 28 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Mon Sep 17 2007 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- Initial build.
