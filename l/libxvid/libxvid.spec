%define bname xvid
%define Name XviD

Name: lib%bname
Version: 1.3.2
Release: alt1
Summary: Shared library of %Name video codec
Group: System/Libraries
License: GPLv2+
URL: http://www.%bname.org

Provides: %bname = %version-%release
Obsoletes: %bname < %version-%release

# http://downloads.xvid.org/downloads/%{bname}core-%version.tar.gz
Source: %{bname}core-%version.tar

%ifarch %ix86 x86_64
BuildRequires: nasm
%set_verify_elf_method textrel=relaxed
%endif

%description
%Name is a high performance and high quality MPEG-4 video de-/encoding
solution.
This package includes the shared library needed to run %Name software.

%package devel
Summary: Development files of %Name video codec
Group: Development/C
Requires: %name = %version-%release
Provides: %bname-devel = %version-%release
Obsoletes: %bname-devel < %version-%release

%description devel
%Name is a high performance and high quality MPEG-4 video de-/encoding
solution.
This package includes the header files needed to develop %Name-based
software.

%prep
%setup -q -n %{bname}core-%version

%build
pushd build/generic
%configure
%make_build
popd

%install
pushd build/generic
%make DESTDIR=%buildroot install
popd

ln -s %{name}core.so.4.3 %buildroot%_libdir/%{name}core.so
rm -f %buildroot%_libdir/*.a

%files
%doc AUTHORS README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed May 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Wed May 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Thu Feb 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt4
- rebuild

* Wed Oct 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt3
- x86_64: enabled asm (closes: #19684)

* Wed Oct 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt2
- ix86: reenabled asm (closes: #19684)

* Sun Sep 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Apr 19 2009 Led <led@altlinux.ru> 1.2.1-alt2
- replaced yasm with nasm in BuildRequires (Closes: #19684)

* Sun Dec 28 2008 Led <led@altlinux.ru> 1.2.1-alt1
- 1.2.1
- cleaned up spec

* Sat Oct 11 2008 Led <led@altlinux.ru> 1.1.3-alt3
- fixed License
- cleaned up spec

* Fri Aug 10 2007 Led <led@altlinux.ru> 1.1.3-alt2
- cleaned up BuildRequires
- used yasm for x86_32

* Fri Jul 06 2007 Led <led@altlinux.ru> 1.1.3-alt1
- 1.1.3 bugfix release:
  + fixed a potential vulnerability in mbcoding.c
- cleaned up spec

* Fri Dec 01 2006 Led <led@altlinux.ru> 1.1.2-alt1
- 1.1.2 (bugfix release)
- removed %{name}core-1.1.1-quotes.patch (fixed in upstream)

* Tue Oct 31 2006 Led <led@altlinux.ru> 1.1.1-alt1
- 1.1.1 (bugfix release)
- cleaned up spec
- added %{name}core-1.1.1-quotes.patch

* Fri Jul 28 2006 Led <led@altlinux.ru> 1.1.0-alt7
- added ability build shared or static or both libraries (with
  %{name}core-1.1.0-shared_static.patch)

* Thu Jul 06 2006 Led <led@altlinux.ru> 1.1.0-alt6
- fixed %%post and %%postun

* Tue May 16 2006 Led <led@altlinux.ru> 1.1.0-alt5
- rebuild with gcc-4.1
- fixed spec
- moved ChangeLog* to lib%name-devel
- added lib%name-examples package
- added LICENSE into lib%name

* Wed Apr 05 2006 Led <led@altlinux.ru> 1.1.0-alt4
- changed asm BuildRequires

* Tue Feb 28 2006 Led <led@altlinux.ru> 1.1.0-alt3
- added %{name}core-1.1.0-configure.patch (for detect pentium4)
- fix spec

* Mon Feb 27 2006 Led <led@altlinux.ru> 1.1.0-alt2
- enabled assembly for all arches

* Wed Feb 01 2006 Led <led@altlinux.ru> 1.1.0-alt1
- uk and ru Summary and description
- fix spec

* Tue Jan 31 2006 Led <led@altlinux.ru> 1.1.0-alt0.4
- fix spec

* Mon Jan 30 2006 Led <led@altlinux.ru> 1.1.0-alt0.3
- 1.1.0 release
- rename packages
- fix BuildRequires for x86_64

* Fri Oct 07 2005 Led <led@linux.kiev.ua> 1.1.0-alt0.2
- 1.1.0-beta2

* Tue Jul 05 2005 Led <led@linux.kiev.ua> 1.1.0-alt0.1
- 1.1.0-beta1
- update alt-makefile patch

* Wed Dec 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Nov 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Jun 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Mar 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt0.5rc3
- 1.0.0-rc3

* Sun Feb 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt0.5rc1
- 1.0.0-rc1

* Sat Nov 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1.1
- fix TEXTREL bug.

* Sun Aug 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Mon Apr 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sun Dec 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Fri Sep 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 0-alt0.6cvs20020822
- lastest snapshot built

* Fri May 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 0-alt0.5cvs120020412
- Adopted for Sisyphus PLD Team package.
