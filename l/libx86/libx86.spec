Name: libx86
Version: 1.1
Release: alt9
Summary: a hardware-independent library for executing real-mode x86 code
Url: http://www.codon.org.uk/~mjg59/libx86/
License: BSD
Group: System/Libraries

Packager: Vladislav Zavjalov <slazav@altlinux.org>

Source: http://www.codon.org.uk/~mjg59/%name/downloads/%name-%version.tar
#.gz

%if_enabled static
BuildPreReq: glibc-devel-static
%endif

%description
It's often useful to be able to make real-mode x86 BIOS calls from userland.
lrmi provides a simple interface to this for x86 machines, but this doesn't help
on other platforms. libx86 provides the lrmi interface, but will also run on
platforms such as amd64 and alpha.

%package devel
Group: Development/C
Summary: Development files of %name
Requires: %name = %version-%release

%description devel
It's often useful to be able to make real-mode x86 BIOS calls from userland.
lrmi provides a simple interface to this for x86 machines, but this doesn't help
on other platforms. libx86 provides the lrmi interface, but will also run on
platforms such as amd64 and alpha.

This package contains the C headers and documentation required for building
programs based on %name.

%if_enabled static
%package static-devel
Group: Development/C
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description static-devel
It's often useful to be able to make real-mode x86 BIOS calls from userland.
lrmi provides a simple interface to this for x86 machines, but this doesn't help
on other platforms. libx86 provides the lrmi interface, but will also run on
platforms such as amd64 and alpha.

This package contains the static library required for statically linking
applications based on %name.

%endif #enabled static

%prep
%setup -q

%build
%ifarch %ix86
BACKEND=
%else
BACKEND=x86emu
%endif
%make_build BACKEND=$BACKEND

%install
%makeinstall DESTDIR=%buildroot LIBDIR=%_libdir

%files
%_libdir/*.so.*
%doc COPYRIGHT x86emu/LICENSE

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%if_enabled static
%files static-devel
%_libdir/*.a
%endif

%changelog
* Mon Oct 11 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt9
- spec: don't use make_install_std macro

* Thu Mar 25 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt8
- apply libx86-add-pkgconfig.patch from Fedora, thanks to lav@ (closes #23209)
- apply libx86-mmap-offset.patch from Fedora, thanks to lav@
- fix a bug introoduced by the libx86-mmap-offset.patch in non-x86emu build
  (zero offset in real mode must be separated from zero exit status of
  the LRMI_common_init())
- reshape the git-repository to keep all sources in the master branch

* Fri Sep 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt7
- fix build

* Fri Sep 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt6
- use BACKEND=x86emu for x86_64, BACKEND= for i586
- processor flags changed for new glibc-kernheaders (fix build on i586)
- fix warnings on i586 and x86_64 with BACKEND=x86emu

* Tue Sep 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt3
- change Packager
- remove %post(un)_ldconfig
- always use BACKEND=x86emu (fix i586 build)

* Thu Jul 17 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.1-alt2
- fixed x86_64 build

* Tue Jun 17 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.1-alt1
- initial package
- build static libs if only --enabled static
