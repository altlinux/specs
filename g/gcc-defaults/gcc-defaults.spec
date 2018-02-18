%set_compress_method none

%define gcc_version 7
%define psuffix -%gcc_version

%define gnat_arches		%ix86 x86_64
%define go_arches		%ix86 x86_64
%define libasan_arches		%ix86 x86_64 %arm aarch64
%define libatomic_arches	%ix86 x86_64 %arm aarch64 mips mipsel s390x
%define libcilkrts_arches	%ix86 x86_64
%define libitm_arches		%ix86 x86_64 %arm aarch64 s390x
%define liblsan_arches		x86_64 aarch64
%define libmpx_arches		%ix86 x86_64
%define libquadmath_arches	%ix86 x86_64
%define libtsan_arches		x86_64 aarch64
%define libubsan_arches		%ix86 x86_64 %arm aarch64
%define libvtv_arches		%ix86 x86_64

Name: gcc-defaults
Version: %gcc_version
Release: alt4
License: None
Group: Development/Other

Summary: %vendor GNU Compiler Collection Setup

%define gcc_target_platform %_target_platform

%description
This package contains default %vendor
GNU Compiler Collection Setup.

%package -n cpp
Summary: Dependency package for GNU C preprocessor
Group: Development/C
Requires: cpp%gcc_version
Conflicts: cpp3.4 < 3.4.5-alt18
Conflicts: cpp4.1 < 4.1.2-alt13
Conflicts: cpp4.3 < 4.3.2-alt21
Conflicts: cpp4.4 < 4.4.7-alt5
Conflicts: cpp4.5 < 4.5.4-alt5
Conflicts: cpp4.6 < 4.6.3-alt12
Conflicts: cpp4.7 < 4.7.2-alt11
Conflicts: cpp4.8 < 4.8.2-alt6
Conflicts: cpp4.9 < 4.9.2-alt6
Conflicts: cpp5 < 5.3.1-alt5
Conflicts: cpp6 < 6.3.1-alt3

%description -n cpp
This is metapackage for the default GNU C preprocessor.

%package -n gcc
Summary: Dependency package for GNU C compiler
Group: Development/C
Requires: cpp = %EVR
Requires: gcc%gcc_version
Conflicts: gcc3.4 < 3.4.5-alt18
Conflicts: gcc4.1 < 4.1.2-alt13
Conflicts: gcc4.3 < 4.3.2-alt21
Conflicts: gcc4.4 < 4.4.7-alt5
Conflicts: gcc4.5 < 4.5.4-alt5
Conflicts: gcc4.6 < 4.6.3-alt12
Conflicts: gcc4.7 < 4.7.2-alt11
Conflicts: gcc4.8 < 4.8.2-alt6
Conflicts: gcc4.9 < 4.9.2-alt6
Conflicts: gcc5 < 5.3.1-alt5
Conflicts: gcc6 < 6.3.1-alt3

%description -n gcc
This is metapackage for the default GNU C compiler.

%package -n gcc-c++
Summary: Dependency package for GNU C++ compiler
Group: Development/C
Requires: gcc = %EVR
Requires: gcc%gcc_version-c++
Conflicts: gcc3.4-c++ < 3.4.5-alt18
Conflicts: gcc4.1-c++ < 4.1.2-alt13
Conflicts: gcc4.3-c++ < 4.3.2-alt21
Conflicts: gcc4.4-c++ < 4.4.7-alt5
Conflicts: gcc4.5-c++ < 4.5.4-alt5
Conflicts: gcc4.6-c++ < 4.6.3-alt12
Conflicts: gcc4.7-c++ < 4.7.2-alt11
Conflicts: gcc4.8-c++ < 4.8.2-alt6
Conflicts: gcc4.9-c++ < 4.9.2-alt6
Conflicts: gcc5-c++ < 5.3.1-alt5
Conflicts: gcc6-c++ < 6.3.1-alt3

%description -n gcc-c++
This is metapackage for the default GNU C++ compiler.

