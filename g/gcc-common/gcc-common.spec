Name: gcc-common
Version: 1.4.22
Release: alt1

Summary: Common directories, symlinks and selection utility for the GNU Compiler Collection
License: GPL
Group: Development/C

Source1: gccbug.in
Source2: gcc_wrapper.c

Patch: gccbug-alt.patch

%define _libexecdir /usr/libexec

%ifarch ppc ppc64
# On powerpc, even though target is ppc32, compiler is inherently 64-bit,
# thus the wrapper should call ppc64-alt-linux-*.
%define _target_platform ppc64-alt-linux
%endif

%package -n gcc-c++-common
Summary: Common symlinks for the GNU C++ Compiler
License: GPL
Group: Development/C++
BuildArch: noarch
PreReq: %name = %version-%release

%package -n gcc-go-common
Summary: Common symlinks for the Go Compiler
License: GPL
Group: Development/Other
BuildArch: noarch
PreReq: %name = %version-%release

%package -n gcc-fortran-common
Summary: Common symlinks for the GNU Fortran Compiler
License: GPL
BuildArch: noarch
Group: Development/Other
PreReq: %name = %version-%release
Provides: gcc-g77-common = %version-%release
Obsoletes: gcc-g77-common
Conflicts: gcc2.95-g77 < 1:2.95.3-alt8
Conflicts: gcc2.96-g77 < 0:2.96-alt8
Conflicts: gcc3.3-g77 < 0:3.3.4-alt5
Conflicts: gcc3.4-g77 < 0:3.4.5-alt3

%package -n gcc-treelang-common
Summary: Common symlinks for the GNU Treelang Compiler
License: GPL
Group: Development/Other
BuildArch: noarch
PreReq: %name = %version-%release
Conflicts: gcc3.3-treelang < 0:3.3.4-alt5
Conflicts: gcc3.4-treelang < 0:3.4.5-alt3

%package -n gcc-gnat-common
Summary: Common symlinks for the GNU Ada compiler (GNAT)
License: GPL
Group: Development/Other
BuildArch: noarch
PreReq: %name = %version-%release
Conflicts: gcc4.7-gnat gcc4.6-gnat gcc4.5-gnat gcc4.4-gnat gcc4.3-gnat gcc4.2-gnat gcc4.1-gnat

%description
This package contains common symlinks, directories and selection
utility for the GNU Compiler Collection.

%description -n gcc-c++-common
This package contains common symlinks for the GNU C++ Compiler.

%description -n gcc-go-common
This package contains common symlinks for the Go Compiler.

%description -n gcc-fortran-common
This package contains common symlinks for the GNU Fortran 77 Compiler.

%description -n gcc-treelang-common
This package contains common symlinks for the GNU Treelang Compiler.

%description -n gcc-gnat-common
This package contains common symlinks for the GNU Ada compiler (GNAT).

%prep
%setup -cT
install -p -m755 %SOURCE1 gccbug
%patch -p1

%build
gcc %optflags -Werror '-DBINDIR="%_bindir"' \
	'-DTARGET="%_target_platform"' %_sourcedir/gcc_wrapper.c -o gcc_wrapper
sed -i 's|@TARGET@|%_target_platform|g' gccbug

%install
mkdir -p %buildroot{/lib,%_libdir/gcc{,-lib}/%_target_platform,%_libexecdir/gcc/%_target_platform,%_bindir,%_includedir/c++}
install -p -m755 gcc_wrapper %buildroot%_bindir/
install -p -m755 gccbug %buildroot%_bindir/%_target_platform-gccbug

ln -s gcc_wrapper %buildroot%_bindir/gcc

for n in cc cpp g++ gcc-{ar,nm,ranlib} gccgo gcov gfortran gnat gtreelang protoize unprotoize; do
	ln -s gcc "%buildroot%_bindir/$n"
done
for n in dump tool; do
	ln -s gcov "%buildroot%_bindir/gcov-$n"
