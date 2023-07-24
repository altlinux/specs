%define soname 1
%def_disable devel

Name: libpaper%soname
Version: 1.1.28
Release: alt4

Summary: Library and tools for handling papersize

License: GPL-2.0-only
Group: System/Legacy libraries
Url: http://packages.qa.debian.org/libp/libpaper.html

# Source-url: http://deb.debian.org/debian/pool/main/libp/libpaper/libpaper_%version.tar.gz
Source: %name-%version.tar

# Fedora's patches:
Patch1: libpaper-covscan.patch
Patch2: libpaper-file-leak.patch
Patch3: libpaper-useglibcfallback.patch

# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: gcc-c++ libstdc++-devel

%description
The paper library and accompanying files are intended to provide a simple
way for applications to take actions based on a system- or user-specified
paper size.  This release is quite minimal, its purpose being to provide
really basic functions (obtaining the system paper name and getting
the height and width of a given kond of paper) that applications can
immediately integrate.

%package -n libpaper
Summary: Library for handling papersize
Group: System/Legacy libraries
Provides: libpaper1 = %EVR
Obsoletes: libpaper1 < %EVR

%description -n libpaper
The paper library and accompanying files are intended to provide a simple
way for applications to take actions based on a system- or user-specified
paper size.  This release is quite minimal, its purpose being to provide
really basic functions (obtaining the system paper name and getting
the height and width of a given kond of paper) that applications can
immediately integrate.

This package contains the libpaper.so.1 library.

%if_enabled devel
%package devel
Summary: Header files for %name
Group: Development/Other
Requires: libpaper = %EVR

%description devel
Header files for %name library.
%endif

%prep
%setup
#patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure --disable-static
# Disable rpath
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la
mkdir -p %buildroot%_sysconfdir
echo '# Simply write the paper name. See papersize(5) for possible values' > %buildroot%_sysconfdir/papersize
mkdir -p %buildroot%_sysconfdir/libpaper.d
for i in cs da de es fr gl hu it ja nl pt_BR sv tr uk vi; do
    mkdir -p %buildroot%_datadir/locale/$i/LC_MESSAGES/;
    msgfmt debian/po/$i.po -o %buildroot%_datadir/locale/$i/LC_MESSAGES/%name.mo;
done
%find_lang %name

%if_disabled devel
rm -rv %buildroot%_libdir/libpaper.so
rm -rv %buildroot%_includedir/paper.h
rm -rv %buildroot%_man3dir/
%endif

# drop files (conflict with libpaper2)
rm -v %buildroot%_bindir/paperconf
rm -v %buildroot%_sbindir/paperconfig

%files -n libpaper -f %name.lang
%doc README
%config(noreplace) %_sysconfdir/papersize
%dir %_sysconfdir/libpaper.d
%_libdir/libpaper.so.*
%_man1dir/*
%_man5dir/*
%_man8dir/*

%if_enabled devel
%files devel
%_libdir/libpaper.so
%_includedir/paper.h
%_man3dir/*
%endif

%changelog
* Mon Jul 24 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.28-alt4
- NMU: libpaper: fixed the 'Obsoletes: libpaper1' tag introduced in the
  previous release to cover all possible versions of libpaper1.

* Mon Jul 24 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.28-alt3
- NMU:
  - Reverted the libpaper1 package name to libpaper to prevent an unnecessary
    relocation of the libpaper.so.1 soname provider.
  - libpaper: added Provides: libpaper1 and Obsoletes: libpaper1 because
    it has already been uploaded into the Sisyphus repository.
  - Fixed the License: tag (GPL -> GPL-2.0-only).
  - Fixed libpaper Group: tag (System/Libraries -> System/Legacy libraries).

* Wed Jul 19 2023 Mikhail Tergoev <fidel@altlinux.org> 1.1.28-alt2
- build as libpaper1
- drop devel package, paperconf and paperconfig

* Sat Oct 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.28-alt1
- new version 1.1.28 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version (1.1.26) with rpmgs script
- update all patches from Fedora project

* Wed Sep 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.24-alt4
- steal Fedora patches for proper papersize setting (ALT #26176)

* Mon Aug 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.24-alt3
- firsttime script added

* Mon Aug 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.24-alt2
- set paper to A4 if not set

* Fri Mar 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.24-alt1
- 1.1.24

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.23-alt1.qa2
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.23-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libpaper
  * postun_ldconfig for libpaper
  * postclean-05-filetriggers for spec file

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt1
- new version 1.1.23 (with rpmrb script)

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.21-alt0.1
- new version 1.1.21 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.20-alt0.1
- new version 1.1.20 (with rpmrb script)

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt0.1
- initial build for ALT Linux Sisyphus
