Name: libunistring2
Version: 0.9.10
Release: alt1

Summary: GNU Unicode string library
License: GPLV2+ or LGPLv3+
Group: System/Libraries
Url: http://www.gnu.org/software/libunistring/
%define srcname libunistring-%version
# https://ftp.gnu.org/gnu/libunistring/%srcname.tar.xz
Source: %srcname.tar
%def_disable static
Provides: libunistring = %version-%release

%description
This portable C library implements Unicode string types in three
flavours: (UTF-8, UTF-16, UTF-32), together with functions for character
processing (names, classifications, properties) and functions for
string processing (iteration, formatted output, width, word breaks,
line breaks, normalization, case folding and regular expressions).

%package -n libunistring-devel
Summary: GNU Unicode string library development files
Group: Development/C
Requires: %name = %version-%release

%description -n libunistring-devel
This package contains development files for programs building with libunistring.

%prep
%setup -n %srcname

# Disable printf_safe for a while,
# required to enforce build using system vfprintf().
subst --preserve 's/gl_printf_safe=yes/gl_printf_safe=/' \
	gnulib-m4/gnulib-comp.m4 configure

# Taken from gnulib.
grep -lZ '^test_.*@LIBMULTITHREAD@' tests/Makefile.* |
        xargs -r0 sed -i '/^test_.*@LIBMULTITHREAD@/ s/@LIBMULTITHREAD@/-Wl,--push-state,--no-as-needed,-lpthread,--pop-state/' --

%build
%configure %{subst_enable static}
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

%files
/%_lib/*.so.*
%doc AUTHORS BUGS NEWS THANKS
%exclude %_docdir/libunistring/libunistring*

%files -n libunistring-devel
%_libdir/*.so
%_includedir/*
%_infodir/*.info*
%if_enabled static
%_libdir/*.a
%endif

%changelog
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
