%define soname 4

Name: planarity
Summary: Implementations of several planarity-related graph algorithms
Version: 5.0.0.0
Release: alt1
License: BSD-3-Clause
Group: Sciences/Mathematics
Url: https://github.com/graph-algorithms/edge-addition-planarity-suite
VCS: https://github.com/graph-algorithms/edge-addition-planarity-suite

# Source-url: https://github.com/graph-algorithms/edge-addition-planarity-suite/archive/Version_%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc

%description
This code project provides a library for implementing graph algorithms
as well as implementations of several planarity-related graph algorithms.
The origin of this project is the reference implementation for the Edge
Addition Planarity Algorithm, which is now the fastest and simplest
linear-time method for planar graph embedding and planarity obstruction
isolation (i.e. Kuratowski subgraph isolation).

The software in this code project provides a graph algorithm framework and
library, including an updated version of the edge addition combinatorial
planar graph embedder and planar obstruction isolator (i.e., a Kuratowski
subgraph isolator). This code project also includes several extensions
that implement planarity-related algorithms such as a planar graph drawing
algorithm, an outerplanar graph embedder and outerplanar obstruction
isolator, and a number of subgraph homeomorphism search algorithms.

%package -n lib%name%soname
Summary: %summary
Group: System/Libraries

%description -n lib%name%soname
This code project provides a library for implementing graph algorithms
as well as implementations of several planarity-related graph algorithms.
The origin of this project is the reference implementation for the Edge
Addition Planarity Algorithm, which is now the fastest and simplest
linear-time method for planar graph embedding and planarity obstruction
isolation (i.e. Kuratowski subgraph isolation).

The software in this code project provides a graph algorithm framework and
library, including an updated version of the edge addition combinatorial
planar graph embedder and planar obstruction isolator (i.e., a Kuratowski
subgraph isolator). This code project also includes several extensions
that implement planarity-related algorithms such as a planar graph drawing
algorithm, an outerplanar graph embedder and outerplanar obstruction
isolator, and a number of subgraph homeomorphism search algorithms.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C

%description -n lib%name-devel
This package contains the header files and development documentation
for %name.

%prep
%setup -n edge-addition-%name-suite-Version_%version
%patch -p1

# Use unix line endings in installed headers and debugsource files
f=$(find ./c -name '*.c' -o -name '*.h')
for header in $f; do
    sed -i.orig 's|\r$||g' $header
    # Preserve timestamps
    touch -r $header.orig $header
    rm $header.orig
done

%build
# Generate the configure script
%autoreconf
%configure --enable-static=false

# Eliminate hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build

%install
%makeinstall_std

# We don't want the samples
rm -rf %buildroot%_docdir

%files
%doc LICENSE.TXT README.md
%_bindir/%name
%_man1dir/%name.1*

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/libplanarity.pc

%changelog
* Thu Jun 18 2026 Leontiy Volodin <lvol@altlinux.org> 5.0.0.0-alt1
- New version 5.0.0.0.

* Tue Oct 21 2025 Leontiy Volodin <lvol@altlinux.org> 4.0.1.0-alt1
- New version 4.0.1.0.

* Mon Mar 17 2025 Leontiy Volodin <lvol@altlinux.org> 4.0.0.0-alt1
- New version 4.0.0.0.
- Added vcs tag.

* Thu Mar 17 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.2.0-alt1
- New version (3.0.2.0).

* Thu Oct 21 2021 Leontiy Volodin <lvol@altlinux.org> 3.0.1.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
