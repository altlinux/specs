Name: libnotify1
Version: 0.6.0
Release: alt4
Summary: Desktop notification library
License: LGPLv2.1+
Group: System/Legacy libraries
URL: http://www.galago-project.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc libdbus-glib-devel libgtk+2-devel xmlto

%description
The library that allows applications post notifications on the desktop
in accordance to the proposed Desktop Notification Specification.

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure \
	--disable-gtk-doc \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%changelog
* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt4
- package as legacy library

* Fri Mar 18 2011 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt3
- libnotify.pc: moved libnotify deps from Requires to Requires.private

* Sun Mar 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt2
- rebuild for debuginfo

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 0.4.5-alt2
- Rebuilt for soname set-versions.

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 0.4.5-alt1
- 0.4.5

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.4.4-alt1
- 0.4.4

* Tue Jan 09 2007 Victor Forsyuk <force@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue Sep 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.2-alt1
- Rebuilt with GTK+ 0.10 to enable necessary functions
- Added libnotify-devel-doc package
- Buildreq

* Thu Jul 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.2-alt0.1
- Updated to 0.4.2
- Polished descriptions
- Spec cleanup

* Thu May 04 2006 Vital Khilko <vk@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Feb 02 2006 Vital Khilko <vk@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Sun Sep 17 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus

* Sun Sep 17 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