%package -n gcc-fortran
Summary: Dependency package for GNU Fortran compiler
Group: Development/C
Provides: gcc-g77 = %EVR
Requires: gcc = %EVR
Requires: gcc%gcc_version-fortran
Conflicts: gcc4.1-fortran < 4.1.2-alt13
Conflicts: gcc4.3-fortran < 4.3.2-alt21
Conflicts: gcc4.4-fortran < 4.4.7-alt5
Conflicts: gcc4.5-fortran < 4.5.4-alt5
Conflicts: gcc4.6-fortran < 4.6.3-alt12
Conflicts: gcc4.7-fortran < 4.7.2-alt11
Conflicts: gcc4.8-fortran < 4.8.2-alt6
Conflicts: gcc4.9-fortran < 4.9.2-alt6
Conflicts: gcc5-fortran < 5.3.1-alt5
Conflicts: gcc6-fortran < 6.3.1-alt3

%description -n gcc-fortran
This is metapackage for the default GNU Fortran compiler.

%package -n gcc-go
Summary: Dependency package for GNU Go compiler
Group: Development/C
Requires: gcc = %EVR
Requires: gcc%gcc_version-go
Conflicts: gcc4.7-go < 4.7.2-alt11
Conflicts: gcc4.8-go < 4.8.2-alt6
Conflicts: gcc4.9-go < 4.9.2-alt6
Conflicts: gcc5-go < 5.3.1-alt5
Conflicts: gcc6-go < 6.3.1-alt3

%description -n gcc-go
This is metapackage for the default GNU Go compiler.

%package -n gcc-gnat
Summary: Dependency package for GNU Ada compiler
Group: Development/C
Requires: gcc = %EVR
Requires: gcc%gcc_version-gnat
Conflicts: gcc4.1-gnat < 4.1.2-alt13
Conflicts: gcc4.3-gnat < 4.3.2-alt21
Conflicts: gcc4.4-gnat < 4.4.7-alt5
Conflicts: gcc4.5-gnat < 4.5.4-alt5
Conflicts: gcc4.6-gnat < 4.6.3-alt12
Conflicts: gcc4.7-gnat < 4.7.2-alt11
Conflicts: gcc4.8-gnat < 4.8.2-alt6
Conflicts: gcc4.9-gnat < 4.9.2-alt6
Conflicts: gcc5-gnat < 5.3.1-alt5
Conflicts: gcc6-gnat < 6.3.1-alt3

%description -n gcc-gnat
This is metapackage for the default GNU Ada compiler.

%global do_package() \
%if 0%{3} \
%package -n %{1}-%{2} \
Summary: Dependency package for %{1}-%{2} \
Group: Development/C \
Requires: %{1}%gcc_version-%{2}\
%{4}BuildArch: noarch \
%description -n %{1}-%{2} \
This is metapackage for %{1}-%{2}. \
%endif

# noarch
%do_package gcc doc 1 %nil
%do_package gcc locales 1 %nil
%do_package gcc objc 1 %nil
%do_package gcc objc++ 1 %nil
%do_package gcc plugin-devel 1 %nil
%do_package libgccjit devel 1 %nil
%do_package libgfortran devel 1 %nil
%do_package libgfortran devel-static 1 %nil
%do_package libgomp devel 1 %nil
%do_package libgomp devel-static 1 %nil
%do_package libobjc devel 1 %nil
%do_package libobjc devel-static 1 %nil
%do_package libstdc++ devel 1 %nil
%do_package libstdc++ devel-static 1 %nil

# arch
%do_package libasan devel-static 1 #
%do_package libatomic devel-static 1 #
%do_package libcilkrts devel 1 #
%do_package libcilkrts devel-static 1 #
%do_package libgnat devel 1 #
%do_package libgnat devel-static 1 #
%do_package libitm devel-static 1 #
%do_package liblsan devel-static 1 #
%do_package libmpx devel-static 1 #
%do_package libquadmath devel 1 #
%do_package libtsan devel-static 1 #
%do_package libubsan devel-static 1 #
%do_package libvtv devel-static 1 #

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir

ln_bin()
{
	for i; do
		ln -s %_target_platform-"$i"%psuffix \
			%buildroot%_bindir/%_target_platform-"$i"
	done
}

