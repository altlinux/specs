%def_with cmake
%define major 1.8

Name: sword
Version: %major.1
Release: alt5

Summary: The SWORD Project framework for manipulating Bible texts
Summary(ru_RU.UTF-8): Проект SWORD - оболочка для работы с текстами Библии

License: GPL2
Url: http://www.crosswire.org/sword
Group: Databases

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source0: http://www.crosswire.org/download/ftpmirror.tmp/pub/sword/source/v1.5/%name-%version.tar.bz2
Source: http://www.crosswire.org/ftpmirror/pub/sword/source/v%major/%name-%version.tar
Source2: sword_icons.tar
Patch: https://src.fedoraproject.org/rpms/sword/raw/fddb031c123743bc8dc622d48e65a73727cc398f/f/sword-1.8.1-integer-types.diff

Requires: lib%name = %version

BuildRequires: bc cppunit-devel gcc-c++ glibc-devel libclucene-core-devel libcurl-devel libicu-devel zlib-devel

%if_with cmake
BuildRequires: cmake
%endif

# http://site.icu-project.org/download/61#TOC-Migration-Issues
%add_optflags -DU_USING_ICU_NAMESPACE=1

%description
The SWORD Project is an effort to create an ever expanding software package
for research and study of God and His Word.  The SWORD Framework
allows easy manipulation of Bible texts, commentaries, lexicons, dictionaries,
etc.  Many frontends are build using this framework.  An installed module
set may be shared between any frontend using the framework.

%package -n lib%name
Summary: Main library for sword
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with sword.

%package -n lib%name-devel
Summary: Include files for developing sword applications
Group: Development/C
Requires: lib%name = %version
Requires: libcurl-devel >= 7.10.5
Requires: zlib-devel

%description -n lib%name-devel
This package contains the headers that programmers
will need to develop applications which will use the SWORD Bible Framework.

%prep
%setup
%patch -p1

%ifarch %e2k
# mcst#4060
%add_optflags -std=gnu++11
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%if_with cmake
%cmake -DLIBSWORD_LIBRARY_TYPE=Shared \
       -DSWORD_BUILD_UTILITIES="Yes" \
       -DLIBSWORD_SOVERSION=%{major} \
       -DLIBDIR=%{_libdir} \
       -DSWORD_BUILD_TESTS=Yes
       #-DSWORD_BINDINGS="Python" \
       #-DSWORD_PYTHON_INSTALL_DIR="%{buildroot}%{_prefix}" \

%cmake_build
%else
%add_optflags -fpermissive -ftemplate-depth=100
%autoreconf
%configure --with-lucene --with-icu --with-curl --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build
%endif

%install
%if_with cmake
%cmakeinstall_std
%else
%makeinstall_std
pushd utilities
install -m755 mkfastmod mod2vpl vpl2mod %buildroot/%_bindir
popd
%endif

# TODO:
%check
make tests

