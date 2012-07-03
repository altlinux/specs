Name: o3read
Version: 0.0.4
Release: alt3

Summary: o3read is a standalone converter for the OpenOffice.org swriter and scalc formats
License: GPL
Group: Text tools
URL: http://siag.nu/o3read/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: %name-%version.tar.gz

Patch0: o3read-0.0.4-alt-natspec.patch
Patch1: o3read-alt-makefile.patch

# Automatically added by buildreq on Mon Aug 14 2006
BuildRequires: libnatspec-devel

%description
This is a standalone converter for the OpenOffice.org swriter (.sxw)
and scalc (.sxc) formats. It doesn't depend on Open Office or any
other external tools or libraries.

Example: unzip -p filformat.sxw content.xml | o3read | utf8tolatin1

There are three output modules:

 - o3read displays a dump of the parse tree
 - o3totxt creates plain text
 - o3tohtml creates html code

The utility utftolatin1 converts from utf8 to 8859-1.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -ansi -pedantic"

%install
%make_install DESTDIR=%buildroot install

%files
%doc ChangeLog README TODO
%_bindir/*
%_man1dir/*

%changelog
* Fri Aug 20 2010 Ilya Mashkin <oddity@altlinux.ru> 0.0.4-alt3
- rebuild

* Mon Aug 14 2006 Igor Zubkov <icesik@altlinux.ru> 0.0.4-alt2
- #7944
- buildreq

* Sat Jun 25 2005 Igor Zubkov <icesik@altlinux.ru> 0.0.4-alt1
- initial build for Sisyphus.
