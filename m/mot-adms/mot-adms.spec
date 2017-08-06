# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
# This package is part of the Free Electronic Lab.

%define majver 2.3

Name: mot-adms
Version: %majver.4
Release: alt1
Summary: An electrical compact device models converter

Group: Engineering
License: LGPLv2+
Url: http://mot-adms.sourceforge.net/

Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://sourceforge.net/projects/mot-adms/files/adms-source/%majver/adms-%version.tar.gz

# Remove useless perl-GD dependency
Patch: mot-adms-remove-BR-perl-GD.patch

BuildRequires: %_bindir/perl gcc-c++ perl(GD.pm)
BuildRequires: flex perl-XML-LibXML
#bison 
#BuildRequires: automake-common autoconf-common libtool-common

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
%setup -n adms-%version

%patch -p1 -b .perlGD
mv README.md README

%build
%autoreconf
%configure --enable-maintainer-mode

%make_build

%install
#make INSTALL="%_bindir/install -p" install DESTDIR=%buildroot
%makeinstall_std

# Remove libtool archives and static libs
find %buildroot -type f -name "*.la" -delete

%files
%doc AUTHORS TODO README ChangeLog
%doc COPYING
%_bindir/*
%_man1dir/admsXml.1*
%_man1dir/admsCheck.1*

%changelog
* Sun Aug 06 2017 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1
- Initial build for ALT Sisyphus.
