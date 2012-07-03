%define udapl 1
#define static 1
%define thread 1

# Build examples package only once
%ifndef udapl
%ifndef thread
%define examples 1
%endif
%endif

%ifdef udapl
%define udaplpkg openmpi-udapl
%define udaplarg --with-udapl
%else
%define udaplpkg openmpi
%define udaplarg --without-udapl
%endif

%ifdef thread
%define threadpkg %udaplpkg-threads
%define threadarg --with-threads=posix --enable-mpi-threads --enable-progress-threads --enable-ft-thread
%else
%define threadpkg %udaplpkg
%define threadarg --without-threads --disable-ft-thread --disable-mpi-threads
%endif


%ifdef static
%define pkgname %threadpkg-static
%define staticarg --enable-static --disable-shared
%else
%define pkgname %threadpkg
%define staticarg --disable-static
%endif

%define arguments %udaplarg %threadarg %staticarg

Name: openmpi
#pkgname

Version: 1.6
Release: alt2

%define mpi_prefix %_libdir/%name
%define mpi_sysconfdir %_sysconfdir/%name

Summary: A powerful implementaion of MPI
Summary(ru_RU.UTF8): Открытая реализация MPI
License: BSD
Group: Development/Other
Url: http://www.open-mpi.org/

Packager: Denis Pynkin <dans@altlinux.ru>
Source:  openmpi-%version.tar
#Source1: MPI_Status_c2f.3

Patch0: openmpi-%version-%release.patch
#Patch1: openmpi-arm-%version.patch

BuildPreReq: rpm-macros-mpi-selector
Requires(post,preun): mpi-selector


%ifdef static
BuildPreReq: libibverbs-devel-static >= 1.1.2
%endif

%ifdef udapl
%ifdef static
BuildPreReq: libdapl-devel-static libstdc++-devel-static
%endif
Requires: libdapl >= 1.2.12
BuildPreReq: libdapl-devel
%endif

%ifdef thread
BuildPreReq: glibc-pthread
%endif

Requires: libibverbs >= 1.1.2
BuildPreReq: /proc flex gcc-c++ gcc-fortran
BuildPreReq: libibverbs-devel
BuildPreReq: valgrind-devel libiberty-devel


%package devel
Summary: Development part of %name
Group: Development/Other

Requires: %name = %version-%release
Requires: gcc-c++ gcc-fortran
Requires: libibverbs-devel libibumad-devel

%ifdef udapl
Requires: libdapl-devel
%endif

%package devel-vt
Summary: Development part of %name. VampirTrace related stuff.
Group: Development/Other

Requires: %name-devel = %version-%release
Requires: gcc-c++ gcc-fortran
Requires: libibverbs-devel libibumad-devel 

%ifdef examples
%package %name-examples
Summary: Generic examples for %name.
Group: Development/Other
BuildArch: noarch

%description %name-examples
Examples comming with upstream sources tarball.
%endif

%description
Open MPI is a project combining technologies and resources from
several other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in
order to build the best MPI library available. A completely new
MPI-2 compliant implementation, Open MPI offers advantages for
system and software vendors, application developers and computer
science researchers.

This part is attended for computing nodes.
#description -l ru_RU.KOI8-R

%description devel
Package for development with Open MPI 

%description devel-vt
Package for development with Open MPI and VampirTrace 

%prep
%setup -q -n openmpi-%version
#__cp -f SOURCE1 ompi/mpi/man/man3/
%patch0 -p1
#patch1 -p1

%build
CFLAGS+=" %optflags -D_FORTIFY_SOURCE=2"
CXXFLAGS+=" %optflags"
LDFLAGS+="-Wl,-R%mpi_prefix/lib/openmpi:%mpi_prefix/lib"
echo="/bin/echo"
export CFLAGS CXXFLAGS LDFLAGS echo

#autoreconf
sh autogen.sh

function buildIt() {
	./configure $* \
			--enable-mpi-f77 \
			--enable-mpi-f90 \
			--prefix=%mpi_prefix \
			--with-ft=cr \
			--sysconfdir=%mpi_sysconfdir \
			--bindir=%mpi_prefix/bin \
			--libdir=%mpi_prefix/lib \
			--datadir=%mpi_prefix/data \
			--includedir=%mpi_prefix/include \
			--mandir=%mpi_prefix/man \
			--docdir=%_docdir/%name-%version \
			--with-gnu-ld \
			--with-wrapper-ldflags="-Wl,--no-as-needed,-Rpath=%mpi_prefix/lib"

	%make_build
}

