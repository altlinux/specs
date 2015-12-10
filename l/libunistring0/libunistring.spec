Name: libunistring0
Version: 0.9.3
Release: alt4

Summary: GNU Unicode string library
License: LGPLv3+
Group: System/Legacy libraries
Url: http://www.gnu.org/software/libunistring/
%define srcname libunistring-%version
# ftp://ftp.gnu.org/gnu/libunistring/%srcname.tar.gz
Source: %srcname.tar
Provides: libunistring = %version-%release
Obsoletes: libunistring < %version-%release

%description
This portable C library implements Unicode string types in three
flavours: (UTF-8, UTF-16, UTF-32), together with functions for character
processing (names, classifications, properties) and functions for
string processing (iteration, formatted output, width, word breaks,
line breaks, normalization, case folding and regular expressions).

%prep
%setup -n %srcname

%build
# Disable printf_safe for a while,
# required to enforce build using system vfprintf().
subst --preserve 's/gl_printf_safe=yes/gl_printf_safe=/' \
	gnulib-m4/gnulib-comp.m4 configure
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS BUGS NEWS THANKS
%exclude %_docdir/libunistring/
%exclude %_libdir/*.so
%exclude %_includedir/*
%exclude %_infodir/*.info*

%changelog
* Thu Dec 10 2015 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt4
- Renamed: libunistring -> libunistring0.
- Group: System/Libraries -> System/Legacy libraries.

* Sat Apr 30 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt3
- Rebuilt for debuginfo.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt2
- Rebuilt for soname set-versions.

* Fri Jun 04 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt1
- Initial revision.
