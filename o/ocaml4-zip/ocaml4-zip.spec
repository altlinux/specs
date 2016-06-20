Name: ocaml4-zip
Version: 1.06
Release: alt1
Summary: OCaml library for reading and writing zip, jar and gzip files

Group: Development/ML
License: LGPLv2.1+ with exceptions
Url: http://pauillac.inria.fr/~xleroy/software.html
Packager: %packager

Provides:	ocaml-zip
Obsoletes:	ocaml-zip

Source: http://forge.ocamlcore.org/frs/download.php/1037/camlzip-%version.tar.gz
Patch: ocaml4-zip-alt-fix-make.patch

# Automatically added by buildreq on Wed Jul 16 2008
BuildRequires: ocaml4 zlib-devel

BuildRequires(pre): ocaml4

%description
This Objective Caml library provides easy access to compressed files
in ZIP and GZIP format, as well as to Java JAR files. It provides
functions for reading from and writing to compressed files in these
formats.

%prep
%setup -q -n camlzip-%version
%patch -p1

%build
%make_build all
%make_build allopt

cat > META <<EOF
name = "%name"
version = "%version"
requires = "unix"
description = "%description"
requires = ""
archive(byte) = "zip.cma"
archive(native) = "zip.cmxa"
EOF

%install
%define ocamlsitelib %_libdir/ocaml/site-lib

mkdir -p %buildroot%ocamlsitelib/zip

cp *.{mli,cmi,a,cma,so} %buildroot%_libdir/ocaml/site-lib/zip
cp META %buildroot%_libdir/ocaml/site-lib/zip

%files
%doc LICENSE
%ocamlsitelib/zip

%changelog
* Wed Jun 22 2016 Andrey Bergman <vkni@altlinux.org> 1.06-alt1
- Update to version 1.06.

* Mon Jun 17 2013 Andrey Bergman <vkni@altlinux.org> 1.05-alt1
- Update to version 1.05. Built with ocaml4.

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.04-alt1
- 1.04

* Wed Sep 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.03-alt1
- Initial build for ALTLinux

* Fri Feb 22 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-1
- Initial RPM release.