buildIt %arguments

%install
echo="/bin/echo"
export echo

%make_install DESTDIR=%buildroot install

#ln -s ompi-restart %buildroot%_libdir/%name/bin/orte-restart
#ln -s ompi-checkpoint %buildroot%_libdir/%name/bin/orte-checkpoint

# Avoid fail during man pages compression
rm -f %buildroot%_libdir/%name/man/man1/mpiCC.1
rm -f %buildroot%_libdir/%name/man/man1/orteCC.1

ln -s mpic++.1.gz %buildroot%_libdir/%name/man/man1/mpiCC.1.gz
ln -s mpic++.1.gz %buildroot%_libdir/%name/man/man1/orteCC.1.gz

%find_lang %name

echo -e "btl = tcp,self\n" >> %buildroot%mpi_sysconfdir/openmpi-mca-params.conf

cat>%buildroot/%mpi_prefix/bin/mpivars.sh<<EOF
if ! echo \$PATH | grep -q %mpi_prefix/bin ; then
    PATH=%mpi_prefix/bin:\$PATH
    export PATH
fi

if ! echo \$LD_LIBRARY_PATH | grep -q %mpi_prefix/lib ; then
    LD_LIBRARY_PATH=%mpi_prefix/lib\${LD_LIBRARY_PATH:+:\$LD_LIBRARY_PATH}
    export LD_LIBRARY_PATH
fi

if ! echo \$MANPATH | grep -q %mpi_prefix/man ; then
    MANPATH=%mpi_prefix/man:\$MANPATH
    export MANPATH
fi
EOF

cat >%buildroot%mpi_prefix/bin/mpivars.csh <<EOF
if (\$?path) then
    if ( "\${path}" !~ *%mpi_prefix/bin* ) then
	set path = ( %mpi_prefix/bin \$path )
    endif
else
    set path = ( %mpi_prefix/bin )
endif

if (\$?LD_LIBRARY_PATH) then
    if ( "\$LD_LIBRARY_PATH" !~ *%mpi_prefix/lib* ) then
	setenv LD_LIBRARY_PATH %mpi_prefix/lib:\$LD_LIBRARY_PATH
    endif
else
    setenv LD_LIBRARY_PATH %mpi_prefix/lib
endif

if (\$?MANPATH) then
    if ( "\$MANPATH" !~ *%mpi_prefix/man* ) then
	setenv MANPATH %mpi_prefix/man:\$MANPATH
    endif
else
    setenv MANPATH %mpi_prefix/man
endif
EOF

%post
%post_mpi_selector %name %mpi_prefix/bin

%preun
%preun_mpi_selector %name

%files -f %name.lang
%doc AUTHORS LICENSE NEWS README VERSION 

%dir %mpi_prefix

%dir %mpi_prefix/bin

%mpi_prefix/bin/mpivars.*
%mpi_prefix/bin/mpirun
%mpi_prefix/bin/ompi_info
%mpi_prefix/bin/opal_wrapper
%mpi_prefix/bin/orted
%mpi_prefix/bin/orterun
%mpi_prefix/bin/mpiexec

%mpi_prefix/bin/ompi-*
%mpi_prefix/bin/orte-*
%mpi_prefix/bin/opal-*

