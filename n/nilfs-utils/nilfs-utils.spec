%def_enable shared
%def_enable static
%def_with selinux
%def_with blkid
%def_with libmount
%define libdir /%_lib

%define bname nilfs
%define lname lib%bname

Name: %bname-utils
Version: 2.2.7
Release: alt1

Summary: Utilities for managing NILFS v2 filesystems
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.%bname.org
Source: http://www.%bname.org/download/%name-%version.tar
Patch: %name-%version-%release.patch

Provides: %{bname}2-utils = %version-%release
%{!?_disable_shared:Requires: %lname = %version-%release}

BuildRequires: libuuid-devel
%{?_with_blkid:BuildRequires: libblkid-devel}
%{?_with_libmount:BuildRequires: libmount-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}

%description
Utilities to work with NILFS v2 filesystems.

%if_enabled shared
%package -n %lname
Summary: NILFS v2 libraries
Group: System/Libraries
License: LGPLv2

%description -n %lname
This package contains shared code for %name and other utilities dealing
with NILFS v2 filesystems.
%endif

%package -n %lname-devel
Summary: NILFS v2 filesystem-specific headers
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release
License: LGPLv2

%description -n %lname-devel
This package contains the header files needed to develop NILFS v2
filesystem-specific programs.

%if_enabled static
%package -n %lname-devel-static
Summary: NILFS v2 static libraries
Group: Development/C
Requires: %lname-devel = %version-%release
License: LGPLv2+

%description -n %lname-devel-static
This package contains NILFS v2 static libraries.
%endif

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--libdir=%libdir \
	--sbindir=/sbin \
	--enable-largefile \
	%{subst_enable static} \
	%{subst_with blkid} \
	%{subst_with libmount} \
	%{subst_with selinux} \
	--with-gnu-ld
%make_build
gzip -9c ChangeLog > ChangeLog.gz

%install
%makeinstall_std
%if "%libdir" != "%_libdir"
install -dm755 %buildroot%_libdir
%if_enabled shared
for f in %buildroot%libdir/*.so; do
	ln -sf %libdir/$(readlink $f) %buildroot%_libdir/$(basename $f)
	rm -f $f
done
%endif
%{?_enable_static:mv %buildroot%libdir/*.a %buildroot%_libdir/}
%endif

%files
%doc AUTHORS ChangeLog.*
%config(noreplace) %_sysconfdir/%{bname}_cleanerd.conf
/sbin/*
%_sbindir/*
%_bindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*

%if_enabled shared
%files -n %lname
%libdir/*.so.*
%endif

%files -n %lname-devel
%{?_enable_shared:%_libdir/*.so}
%_includedir/*

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%changelog
* Thu Jan 18 2018 Michael Shigorin <mike@altlinux.org> 2.2.7-alt1
- 2.2.7
- minor spec cleanup

* Wed Apr 23 2014 Led <led@altlinux.ru> 2.2.0-alt2
- upstream fixes

* Wed Apr 09 2014 Led <led@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sat Feb 01 2014 Led <led@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Fri Oct 18 2013 Led <led@altlinux.ru> 2.1.5-alt2
- cleanerd: fix wrong cleaner speed of manual clean mode

* Sun Jul 14 2013 Led <led@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Thu Feb 14 2013 Led <led@altlinux.ru> 2.1.4-alt1
- 2.1.4
- fixed License for libraries
- enabled static libraries
- moved devel libraries to default %%_libdir

* Thu Jun 23 2011 Michael Shigorin <mike@altlinux.org> 2.0.23a-alt1
- retrofitted upstream commit to fix m4/ nanoissue
  (thx Ryusuke Konishi)

* Mon Jun 20 2011 Michael Shigorin <mike@altlinux.org> 2.0.23-alt2
- fix build (thx led@)

* Thu May 19 2011 Michael Shigorin <mike@altlinux.org> 2.0.23-alt1
- 2.0.23

* Tue Apr 05 2011 Michael Shigorin <mike@altlinux.org> 2.0.21-alt1
- 2.0.21 (closes: #25389)

* Sun Feb 21 2010 Michael Shigorin <mike@altlinux.org> 2.0.15-alt1
- 2.0.15 (trivial fixes)
- dropped the (upstream) patch

* Fri Nov 27 2009 Michael Shigorin <mike@altlinux.org> 2.0.14-alt2
- fixed FTBFS (updated buildrequires)
- minor spec cleanup

* Wed Nov 04 2009 Michael Shigorin <mike@altlinux.org> 2.0.14-alt1
- built for ALT Linux (starting off a fedora proposed package)
- considerable spec cleanup
- replaced patch/hacks with two upstream git commits

* Thu Jul 30 2009 Eric Sandeen <sandeen@redhat.com> 2.0.14-2
- Fix libuuid-devel dep, fix odd chown in make install

* Wed Jul 29 2009 Eric Sandeen <sandeen@redhat.com> 2.0.14-1
- New upstream release

* Wed Jun 10 2009 Eric Sandeen <sandeen@redhat.com> 2.0.12-1
- Initial fedora package

