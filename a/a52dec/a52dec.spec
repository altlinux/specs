%define _name liba52

%def_disable static

Name: a52dec
Version: 0.7.4
Release: alt7

Summary: Library for decoding ATSC A/52 streams
Group: Sound
License: GPL
Url: http://%_name.sourceforge.net
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: %url/files/%name-%version.tar.gz
Requires: %_name = %version-%release

BuildPreReq: libtool_1.5

%if_enabled static
BuildRequires: glibc-devel-static
%endif

%description
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

a52dec is a test program for liba52. It decodes ATSC A/52 streams, and
also includes a demultiplexer for mpeg-1 and mpeg-2 program streams.

%package -n %_name
Summary: %_name shared libraries
Group: System/Libraries

%description -n %_name
This package contains shared version of %_name.

%package -n %_name-devel
Summary: %_name header files and development libraries
Group: Development/C
Requires: %_name = %version-%release

%description -n %_name-devel
Header files and development libraries for %_name.

%if_enabled static
%package -n %_name-devel-static
Summary: %_name static libraries
Group: Development/C
Requires: %_name-devel = %version-%release

%description -n %_name-devel-static
Static version of %_name libraries.
%endif

%prep
%setup

%build
%set_libtool_version 1.5
%add_optflags %optflags_shared

%autoreconf
%configure \
	--enable-shared \
	%{subst_enable static}

%make_build

%install
%makeinstall

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%_man1dir/*
%doc README ChangeLog AUTHORS HISTORY TODO

%files -n %_name
%_libdir/*.so.*

%files -n %_name-devel
%_includedir/*
%_libdir/*.so
%doc doc/%_name.txt

%if_enabled static
%files -n %_name-devel-static
%_libdir/*.a
%endif

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt7
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt6
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.7.4-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liba52
  * postun_ldconfig for liba52
  * postclean-05-filetriggers for spec file

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7.4-alt5
- Fixed #8639 (proper packaging of %%_bindir).
- Changed packager field.
- Disable static library build.

* Tue Oct 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7.4-alt4
- use libtool-1.5.
- use autoreconf.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt3
- use libtool-1.4
- do not package .la files.
- fix TEXTREL bug.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt2
- Rebuild with gcc-3.2. 

* Tue Aug 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Thu Apr 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.3-alt1
- First build for Sisyphus.
