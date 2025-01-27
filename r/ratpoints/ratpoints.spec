%global sover 0

%ifarch %ix86 x86_64
%global use_sse -DUSE_SSE
%else
%global use_sse %nil
%endif

Name: ratpoints
Version: 2.2.1
Release: alt1

Summary: Find rational points on hyperelliptic curves

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://www.mathe2.uni-bayreuth.de/stoll/programs/

Source0: %url/%name-%version.tar.gz
Source1: %name.1
# Based on ratpoints-shared.patch by fedora
Patch: ratpoints-2.2.1-alt-fedora-shared.patch

BuildRequires: gcc libgmp-devel texlive-dist

%description
Ratpoints is a program that uses an optimized quadratic sieve algorithm
in order to find rational points on hyperelliptic curves.

%package -n lib%name%sover
Summary: %name library
Group: System/Libraries

%description -n lib%name%sover
Library for %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Sciences/Mathematics
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
Header and library for development with %name.

%prep
%setup
%patch -p1

sed -e "s|-Wall -O2 -fomit-frame-pointer|%optflags %use_sse|" \
   -i Makefile

%build
%make_build LIB=/%_lib LIBDIR=%_libdir

%install
%makeinstall_std LIB=/%_lib LIBDIR=%_libdir
install -p -D -m644 %SOURCE1 %buildroot%_man1dir/%name.1

%check
LD_LIBRARY_PATH=$PWD: make test

%files
%doc gpl-2.0.txt
%doc ratpoints-doc-2.2.pdf
%_bindir/ratpoints
%_man1dir/ratpoints.1*

%files -n lib%name%sover
%_libdir/libratpoints.so.%{sover}*

%files -n lib%name-devel
%_includedir/ratpoints.h
%_libdir/libratpoints.so

%changelog
* Mon Jan 27 2025 Leontiy Volodin <lvol@altlinux.org> 2.2.1-alt1
- New version 2.2.1.
- Packaged the library separately (thanks fedora for the patch).

* Mon Oct 25 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
