Name: mingw32-binutils
Version: 2.19.51.0.14
Release: alt1.1
Summary: MinGW Windows binutils

License: GPLv2+ and LGPLv2+ and GPLv3+ and LGPLv3+
Group: Development/Other
Url: http://www.gnu.org/software/binutils/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://ftp.gnu.org/gnu/binutils/binutils-%version.tar.bz2

BuildRequires: flex
BuildRequires: bison
BuildRequires: texinfo
BuildRequires: rpm-macros-mingw32

# NB: This must be left in.
Requires: mingw32-filesystem
BuildRequires: perl-podlators

%description
MinGW Windows binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%prep
%setup -q -n binutils-%version

find -type f -name \*.orig -delete

sed -i 's/%%{release}/%release/g' bfd/Makefile{.am,.in}

# Fix build with glibc-devel >= 2.10
sed -i s/getline/get_line/g libiberty/testsuite/test-demangle.c

%build
# without -O0 gnu as doesnt works
%configure \
	CFLAGS="%optflags -O0" \
	--target=%_mingw32_target \
	--verbose --disable-nls \
	--with-included-gettext \
	--disable-win32-registry \
	--disable-werror \
	--with-sysroot=%_mingw32_sysroot \
	--with-bugurl=http://bugzilla.altlinux.org/

%make_build

%install
%makeinstall_std
# These files conflict with ordinary binutils.
rm -rf %buildroot%_infodir
rm -f %buildroot%_libdir/libiberty*
ln -sf ../../..%_bindir/%_mingw32_target-windres \
%buildroot%prefix/%_mingw32_target/bin/windres
ln -sf ../../..%_bindir/%_mingw32_target-dllwrap \
%buildroot%prefix/%_mingw32_target/bin/dllwrap

%files
%_man1dir/*
%_bindir/%_mingw32_target-*
%prefix/%_mingw32_target/bin
%prefix/%_mingw32_target/lib/ldscripts

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 2.19.51.0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 15 2010 Boris Savelev <boris@altlinux.org> 2.19.51.0.14-alt1
- sync with fedora

* Thu Jul 30 2009 Boris Savelev <boris@altlinux.org> 2.19.1-alt3
- add symlinks to %prefix/%_mingw32_target/bin

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 2.19.1-alt2
- rebuild with new macros

* Sun Jul 19 2009 Boris Savelev <boris@altlinux.org> 2.19.1-alt1
- initial build for Sisyphus

* Tue Mar 10 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.1-4
- Switch to using upstream (GNU) binutils 2.19.1.  It's exactly the
  same as the MinGW version now.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.1-2
- Rebuild for mingw32-gcc 4.4

* Tue Feb 10 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.1-1
- New upstream version 2.19.1.

* Mon Dec 15 2008 Richard W.M. Jones <rjones@redhat.com> - 2.19-1
- New upstream version 2.19.

* Sat Nov 29 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.50_20080109_2-10
- Must runtime-require mingw32-filesystem.

* Fri Nov 21 2008 Levente Farkas <lfarkas@lfarkas.org> - 2.18.50_20080109_2-9
- BR mingw32-filesystem >= 38

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.50_20080109_2-8
- Rename mingw -> mingw32.
- BR mingw32-filesystem >= 26.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.50_20080109_2-7
- Use mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.50_20080109_2-5
- Initial RPM release, largely based on earlier work from several sources.
