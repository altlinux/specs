%def_enable static

Name: pcre2
Version: 10.30
Release: alt2

Summary: Perl-compatible regular expression library
Group: System/Libraries
License: BSD
Url: http://www.pcre.org/

Source: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%name-%version.tar.gz

BuildRequires: libreadline-devel zlib-devel bzlib-devel

%description
PCRE2 is a re-working of the original PCRE (Perl-compatible regular
expression) library to provide an entirely new API.

PCRE2 is written in C, and it has its own API. There are three sets of
functions, one for the 8-bit library, which processes strings of bytes, one
for the 16-bit library, which processes strings of 16-bit values, and one for
the 32-bit library, which processes strings of 32-bit values. There are no C++
wrappers.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
PCRE2 is a re-working of the original PCRE (Perl-compatible regular
expression) library to provide an entirely new API.

This package provides shared perl-compatible regular expression libraries.

%package -n lib%name-devel
Summary: Development files for PCRE2 libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides development files for PCRE2 libraries.

%package -n lib%name-devel-static
Summary: Static PCRE2 libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package provides static versions of PCRE2 libraries.

%package tools
Summary: Auxiliary utilities for %name
Group: Development/Tools
Requires: lib%name = %version-%release

%description tools
Utilities demonstrating PCRE2 capabilities like pcre2grep or pcre2test.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure \
%ifnarch e2k
    --enable-jit \
    --enable-pcre2grep-jit \
%endif
    --disable-bsr-anycrlf \
    --disable-coverage \
    --disable-ebcdic \
    --enable-newline-is-lf \
    --enable-pcre2-8 \
    --enable-pcre2-16 \
    --enable-pcre2-32 \
    --disable-pcre2test-libedit \
    --enable-pcre2test-libreadline \
    --enable-pcre2grep-libbz2 \
    --enable-pcre2grep-libz \
    --disable-rebuild-chartables \
    --enable-shared \
    --enable-stack-for-recursion \
    --enable-static \
    --enable-unicode \
    --disable-valgrind \
    %{subst_enable static}
%make_build

%install
%makeinstall_std

# relocate shared libraries to /%_lib for journalctl
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/lib%name-{8,16,32,posix}.so; do
	if t=$(readlink "$f"); then
		ln -sf ../../%_lib/"$t" "$f"
	fi
done

mv %buildroot%_libdir/lib%name-{8,16,32,posix}.so.* %buildroot/%_lib/

%check
%make check

%files -n lib%name
/%_lib/lib%name-16.so.*
/%_lib/lib%name-32.so.*
/%_lib/lib%name-8.so.*
/%_lib/lib%name-posix.so.*
%doc LICENCE AUTHORS ChangeLog NEWS README

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man1dir/%name-config.1.*
%_man3dir/*
%doc doc/html
%doc HACKING ./src/%{name}demo.c

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files tools
%_bindir/%{name}grep
%_bindir/%{name}test
%_man1dir/%{name}grep.1.*
%_man1dir/%{name}test.1.*

%exclude %_docdir/%name

%changelog
* Mon Jan 29 2018 Yuri N. Sedunov <aris@altlinux.org> 10.30-alt2
- relocated shared libraries from %%_libdir to /%%_lib for systemd
- mike@:
  E2K: disable jit

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 10.30-alt1
- 10.30

* Sun Feb 19 2017 Yuri N. Sedunov <aris@altlinux.org> 10.23-alt1
- 10.23

* Mon Aug 01 2016 Yuri N. Sedunov <aris@altlinux.org> 10.22-alt1
- 10.22

* Fri Jan 15 2016 Yuri N. Sedunov <aris@altlinux.org> 10.21-alt1
- 10.21

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 10.20-alt1
- first build for Sisyphus

