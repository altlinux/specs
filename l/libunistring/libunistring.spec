Name: libunistring
Version: 0.9.3
Release: alt3

Summary: GNU Unicode string library
License: LGPLv3+
Group: System/Libraries
Url: http://www.gnu.org/software/libunistring/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar
%def_disable static

%description
This portable C library implements Unicode string types in three
flavours: (UTF-8, UTF-16, UTF-32), together with functions for character
processing (names, classifications, properties) and functions for
string processing (iteration, formatted output, width, word breaks,
line breaks, normalization, case folding and regular expressions).

%package devel
Summary: GNU Unicode string library development files
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for programs building with libunistring.

%prep
%setup

%build
# Disable printf_safe for a while,
# required to enforce build using system vfprintf().
sed -i 's/gl_printf_safe=yes/gl_printf_safe=/' \
	gnulib-m4/gnulib-comp.m4 configure
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS BUGS NEWS THANKS
%exclude %_docdir/%name/%{name}*

%files devel
%_libdir/*.so
%_includedir/*
%_infodir/*.info*

%if_enabled static
%_libdir/*.a
%endif

%changelog
* Sat Apr 30 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt3
- Rebuilt for debuginfo.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt2
- Rebuilt for soname set-versions.

* Fri Jun 04 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt1
- Initial revision.
