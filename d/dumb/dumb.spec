Name: dumb
Version: 0.9.3
Release: alt3
Summary: IT, XM, S3M and MOD player library
Group: System/Libraries
License: zlib
Url: http://dumb.sourceforge.net/
Source0: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: http://downloads.sourceforge.net/%name/%name-%version-autotools.tar.gz
Source2: license-clarification.eml
Patch0: dumb-0.9.3-CVE-2006-3668.patch
Patch1: dumb-0.9.3-license-clarification.patch
Patch2: dumb-0.9.3-as-needed.patch
Packager: Fr. Br. George <george@altlinux.ru>
BuildRequires: liballegro-devel gcc-c++
Conflicts: dumb_0.9.2

%description
IT, XM, S3M and MOD player library. Mainly targeted for use with the allegro
game programming library, but it can be used without allegro. Faithful to the
original trackers, especially IT.

%package devel
Summary: Development libraries and headers for dumb
Group: Development/C
Requires: %name = %version
Requires: liballegro-devel
Conflicts: libdumb_0.9.2-devel

%description devel
The developmental files that must be installed in order to compile
applications which use dumb.

%prep
%setup -q -b 01
%patch0 -p1 -z .cve-2006-3668
%patch1 -p1
%patch2 -p0
cp %SOURCE2 .

%build
#touch INSTALL NEWS README AUTHORS ChangeLog COPYING
#autoreconf
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot
#clean out .la and static libs
rm -f %buildroot%_libdir/*.a %buildroot%_libdir/*.la
ln -s  lib%name-%version.so %buildroot%_libdir/lib%name.so.1
ln -s  libaldmb-%version.so %buildroot%_libdir/libaldmb.so.1

%files
%doc licence.txt release.txt readme.txt license-clarification.eml
%_bindir/dumb*
%_libdir/lib*-%version.so
%_libdir/lib*.so.1

%files devel
%doc docs/deprec.txt docs/dumb.txt docs/faq.txt docs/fnptr.txt docs/howto.txt docs/ptr.txt
%_includedir/*.h
%_libdir/libdumb.so
%_libdir/libaldmb.so

%changelog
* Tue Mar 22 2011 Fr. Br. George <george@altlinux.ru> 0.9.3-alt3
- Rebuild with allegro-4.4

* Tue Feb 19 2010 Fr. Br. George <george@altlinux.ru> 0.9.3-alt2
- veird soname workaround

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for dumb
  * postun_ldconfig for dumb
  * postclean-05-filetriggers for spec file

* Sun Feb 17 2008 Fr. Br. George <george@altlinux.ru> 0.9.3-alt1
- Initial build from FC8

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-6
- Clarify license after talking about it with upstream
- Include permission notice from upstream for license clarification
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-5
- FE6 Rebuild

* Thu Jul 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-4
- Fix CVE-2006-3668, thanks to Debian for the patch

* Wed Mar 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-3
- Add Requires: allegro-devel to -devel package

* Thu Mar 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-2
- Drop modplug.txt from %%doc and move release.txt and readme.txt from the
 -devel package to the main package (bz 185576).

* Fri Jan 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-1
- Initial Fedora Extras package
