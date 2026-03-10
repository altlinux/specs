%define soname 19
%define oname sleuthkit

Name: libtsk%soname
Version: 4.12.1
Release: alt2

Summary: Shared library of The Sleuth Kit (legacy)

License: GPL
Group: System/Legacy libraries
Url: http://www.sleuthkit.org/sleuthkit/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-%version/sleuthkit-%version.tar.gz
Source: %name-%version.tar
# https://github.com/sleuthkit/sleuthkit/issues/642
Patch: sleuthkit-adapt-for-new-libewf.diff

BuildRequires: gcc-c++ glibc-devel libaff-devel libewf-devel zlib-devel

%description
Legacy shared library libtsk.so.19 for backward compatibility.
Use libtsk23 for new development.

%prep
%setup -q
%patch -p2
find -name Makefile.am | xargs subst "s| -static||g"

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
# Keep only the library
rm -rf %buildroot%_bindir
rm -rf %buildroot%_includedir
rm -f %buildroot%_libdir/*.so
rm -rf %buildroot%_libdir/pkgconfig
rm -rf %buildroot%_man1dir
rm -rf %buildroot%_datadir/tsk

%files
%_libdir/libtsk.so.%soname
%_libdir/libtsk.so.%soname.*

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 4.12.1-alt2
- rebuild as legacy libtsk19 (soname 19) per Shared Libs Policy

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 4.12.1-alt1
- new version 4.12.1 (with rpmrb script)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 4.12.0-alt1
- new version 4.12.0 (with rpmrb script)

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 4.11.1-alt1
- new version 4.11.1 (with rpmrb script)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 4.11.0-alt1
- new version 4.11.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.10.2-alt1
- new version 4.10.2 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 4.10.1-alt1
- new version 4.10.1 (with rpmrb script)

* Mon Sep 16 2019 Grigory Ustinov <grenka@altlinux.org> 4.6.7-alt2
- NMU: Rebuild with new libewf with a patch.

* Sat Sep 07 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6.7-alt1
- new version 4.6.7 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6.6-alt1
- new version 4.6.6 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6.5-alt1
- new version 4.6.5 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 4.6.2-alt1
- new version 4.6.2 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 4.6.0-alt1
- new version 4.6.0 (with rpmrb script)

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt1
- new version 4.5.0 (with rpmrb script)

* Thu Dec 07 2017 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt2
- drop BR:bouncycastle-tsp

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt1
- new version 4.4.2 (with rpmrb script)

* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 4.4.0-alt1
- new version 4.4.0 (with rpmrb script)

* Sun Dec 25 2016 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- new version (4.3.0) with rpmgs script

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- new version 4.2.0 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 4.1.3-alt1
- new version 4.1.3 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt1
- Version 3.2.3

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtsk
  * postun_ldconfig for libtsk
  * postclean-05-filetriggers for spec file

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- fix rpath problem on i586

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.09-4mdv2009.0
+ Revision: 260795
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.09-3mdv2009.0
+ Revision: 252599
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.09-1mdv2008.1
+ Revision: 136503
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.09-1mdv2008.0
+ Revision: 81984
- 2.09
- unbundle file, afflib and libewf

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 2.05-2mdv2008.0
+ Revision: 76894
- rebuild

* Sat Jul 29 2006 Oden Eriksson <oeriksson@mandriva.com> 2.05-1mdv2007.0
- 2.05
- fix deps

* Wed Oct 19 2005 Nicolas L�cureuil <neoclust@mandriva.org> 2.03-1mdk
- New release 2.03
- %%mkrel

* Sun Dec 26 2004 Stefan van der Eijk <stefan@mandrake.org> 1.73-1mdk
- 1.73
- rediffed p0

* Thu Nov 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.72-2mdk
- fix #12488

* Sun Oct 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.72-1mdk
- 1.72
- fix P0

* Wed Sep 01 2004 Stefan van der Eijk <stefan@mandrake.org> 1.71-1mdk
- 1.71

* Thu May 06 2004 Michael Scherer <misc@mandrake.org> 1.69-1mdk
- New release 1.69
- rpmbuildupdate aware
- update patch
- [DIRM]

