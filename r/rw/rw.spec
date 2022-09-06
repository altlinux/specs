%define soname 0

Name: rw
Version: 0.9
Release: alt2

Summary: Program that calculates rank-width and rank-decompositions
Summary(ru): Программа, вычисляющая ранговую ширину и декомпозицию рангов

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://sourceforge.net/projects/rankwidth/

Source: https://downloads.sourceforge.net/rankwidth/%name-%version.tar.gz
Patch: rw-0.9-alt-fix-build-with-igraph.patch

Provides: rankwidth = %version-%release

BuildRequires: gcc
BuildRequires: libigraph-devel

%description
rw is a program that calculates rank-width and rank-decompositions.
It is based on ideas from "Computing rank-width exactly" by Sang-il Oum,
"Sopra una formula numerica" by Ernesto Pascal, "Generation of a Vector
from the Lexicographical Index" by B.P. Buckles and M. Lybanon and
"Fast additions on masked integers" by Michael D. Adams and David S. Wise.

%description -l ru
rw - программа, вычисляющая ранговую ширину и декомпозицию рангов.
rw основана на идеях из «Computing rank-width exactly» Санг-иль Оума,
"Sopra una formula numerica" Эрнесто Паскаля, "Generation of a Vector
from the Lexicographical Index" Б.П. Баклза и М. Либанона и
«Fast additions on masked integers» Майкла Д. Адамса
и Дэвида С. Уайза.

%package -n lib%name%soname
Summary: Libraries for %name
Group: Sciences/Mathematics
Requires: %name = %version-%release

%description -n lib%name%soname
This package contains the libraries for %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Sciences/Mathematics

%description -n lib%name-devel
This package contains the header files for %name.

%prep
%setup
%patch -p1

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la

%files
%doc COPYING
%doc %_docdir/%name/
%_bindir/rw

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Tue Sep 06 2022 Leontiy Volodin <lvol@altlinux.org> 0.9-alt2
- Fix build with igraph 0.10.0.

* Fri Oct 22 2021 Leontiy Volodin <lvol@altlinux.org> 0.9-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
