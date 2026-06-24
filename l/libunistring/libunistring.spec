%define sover 5

Name: libunistring
Version: 1.4.2
Release: alt1

Summary: GNU Unicode string library
License: GPL-2.0-or-later or LGPL-3.0-or-later
Group: System/Libraries
Url: http://www.gnu.org/software/libunistring/
# https://ftp.gnu.org/gnu/libunistring/libunistring-%version.tar.xz
Source: libunistring-%version.tar

%description
This portable C library implements Unicode string types in three
flavours: (UTF-8, UTF-16, UTF-32), together with functions for character
processing (names, classifications, properties) and functions for
string processing (iteration, formatted output, width, word breaks,
line breaks, normalization, case folding and regular expressions).

%package -n libunistring%sover
Group: System/Libraries
Summary: GNU Unicode string library

%description -n libunistring%sover
This portable C library implements Unicode string types in three
flavours: (UTF-8, UTF-16, UTF-32), together with functions for character
processing (names, classifications, properties) and functions for
string processing (iteration, formatted output, width, word breaks,
line breaks, normalization, case folding and regular expressions).

%package -n libunistring-devel
Summary: GNU Unicode string library development files
Group: Development/C
Requires: libunistring%sover = %EVR

%description -n libunistring-devel
This package contains development files for programs building with libunistring.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

# Relocate shared libraries from %%_libdir/ to /%%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
        ln -fnrs %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%check
%make_build -k check VERBOSE=1

%files -n libunistring%sover
/%_lib/*.so.%{sover}*
%doc AUTHORS BUGS NEWS THANKS
%exclude %_docdir/libunistring/libunistring*

%files -n libunistring-devel
%_libdir/*.so
%_includedir/*
%_infodir/*.info*

%changelog
* Wed Jun 17 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.2-alt1
- 0.9.10 -> 1.4.2.
- Fixed the License: tag (GPL-2.0-or-later or LGPL-3.0-or-later).

* Mon Dec 03 2018 Dmitry V. Levin <ldv@altlinux.org> 0.9.10-alt1
- 0.9.8 -> 0.9.10.
- Added %%check.

* Wed Jan 31 2018 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- 0.9.7 -> 0.9.8
- Move library %_libdir -> /%_lib (for libidn2)

* Sat Oct 28 2017 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt1
- 0.9.4 -> 0.9.7 (closes: #30746).

* Wed Dec 09 2015 Dmitry V. Levin <ldv@altlinux.org> 0.9.4-alt1
- Updated: 0.9.3 -> 0.9.4.
- Renamed: libunistring -> libunistring2.

* Sat Apr 30 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt3
- Rebuilt for debuginfo.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt2
- Rebuilt for soname set-versions.

* Fri Jun 04 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt1
- Initial revision.