done
for n in f77 f95 g77; do
	ln -s gfortran "%buildroot%_bindir/$n"
done
for n in gnatbind gnatchop gnatclean gnatfind gnatgcc gnatkr gnatlink gnatls gnatmake gnatname gnatprep gnatxref; do
	ln -s gnat "%buildroot%_bindir/$n"
done

ln -s ..%_bindir/cpp %buildroot/lib/cpp
ln -s g++ %buildroot%_bindir/c++
ln -s gtreelang %buildroot%_bindir/tree1
ln -s %_target_platform-gccbug %buildroot%_bindir/gccbug

%files
/lib/*
%_libdir/gcc*
%_libexecdir/gcc*
%_bindir/gcc_wrapper
%_bindir/cc
%_bindir/cpp
%_bindir/gcc
%_bindir/gcc-ar
%_bindir/gcc-nm
%_bindir/gcc-ranlib
%_bindir/gccbug
%_bindir/gcov
%_bindir/gcov-tool
%_bindir/gcov-dump
%_bindir/protoize
%_bindir/unprotoize
%_bindir/%_target_platform-gccbug

%files -n gcc-c++-common
%_bindir/c++
%_bindir/g++
%_includedir/c++

%files -n gcc-fortran-common
%_bindir/f77
%_bindir/f95
%_bindir/g77
%_bindir/gfortran

%files -n gcc-go-common
%_bindir/gccgo

%files -n gcc-treelang-common
%_bindir/gtreelang
%_bindir/tree1

%files -n gcc-gnat-common
%_bindir/gnat*

%changelog
* Wed Feb 21 2018 Dmitry V. Levin <ldv@altlinux.org> 1.4.22-alt1
- Dropped gcc-java-common and libgcj-common subpackages.
- gcc-common: dropped alternatives.

* Sun Feb 18 2018 Dmitry V. Levin <ldv@altlinux.org> 1.4.21-alt1
- gcc-common: added gcov-dump symlink.

* Fri May 22 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.20-alt1
- gcc-common: added gcov-tool symlink.

* Tue Apr 08 2014 Dmitry V. Levin <ldv@altlinux.org> 1.4.19-alt1
- gcc-common: added gcc-{ar,nm,ranlib} symlinks.

* Mon Feb 17 2014 Dmitry V. Levin <ldv@altlinux.org> 1.4.18-alt1
- Added gcc-gnat-common subpackage.

* Thu Nov 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.17-alt1
- gcc_wrapper:
  + cleanup (ldv@).
  + support GCC_TARGET environment variable.

* Wed Jan 09 2013 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt1
- libgcj-common: added /usr/share/java/ and /usr/share/java/gcj-endorsed/.
- Packaged gcc-{c++,fortran,go,java,treelang}-common as noarch subpackages.

* Tue Aug 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.15-alt1
- go compiler support added

* Fri Nov 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.14-alt1
- Switched to alternatives-0.4.

* Wed Oct 22 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt1
- gcc-java-common: Added more symlinks for better gcc4.3-java support.

* Thu Oct 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.12-alt1
- gcc-java-common: Replaced %_bindir/fastjar with fastjar requirement.

* Sat Jun 07 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.11-alt1
- gcc-common:
  + Do not package files packaged in libgcj-common (closes: #15854).
- gcc wrapper:
  + Do not strip "gcj-" prefix.
  + Recognize more names: tree1, g77, f95, jar, rmic, rmiregistry.
- Removed redundant %%_target_platform-* symlinks:
  gcc-common: cc;
  gcc-c++-common: c++;
  gcc-fortran-common: f77, g77, f95;
  gcc-treelang-common: tree1;
  gcc-java-common: jar.
- gcc-java-common:
  + Removed redundant symlinks: gcj-jar, gcj-rmic.
  + Removed rmiregistry symlink (closes: #15949).
  + Added gjar symlink.

* Sat Mar 22 2008 Alexey Tourbin <at@altlinux.ru> 1.4.10-alt3
- Updated dependencies.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt2
- Rebuilt.

* Sun Sep 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt1
- Updated java subpackage.

* Sat May 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt1
- Updated select-gcc script.

* Fri May 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.8-alt1
- Updated java subpackage.

* Mon May 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.7-alt1
- Renamed gcc-g77-common subpackage to gcc-fortran-common.
- Updated fortran, treelang and java subpackages.

* Mon Jan 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.6-alt1
- Converted alternatives config file to new format (0.2.0).

* Thu Dec 30 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- Added libgcj-common subpackage.

* Wed Dec 29 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.4-alt1
- Packaged new directories used by gcc >= 3.4:
  %_libdir/gcc/%_target_platform
  %_libexecdir/gcc/%_target_platform

* Fri Aug 13 2004 Stanislav Ievlev <inger@altlinux.org> 1.4.3-alt2
- ported to new alternatives

* Sun Mar 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- Changed following symlinks to use alternatives like gcc:
  cpp, gcj-*, gcjh, gcov, gij, grepjar, jcf-dump, jv-scan,
  protoize, rmiregistry, unprotoize.
- Updated wrapper to handle gcj-* symlinks.
- select-gcc: added treelang display support.

* Sun Mar 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- Renamed jar and rmic to resolve conflict with j2se-devel
  alternatives (bug #3739).

* Mon Feb 23 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- Updated wrapper to handle cc, c++, f77 symlinks (#3728).

* Sun Dec 28 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Moved symlinks for various frontends to separate subpackages
  (fixes #2733).

* Thu Dec 25 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt3
- Added config for gcc-3.3.

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt2
- Finalized alternatives transition.

* Thu Oct 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1.3-alt1.3
- port select-gcc to new alternatives

* Wed Oct 15 2003 Stanislav Ievlev <inger@altlinux.ru> 1.3-alt1.2
- second stage: change second alternatives layer

* Wed Oct 15 2003 Stanislav Ievlev <inger@altlinux.ru> 1.3-alt1.1
- first stage: added weight configs for compilers

* Sun Oct 05 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Fixed recent change.

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Implemented ccache support, see
  http://www.altlinux.ru/pipermail/devel/2003-September/014774.html
  for details.

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt4
- Removed c++filt, it's now provided by binutils.

* Wed May 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt3
- Workaround rpm bug with deps processing.

* Fri Nov 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt2
- Corrected dependencies:
  Conflicts: kaffe < 1.0.6-alt2, cpp = 0:2.96-ipl15mdk, cpp = 0:2.96-ipl16mdk

* Fri Nov 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Save gccbug via renaming it to %_target_platform-gccbug.
- Corrected dependencies:
  Conflicts: libgcj2.96 < 0:2.96-alt4

* Tue Nov 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Added symlinks:
  %_bindir/%%_target_platform-{cc,c++,f77};
  %_bindir/{cpp,gcov,protoize,unprotoize,c++filt,gcjh,gij,jcf-dump,jv-scan,grepjar,jar,rmic,rmiregistry}.
- Added gcc_wrapper, added alternatives for cpp,gcc,g+,g77,gcj to use it.
- Added gccbug to this package, based on gccbug.in from gcc-3.2.1.
- Changed select-gcc to work with new scheme.

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- select-gcc: fixed libstdc++.so support.

* Sat Aug 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- Use /bin/readlink.
- Use subst instead of perl for build.

* Fri Aug 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Added %_includedir/c++ directory.

* Mon Aug 12 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- select-gcc: fixed color* avoidance code.

* Sat Aug 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- select-gcc: rewritten to make use of new
  "update-alternatives --config" option.
- select-gcc: avoid changing alternatives pointing to /usr/bin/color*.

* Tue Dec 04 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0-alt2
- select-gcc: fixed forced selection method.
- Moved symlinks for lib/cpp, %_bindir/cc, %_bindir/c++,
  %_bindir/f77 to this package.

* Thu Nov 22 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0-alt1
- Initial revision.
