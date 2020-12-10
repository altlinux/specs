# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
# This package is part of the Free Electronic Lab.

%define majver 2.3

Name: mot-adms
Version: %majver.7
Release: alt1
Summary: An electrical compact device models converter

Group: Engineering
License: GPLv3+
Url: https://github.com/Qucs/ADMS

Packager: Anton Midyukov <antohami@altlinux.org>

Source: adms-%version.tar
# Source-url: https://github.com/Qucs/ADMS/archive/release-%version/adms-%version.tar.gz

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
#make INSTALL="%_bindir/install -p" install DESTDIR=%buildroot
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

%_man1dir/admsCheck.1*
%_man1dir/admsXml.1*

%changelog
* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 2.3.7-alt1
- New version 2.3.7
- Fix License Tag
- Update Url Tag

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1.1
- Rebuilt for aarch64

* Sun Aug 06 2017 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1
- Initial build for ALT Sisyphus.