%dir %mpi_prefix/lib
%dir %mpi_prefix/lib/openmpi
%mpi_prefix/lib/openmpi/*.so

%ifdef static
%mpi_prefix/lib/lib*
%exclude %mpi_prefix/lib/libvt*
%else
%mpi_prefix/lib/lib*.so.*
%endif

%dir %mpi_sysconfdir
%config(noreplace) %mpi_sysconfdir/*

%dir %mpi_prefix/man
%mpi_prefix/man/man1
%mpi_prefix/man/man7
%mpi_prefix/data

%files devel
%mpi_prefix/bin/mpic++
%mpi_prefix/bin/mpicc
%mpi_prefix/bin/mpiCC
%mpi_prefix/bin/mpicxx
%mpi_prefix/bin/mpif77
%mpi_prefix/bin/mpif90
%mpi_prefix/bin/otf*

%mpi_prefix/bin/orte_wrapper_script
%mpi_prefix/bin/orteCC
%mpi_prefix/bin/ortec++
%mpi_prefix/bin/ortecc

%dir %mpi_prefix/include
%mpi_prefix/include/*.h
%dir %mpi_prefix/include/openmpi
%mpi_prefix/include/openmpi/*

%mpi_prefix/man/man3

%mpi_prefix/lib/mpi.mod

%mpi_prefix/lib/pkgconfig/*

%ifdef static
%mpi_prefix/lib/openmpi/*.a
%mpi_prefix/lib/libotf.a
%else
%exclude %mpi_prefix/lib/libvt*.so
%mpi_prefix/lib/lib*.so
%mpi_prefix/lib/*.la
%mpi_prefix/lib/openmpi/*.la
%endif

%files devel-vt
%mpi_prefix/bin/mpic++-vt
%mpi_prefix/bin/mpicc-vt
%mpi_prefix/bin/mpiCC-vt
%mpi_prefix/bin/mpicxx-vt
%mpi_prefix/bin/mpif77-vt
%mpi_prefix/bin/mpif90-vt
%mpi_prefix/bin/vt*
%mpi_prefix/lib/libvt*.so
%dir %mpi_prefix/include/vampirtrace
%mpi_prefix/include/vampirtrace/*

%ifdef examples
%files %name-examples
%doc examples
%endif

%changelog
* Mon Jun 25 2012 Denis Pynkin <dans@altlinux.org> 1.6-alt2
- Fixed overlapping with vt libraries

* Thu May 31 2012 Denis Pynkin <dans@altlinux.org> 1.6-alt1
- Version updated
- removed arm support added by sbolshakov due upstream support
- fixed default hostfile path
- enabled udapl and threads
- moved from %_libexecdir to %_libdir

* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.5-alt2
- arm support addded

* Wed Feb 15 2012 Denis Pynkin <dans@altlinux.org> 1.4.5-alt1
- New version

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt4.1
- Rebuilt for debuginfo

* Tue Jan 11 2011 Denis Pynkin <dans@altlinux.ru> 1.4.3-alt4
- fixed #24839

* Sat Nov 27 2010 Denis Pynkin <dans@altlinux.ru> 1.4.3-alt3
- Rebuild with gcc 4.5 - #24645

* Sun Oct 31 2010 Denis Pynkin <dans@altlinux.ru> 1.4.3-alt2
- All components moved to main package (thanks stanv@ for report)
- Include files for vampirtrace moved to corresponding package

* Sun Oct 10 2010 Denis Pynkin <dans@altlinux.ru> 1.4.3-alt1
- New version

* Thu Aug 26 2010 Denis Pynkin <dans@altlinux.ru> 1.4.2-alt2
- added examples package by Andriy Stepanov

* Tue May 11 2010 Denis Pynkin <dans@altlinux.ru> 1.4.2-alt1
- This release is mainly a bug fix release over the v1.4.1

* Fri Feb 19 2010 Denis Pynkin <dans@altlinux.ru> 1.4.1-alt1
- Security / bug fix release

* Wed Dec 09 2009 Denis Pynkin <dans@altlinux.ru> 1.4-alt1
- Stable version 1.4

* Mon Oct 26 2009 Denis Pynkin <dans@altlinux.ru> 1.3.3-alt3
- Fixed name for openmpi-threads

* Sun Oct 25 2009 Denis Pynkin <dans@altlinux.ru> 1.3.3-alt2
- changed build scheme - now we have different openmpi packages
  selected by variables 'udapl', 'thread' and 'static'

* Fri Jul 17 2009 Denis Pynkin <dans@altlinux.ru> 1.3.3-alt1
- new version from upstream
- bug fix release

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.1
- Add static libraries (NMU)

* Fri Apr 24 2009 Denis Pynkin <dans@altlinux.ru> 1.3.2-alt1
- new version from upstream

* Mon Apr 13 2009 Denis Pynkin <dans@altlinux.ru> 1.3.1-alt2
- fix for #19595 - realtime libraries moved into main package

* Fri Mar 27 2009 Denis Pynkin <dans@altlinux.ru> 1.3.1-alt1
- new version from upstream
- bad elf symbol resolved

* Sun Feb 01 2009 Denis Pynkin <dans@altlinux.ru> 1.3.0-alt2
- added libdapl-devel as requirement for devel package
- added -Rpath option by default for user-space programms

* Tue Jan 20 2009 Denis Pynkin <dans@altlinux.ru> 1.3.0-alt1
- This release contains many bug fixes, feature
  enhancements, and performance improvements over the v1.2 series,
  including (but not limited to):
  * MPI2.1 compliant
  * Valgrind support
  * Updated ROMIO to the version from MPICH2-1.0.7
  * Many other new runtime features
  * Numerous bug fixes
- enbled valgrind support
- enabled dynamic dlopen
- package devel-vt for VampirTrace features

* Wed Dec 17 2008 Denis Pynkin <dans@altlinux.ru> 1.2.8-alt2
- Disable "--as-needed" by default for user's programms
- Enable fortran-90 bindings

* Thu Oct 16 2008 Denis Pynkin <dans@altlinux.ru> 1.2.8-alt1
- New version.

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.6-alt1.M41.1
- fix udapl btl build 
- rebuild with OFED-1.3.1
- build for 4.1

* Thu Aug 28 2008 Denis Pynkin <dans@altlinux.ru> 1.2.7-alt1
- New version.

* Tue May 27 2008 Denis Pynkin <dans@altlinux.ru> 1.2.6-alt2
- Fixed subdirectories packaging violation

* Wed Apr 09 2008 Denis Pynkin <dans@altlinux.ru> 1.2.6-alt1
- New mainly bugfix version

* Wed Feb 06 2008 Denis Pynkin <dans@altlinux.ru> 1.2.5-alt3
- changed mpi_prefix to %_libexecdir

* Fri Feb 01 2008 Denis Pynkin <dans@altlinux.ru> 1.2.5-alt2
- added mpi-selector support by Stanislav Ievlev <inger@altlinux.org>

* Wed Jan 16 2008 Denis Pynkin <dans@altlinux.ru> 1.2.5-alt1
- New version.
- Many bug fixes.

* Mon Oct 01 2007 Denis Pynkin <dans@altlinux.ru> 1.2.4-alt2
- added autoreconf (tnx to Lost for advice)

* Wed Sep 26 2007 Denis Pynkin <dans@altlinux.ru> 1.2.4-alt1
- new version

* Fri Aug 24 2007 Denis Pynkin <dans@altlinux.ru> 1.2.3-alt4
- libdapl-devel to buildrequires by S.Ievlev's request
- auto test of infiniband card

* Thu Aug 23 2007 Denis Pynkin <dans@altlinux.ru> 1.2.3-alt3
- added libibverbs to buildrequires by S.Ievlev's request
- added /proc to buildrequires to build component linux:timer

* Tue Jun 26 2007 Denis Pynkin <dans@altlinux.ru> 1.2.3-alt2
- Added devel package
- Added openmpi-alt-as-needed.patch
- Fix of unresolved symbols

* Tue Jun 26 2007 Denis Pynkin <dans@altlinux.ru> 1.2.3-alt1
- This release is mainly a bug fix release over the v1.2.2
  release, but there are few minor new features.

* Thu May 17 2007 Denis Pynkin <dans@altlinux.ru> 1.2.2-alt1
- This release is mainly a bug fix release over the v1.2.1
  release, but there are few minor new features.

* Thu Apr 26 2007 Denis Pynkin <dans@altlinux.ru> 1.2.1-alt1
- This release is mainly a bug fix release over the
  v1.2 release, but there are few minor new features. 

* Thu Mar 22 2007 Denis Pynkin <dans@altlinux.ru> 1.2.0-alt1
- This release contains many bug fixes, feature
  enhancements, and performance improvements over the v1.1 series
- added echo variable for properly working libtool
- added --disable-dlopen in configuration
- taken ompi/mpi/man/man3/MPI_Status_c2f.3 from package 'lam'
  because of broken version in release

* Wed Mar 21 2007 Denis Pynkin <dans@altlinux.ru> 1.1.5-alt1
- Version 1.1.5 is expected (hoped) to be the last release in the v1.1 series

* Wed Jan 31 2007 Denis Pynkin <dans@altlinux.ru> 1.1.4-alt1
- The 1.1.4 release is what the 1.1.3 release should have been.

* Tue Jan 30 2007 Denis Pynkin <dans@altlinux.ru> 1.1.3-alt1
- This release is mainly a bug fix release over the 1.1.2 release.

* Tue Jan 02 2007 Denis Pynkin <dans@altlinux.ru> 1.1.2-alt2
- added /usr/share/openmpi/* to package

* Tue Dec 26 2006 Denis Pynkin <dans@altlinux.ru> 1.1.2-alt1
- Initial build for ALTLinux.

