%def_enable static
%{?_enable_static:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%def_enable check

Name: pcre2
Version: 10.40
Release: alt2

Summary: Perl-compatible regular expression library
Group: System/Libraries
License: BSD-style
Url: http://www.pcre.org/

Vcs: https://github.com/PhilipHazel/pcre2.git
Source: https://github.com/PhilipHazel/%name/releases/download/%name-%version/%name-%version.tar.gz
#Source: https://ftp.pcre.org/pub/pcre/%name-%version.tar.gz

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
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
%ifnarch %e2k riscv64
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
    --enable-unicode \
    --disable-valgrind \
    %{subst_enable static}
%nil
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
* Sat Nov 05 2022 Ivan A. Melnikov <iv@altlinux.org> 10.40-alt2
- enable static libraries (altbug #44217);
- don't force-enable jit on riscv64 to fix build there.

* Sat Apr 16 2022 Yuri N. Sedunov <aris@altlinux.org> 10.40-alt1
- 10.40

* Sun Oct 31 2021 Yuri N. Sedunov <aris@altlinux.org> 10.39-alt1
- 10.39

* Tue Oct 05 2021 Yuri N. Sedunov <aris@altlinux.org> 10.38-alt1
- 10.38

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 10.37-alt1.1
- disabled build of static libraries

* Thu May 27 2021 Yuri N. Sedunov <aris@altlinux.org> 10.37-alt1
- 10.37

* Fri Dec 04 2020 Yuri N. Sedunov <aris@altlinux.org> 10.36-alt1
- 10.36

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 10.35-alt1
- 10.35

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 10.34-alt1
- 10.34

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 10.33-alt1.1
- mike@: support e2kv4 build through %%e2k macro

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 10.33-alt1
- 10.33

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 10.32-alt1
- 10.32

* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 10.31-alt1
- 10.31

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