ln_man()
{
	for i; do
		ln -s "$i"%psuffix.1.xz %buildroot%_man1dir/"$i".1.xz
	done
}

# cpp
ln_bin cpp
ln_man cpp

# gcc
ln_bin gcc
ln_man gcc

ln_bin gcc-{ar,nm,ranlib}

ln_bin gcov{,-tool,-dump}
ln_man gcov{,-tool,-dump}

# gcc-c++
ln_bin g++
ln_man g++

# gcc-fortran
ln_bin gfortran
ln_man gfortran

%ifarch %go_arches
ln_bin gccgo
ln_man gccgo
%endif

%ifarch %gnat_arches
ln_bin gnat gnatbind gnatchop gnatclean gnatfind gnatkr gnatlink gnatls \
	gnatmake gnatname gnatprep gnatxref
%endif

%files -n cpp
%_bindir/%_target_platform-cpp
%_man1dir/cpp.1.xz

%files -n gcc
%_bindir/%_target_platform-gcc
%_man1dir/gcc.1.xz

%_bindir/%_target_platform-gcc-ar
%_bindir/%_target_platform-gcc-nm
%_bindir/%_target_platform-gcc-ranlib

%_bindir/%_target_platform-gcov
%_man1dir/gcov.1.xz

%_bindir/%_target_platform-gcov-tool
%_man1dir/gcov-tool.1.xz

%_bindir/%_target_platform-gcov-dump
%_man1dir/gcov-dump.1.xz

%files -n gcc-c++
%_bindir/%_target_platform-g++
%_man1dir/g++.1.xz

%files -n gcc-fortran
%_bindir/%_target_platform-gfortran
%_man1dir/gfortran.1.xz

%ifarch %go_arches
%files -n gcc-go
%_bindir/%_target_platform-gccgo
%_man1dir/gccgo.1.xz
%endif

%ifarch %gnat_arches
%files -n gcc-gnat
%_bindir/%_target_platform-gnat*
%files -n libgnat-devel
%files -n libgnat-devel-static
%endif

%files -n gcc-doc
%files -n gcc-locales
%files -n gcc-objc
%files -n gcc-objc++
%files -n gcc-plugin-devel
%files -n libgccjit-devel
%files -n libgfortran-devel
%files -n libgfortran-devel-static
%files -n libgomp-devel
%files -n libgomp-devel-static
%files -n libobjc-devel
%files -n libobjc-devel-static
%files -n libstdc++-devel
%files -n libstdc++-devel-static
%ifarch %libasan_arches
%files -n libasan-devel-static
%endif
%ifarch %libatomic_arches
%files -n libatomic-devel-static
%endif
%ifarch %libcilkrts_arches
%files -n libcilkrts-devel
%files -n libcilkrts-devel-static
%endif
%ifarch %libitm_arches
%files -n libitm-devel-static
%endif
%ifarch %liblsan_arches
%files -n liblsan-devel-static
%endif
%ifarch %libmpx_arches
%files -n libmpx-devel-static
%endif
%ifarch %libquadmath_arches
%files -n libquadmath-devel
%endif
%ifarch %libtsan_arches
%files -n libtsan-devel-static
%endif
%ifarch %libubsan_arches
%files -n libubsan-devel-static
%endif
%ifarch %libvtv_arches
%files -n libvtv-devel-static
%endif

%changelog
* Sun Feb 18 2018 Dmitry V. Levin <ldv@altlinux.org> 7-alt4
- aarch64: packaged liblsan-devel-static and libtsan-devel-static.

* Sat Feb 17 2018 Dmitry V. Levin <ldv@altlinux.org> 7-alt3
- Upgraded Conflicts tags.

* Sat Feb 17 2018 Dmitry V. Levin <ldv@altlinux.org> 7-alt2
- gcc-fortran: provide gcc-g77.
- Fixed conditional packaging of subpackages.
- Fixed symlinks.
- Made arch-agnostic dependency packages noarch.

* Wed Jan 17 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 7-alt1
- Initial build.
