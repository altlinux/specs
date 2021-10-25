%global major 0

%ifarch %ix86 x86_64
%global use_sse -DUSE_SSE
%else
%global use_sse %nil
%endif

Name: ratpoints
Version: 2.1.3
Release: alt1
Summary: Find rational points on hyperelliptic curves
License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://www.mathe2.uni-bayreuth.de/stoll/programs/

Source: %url/%name-%version.tar.gz

# Initially generated with help2man as:
# LD_LIBRARY_PATH=$PWD: help2man --section=1 --no-info \
#    --version-string="%%{version}" \
#    -o %%buildroot%%{_mandir}/man1/ratpoints.1 ./ratpoints
# but edited for better formatting.

Source1: %name.1
Patch: %name-shared.patch

BuildRequires: gcc
BuildRequires: libgmp-devel

%description
Ratpoints is a program that uses an optimized quadratic sieve algorithm
in order to find rational points on hyperelliptic curves.

%package devel
Summary: Development files for %name
Group: Sciences/Mathematics

%description devel
Header and library for development with %name.

%prep
%setup
%patch -p1

sed -e "s|-Wall -O2 -fomit-frame-pointer|%optflags %use_sse|" \
   -e "s|-shared|& $RPM_LD_FLAGS|" \
   -i Makefile

%build
%make_build

%install
%makeinstall_std LIBDIR=%_libdir
install -p -D -m644 %SOURCE1 %buildroot%_man1dir/%name.1

%check
LD_LIBRARY_PATH=$PWD: make test

%files
%doc gpl-2.0.txt
%doc ratpoints-doc.pdf
%_bindir/ratpoints
%_libdir/libratpoints.so.%major
%_man1dir/ratpoints.1*

%files devel
%_includedir/ratpoints.h
%_libdir/libratpoints.so

%changelog
* Mon Oct 25 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
