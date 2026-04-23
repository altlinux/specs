# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
# This package is part of the Free Electronic Lab.

%define majver 2.3

Name: mot-adms
Version: %majver.7
Release: alt2
Summary: An electrical compact device models converter

Group: Engineering
License: GPL-3.0-or-later
URL: https://github.com/Qucs/ADMS
VCS: https://github.com/Qucs/ADMS

# Source-url: https://github.com/Qucs/ADMS/archive/release-%version/adms-%version.tar.gz
Source: adms-%version.tar

# https://github.com/Qucs/ADMS/issues/115
Patch: gcc15.patch

BuildRequires: gcc-c++
BuildRequires: flex perl-XML-LibXML

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
%setup -n adms-%version
%autopatch -p1

%build
%autoreconf
%configure --enable-maintainer-mode --disable-silent-rules

%make_build -C admsXml \
	admstpathYacc.h \
	preprocessorYacc.h \
	verilogaYacc.y \
	%nil
%make_build

%install
%makeinstall_std

# Remove libtool archives and static libs
find %buildroot -type f '(' -name '*.la' -or -name '*.a' ')' -delete
# For now, remove these .so files
find %buildroot -type l -name '*.so' -delete

%files
%doc AUTHORS TODO README.md ChangeLog
%_bindir/admsCheck
%_bindir/admsXml

%_libdir/libadms*.so.*
%dir %_includedir/adms
%_includedir/adms/*.vams

%_man1dir/admsCheck.1.*
%_man1dir/admsXml.1.*

%changelog
* Thu Apr 23 2026 Anton Midyukov <antohami@altlinux.org> 2.3.7-alt2
- Fix build with gcc15.

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 2.3.7-alt1
- New version 2.3.7
- Fix License Tag
- Update Url Tag

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1.1
- Rebuilt for aarch64

* Sun Aug 06 2017 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1
- Initial build for ALT Sisyphus.
