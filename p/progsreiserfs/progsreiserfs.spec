%def_enable shared
%def_enable static
%def_enable nls

Name: progsreiserfs
Version: 0.3.0.5
Release: alt1.1

Summary: Programs needed for manipulating reiserfs partitions
License: %gpl2plus
Group: System/Configuration/Hardware

# Url: ftp://ftp.namesys.com/pub/libreiserfs/
Source: http://ftp.uni-kl.de/pub/linux/archlinux/other/progsreiserfs/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

Requires: lib%name = %version-%release

# Automatically added by buildreq on Mon May 25 2009
BuildRequires: gcc-c++ libuuid-devel

BuildRequires: rpm-build-licenses

%define lname lib%name

Summary(uk_UA.CP1251): Програми для маніпулювання розділами диску з reiserfs

%description
%name is a package that allows you to create, destroy, resize
and copy reiserfs filesystem.

%description -l uk_UA.CP1251
%name - пакет, який дозволє створювати, знищувати, змінювати
розмір та копіювати файлову систему reiserfs.

%if_enabled shared
%package -n %lname
Summary: Shared library for reiserfs utilities
Group: System/Libraries

%description -n %lname
This package includes the shared library needed to run
%lname-based software.
%endif

%package -n %lname-devel
Summary: Files required to compile software that uses %lname
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
This package includes the header files for %lname.

%if_enabled static
%package -n %lname-devel-static
Summary: Files required to compile statically linked software that uses %lname
Group: Development/C
Requires: %lname = %version-%release

%description -n %lname-devel-static
This package includes the libraries needed to statically link software
with %lname.
%endif

%prep
%setup

%build
%configure \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable nls} \
    --with-pic
%make_build
bzip2 --keep --best --force ChangeLog

%install
%make_install DESTDIR=%buildroot install
#mv %buildroot%_sbindir/{fsck.reiserfs,reiserfs.fsck}
mv %buildroot%_sbindir/{mkfs.reiserfs,reiserfs.mkfs}
mv %buildroot%_man8dir/{mkfs.reiserfs,reiserfs.mkfs}.8

%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif

%files -n %lname-devel
%{?_enable_shared:%_libdir/*.so}
%_includedir/*
%_datadir/aclocal/*

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%files
%doc AUTHORS ChangeLog.* NEWS README THANKS TODO
%_sbindir/*
%_man8dir/*

%changelog
* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3.0.5-alt1.1
- rebuild (with the help of girar-nmu utility)

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 0.3.0.5-alt1
- 0.3.0.5
  + no more fsck
  + no more doc/API
  + removed patches
- buildreq
- me as a (inappropriate) Packager: again

* Tue Aug 19 2008 Led <led@altlinux.ru> 0.3.0.4-alt3
- cleaned up spec
- cleaned up BuildRequires

* Thu Jan 19 2006 Led <led@altlinux.ru> 0.3.0.4-alt2
- added patch from Ubuntu
- added API to %lname-devel's docs
- fixed spec

* Thu Jan 19 2006 Led <led@altlinux.ru> 0.3.0.4-alt1
- new version
- enable lib%name-devel-static
- fix spec
- rename fsck.reiserfs to reiserfs.fsck and mkfs.reiserfs* to reiserfs.mkfs*
  (conflicts w/reiserfsprogs)
- build static library by default

* Fri Dec 26 2003 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.4
- removed *.la
- don't build static library by default

* Fri Nov 08 2002 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.3
- patch from Yury Umanets is applied
- moved libs to /lib (see alt0.2)
- not including /sbin/fsck.reiserfs (conflicts w/reiserfsprogs and a stub anyway)

* Thu Nov 07 2002 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.2
- moved utils from /usr/sbin to /sbin (#1057)

* Tue Oct 29 2002 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.1
- 0.3.0.3

* Wed Feb 20 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.7-alt1
* New version of the progsreiserfs

* Mon Feb 18 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.6-alt2
- Copyright information fixed.
- progsreiserfs.spec fixed.
- THANKS file added.
- NAMESYS-README added.

* Sun Feb 16 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.6-alt1
- New version of the progsreiserfs packed.

* Mon Feb 11 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.5-alt2
- Some progsreiserfs.spec fixes.

* Mon Feb 11 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.5-alt1
- Initial release
