Name: jam
Version: 2.6.1
Release: alt1

Summary: Jam is a powerful and highly customizable utility to build programs.
License: Jam
Group: Development/C
Url: http://public.perforce.com/public/jam/index.html

#Source-url: ftp://ftp.perforce.com/jam/%{name}-%{version}.zip
# Source-url: http://deb.debian.org/debian/pool/main/j/jam/jam_%version.orig.tar.gz
Source: %name-%version.tar

Patch0:		jam-2.5-overflow.patch
Patch1:		jam-missing-includes.patch
Patch2:		jam-implicit-int.patch
Patch3:		jam-2.5-argv-fixup.patch
Patch4:		jam-2.6.1-fix-typo.patch

BuildRequires(pre): rpm-macros-make

Conflicts: boost-jam

%description
Jam is a program construction tool, like make. Jam recursively builds target
files from source files, using dependency information and updating actions
expressed in the Jambase file, which is written in jam's own interpreted
language. The default Jambase is compiled into jam and provides a boilerplate
for common use, relying on a user-provide file "Jamfile" to enumerate actual
targets and sources.

%prep
%setup
%patch0 -p1 -b .overflows
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .fixup
%patch4 -p1 -b .fix-typo

%build
%make_build_ext

%install
mkdir -p %buildroot/%_bindir
install -m0755 bin.linux*/jam %buildroot/%_bindir
install -m0755 bin.linux*/mkjambase %buildroot/%_bindir

%files
%doc README RELNOTES *.html
%_bindir/jam
%_bindir/mkjambase

%changelog
* Mon Mar 03 2025 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version 2.6.1
- add patches and install section from Fedora

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.5-alt1
- Initial build for Sisyphus.

