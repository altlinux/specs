Name: tango-icon-theme-extras
Version: 0.1.0
Release: alt1.qa1

Summary: Tango Icon Theme Extras
License: Creative Commons Attribution Share-Alike license 2.5
Group: Graphical desktop/Other
Url: http://tango.freedesktop.org/Tango_Desktop_Project

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: tango-icon-theme

# added by icesik@
BuildPreReq: libImageMagick-devel

# Automatically added by buildreq on Mon Apr 23 2007 (-bb)
BuildRequires: icon-naming-utils ImageMagick 

%description
This is an extension to the Tango Icon Theme. Currently it includes Tango
icons for iPod Digital Audio Player (DAP) devices and the Dell Pocket DJ DAP.
Tango Icon Theme Extras depends on the Tango Icon Theme.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog README
%_datadir/icons/Tango/

%changelog
* Wed Sep 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * deprecated-packages-info-i18n-common for tango-icon-theme-extras
  * postclean-05-filetriggers for spec file

* Wed Apr 18 2007 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt1
- build for Sisyphus

