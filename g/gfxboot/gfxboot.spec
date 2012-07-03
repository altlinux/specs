Name:         gfxboot
Version:      4.3.8
Release:      alt1

Group:        Development/Other
Summary:      Graphical boot logo for lilo, grub and syslinux.
License:      GPL

Source:       %name-%version.tar
Patch0:	      gfxboot-4.1.16-alt1.patch

# Automatically added by buildreq on Thu Jul 31 2008 (-bi)
BuildRequires: libfreetype-devel nasm xmlto 

BuildRequires: perl-HTML-Parser


%description
Here you find the graphical boot logo. Suitable for both lilo, grub and syslinux.

%prep
%setup -q
%patch0 -p1

%build
%make CFLAGS="%optflags -Wno-pointer-sign -fomit-frame-pointer -fno-stack-protector"
%make -C doc

%install
  mkdir -p $RPM_BUILD_ROOT/usr/sbin
  make install DESTDIR=$RPM_BUILD_ROOT THEMES=""
  install -d -m 755 $RPM_BUILD_ROOT/usr/share/gfxboot

%files
%doc changelog doc/gfxboot.html
%_sbindir/*
%_datadir/gfxboot/

%changelog
* Tue May 31 2011 Sergey V Turchin <zerg@altlinux.org> 4.3.8-alt1
- new version

* Thu May 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.1.47-alt1
- new version

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 4.1.16-alt1
- new version

* Wed Oct 08 2008 Anton Farygin <rider@altlinux.ru> 4.1.6-alt2
- build requires updates

* Tue Oct 07 2008 Anton Farygin <rider@altlinux.ru> 4.1.6-alt1
- new version

* Thu Jul 31 2008 Anton Farygin <rider@altlinux.ru> 4.0.14-alt1
- new version
- gfxboot tools moved to %_sbindir (by mainstream)

* Thu Apr 19 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.18-alt2
- build doc

* Fri Dec 08 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.18-alt1
- new version

* Thu Dec 23 2004 Anton Farygin <rider@altlinux.ru> 2.5-alt2
- moved to %_bindir

* Tue Nov 30 2004 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version

* Thu Sep 16 2004 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version

* Mon Feb 10 2003 Rider <rider@altlinux.ru> 1.9-alt2
- move theme files to package design-bootloader-<theme name>

* Tue Feb 04 2003 Rider <rider@altlinux.ru> 1.9-alt1
- first build for ALT Linux, based on SuSE spec and graphics