%files
%_bindir/*
%_sysconfdir/sword.conf
%_datadir/%name/
%doc README AUTHORS NEWS ChangeLog
%doc samples doc/*.*

%files -n lib%name
%_libdir/lib%name.so.%major
#_libdir/%name/

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/*.pc

%changelog
* Mon Dec 30 2019 Ildar Mulyukov <ildar@altlinux.ru> 1.8.1-alt5
- fix ppc64le build (closes #37665)

* Fri May 24 2019 Michael Shigorin <mike@altlinux.org> 1.8.1-alt4
- fix build with lcc-1.23 on e2k

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt3
- rebuild with libicu63

* Fri Sep 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt2
- rebuild with libicu62

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)
- build with cmake, use soname instead version

* Wed May 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version (1.8.0) with rpmgs script (ALT bug #30670)

* Fri May 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.5a1-alt3
- rebuild with libicu60

* Mon Jul 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.5a1-alt2
- Fixed build with new toolchain
- Migrated to clucene-core

* Fri Feb 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.7.5a1-alt1
- new version 1.7.5a1 (with rpmrb script)
- cleanup build (drop obsoleted saphire files)
- this update resolves DataPath issue (ALT bug #31279)
- rebuild with libicu56

* Thu Jan 29 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script) (ALT bug #30670)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version 1.6.2 (with rpmrb script)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.0-alt3.qa5
- NMU: rebuilt with libicuuc.so.50.

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt3.qa4
- Fixed build with gcc 4.7

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt3.qa3
- Removed bad RPATH

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt3.qa2
- Rebuilt with new curl

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3.qa1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Mar 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt3
- rebuild with new libicu

* Sat Sep 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt2
- new version 1.6.0 (with rpmrb script)

* Sat May 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.11-alt2
- fix build with gcc 4.4

* Thu Jul 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.11-alt1
- new version 1.5.11 (with rpmrb script)

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.10-alt1
- new version 1.5.10 (with rpmrb script) - fix bug #13312

* Fri Mar 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.9-alt1
- build with lucene, icu
- update buildreq
- fix lib packaging, cleanup spec

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.9-alt0.1
- new version 1.5.9 (with rpmrb script)

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.8-alt1.1
- try again

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.8-alt1
- new version
- cleanup spec

* Sat Jan 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.7a-alt1
- new version
- build with gcc3.4

* Thu Jul 29 2004 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt1
- first build for Sisyphus

* Mon Dec 28 2003 Brook Humphrey <bah@linux-mandrake.com> 1.5.7-1mdk
- hopefully fixed build problems due to optimizations and mandrake 9.2

* Thu Nov 13 2003 Brook Humphrey <bah@linux-mandrake.com> 1.5.6-1mdk
- New build for sword 1.5.6
- diatheke installs cleanly so it is not needed to force a name change now.
- api docs removed from devel package because they are no longer distributed with the main package.
- may add api docs back later.
- fixed recursive requires for sword and libsword.
- fixed build to use optflags.
- fixed permission problems with include directory.

* Fri Apr 25 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.5.5-5mdk
- Buildrequire zlib-devel (thx slbd)

* Thu Apr 24 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.5.5-4mdk
- Don't provide name in libname package
- Bump release a bit more

* Thu Mar 13 2003 Buchan Milne <bgmilne@linux-mandrake.com> 1.5.5-2mdk
- cleanups
- ->contrib

* Fri Dec 13 2002 Brook Humphrey <bah@webmedic.net> sword-1.5.5-1mdk9.0_kde3.1
- Compiled for mandrake 9.0 using texstars 3.1rc5 rpm's they also have aafonts enabled.

* Wed Oct 9 2002 Brook Humphrey <bah@webmedic.net> sword-1.5.4-1mdk9.0
- Compiled for mandrake 9.0.
- This is current cvs as it wouldn't compile with gcc 3.2 before this.
- Fixed files as some of the files changed from 1.5.3.
- Most notably man is gone now for the api.

* Tue Feb 19 2002 Brook Humphrey <bah@webmedic.net> sword-1.5.3.pre-1mdk
- Compiled on mandrake 8.2
- first rpm of sword 1.5.3 pre
- removed chetah from build as it doesn't build proper
- added configure to sword build for proper build

* Sun Jan 27 2002 Brook Humphrey <bah@webmedic.net> sword-1.5.2-6mdk
- Added libsword1-static-devel package

* Tue Jul 10 2001 Brook Humphrey <bah@webmedic.net> sword-1.5.2-5mdk
- Updates to newest sources with bug fixes

* Fri Jun 22 2001 Brook Humphrey <bah@webmedic.net> sword-base-1.5.2-1mdk
- Added lib packages to be compliant with mandrake specs

* Mon Apr 30 2001 Brook Humphrey <bah@webmedic.net>
- added more mandrake macros for build
- removed apps for build cvs.20010430. They would not build

* Sun Apr 22 2001 Brook Humphrey <bah@webmedic.net>
- added man pages for api to package
- added html api doc to package

* Wed Mar 14 2001 Brook Humphrey <bah@webmedic.net>
- updated to use mandrake menu sysem

* Mon Feb 19 2001 Brook Humphrey <bah@webmedic.net>
- merged spec files from myself and Petr Kri'tof with this one
- added Petr Kri'tof's and my own comments to this changelog

* Sat Jan 20 2001 Stuart Gathman <stuart@bmsi.com>
- mkfastmod and other utilities

* Thu Nov 30 2000 Stuart Gathman <stuart@bmsi.com>
- cheatah application

* Mon Nov 20 2000 Brook Humphrey <bah@webmedic.net>
- added crypto to sword package
- updated to sword 1.5.1a

* Fri Nov 17 2000 Stuart Gathman <stuart@bmsi.com>
- initial release

* Fri Mar 17 2000 Petr Kri╧tof <Petr@Kristof.CZ>
- Sword 1.5.0 tree adaption

* Wed Mar 1 2000 Petr Kri╧tof <Petr@Kristof.CZ>
- Slovak descriptions added (Viera Valkova <ValkovaV@logica.com>)

* Tue Jan 4 2000 Brook Humphrey <bah@webmedic.net>
- Changed icon to sword.xpm

* Sun Jun 20 1999 Petr Kri╧tof <Petr@Kristof.CZ>
- Compliant with mods.d
