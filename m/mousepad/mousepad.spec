Name: mousepad
Version: 0.3.0
Release: alt1

Summary: Mousepad - A simple text editor for Xfce
Summary (ru_RU.UTF-8): Простой текстовый редактор для Xfce
License: %gpl2plus
Group: Editors
Url: http://www.xfce.org
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
# For exo-csource
BuildRequires: libexo-devel
BuildRequires: libgtk+2-devel intltool libgtksourceview-devel libdbus-glib-devel

Obsoletes: xfce-mousepad < %version
Provides: xfce-mousepad = %version-%release

%description
Mousepad is a text editor for Xfce based on Leafpad. The initial reason
for Mousepad was to provide printing support, which would have been
difficult for Leafpad for various reasons.

%description -l ru_RU.UTF-8
Mousepad - простой текстовый редактор для Xfce основанный на Leafpad.
Одной из причин разработки нового редактора было предоставление
возможности печати, что было сложно реализуемо для редактора Leafpad
по некоторым причинам.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag mousepad_version_tag configure.ac.in

%build
%xfce4reconf
%configure --enable-dbus \
	--enable-maintainer-mode \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang mousepad

%files -f mousepad.lang
%doc NEWS README
%_bindir/*
%_desktopdir/*

%changelog
* Sat Jan 05 2013 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- From upstream git:
    + Set textdomain codeset to utf-8.
    + Fix desktop file.
    + Updated translations.
- Updated to 0.3.0.
- Renamed to mousepad.

* Wed Jun 09 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.99-alt2
- Fixed bug when the 'Undo' action works incorrectly with non-latin symbols.

* Sat May 22 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.99-alt1
- New development version.

* Mon May 17 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.16-alt2
- Added Debian patches for Mousepad.

* Mon May 17 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.16-alt1
- New version.

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.14-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for xfce-mousepad
  * postclean-05-filetriggers for spec file

* Sun Nov 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.14-alt1
- Xfce 4.4.3 release

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 0.2.13-alt1
- Xfce 4.4.2 release
- rename package
* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.12-alt0.1
- Xfce 4.4 release

* Fri Nov 10 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.10-alt2
- strict build requires libgtk+2-devel

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  0.2.10-alt1
- First version of RPM package for Sisyphus.
