%define dist libxml-perl
Name: perl-%dist
Version: 0.08
Release: alt3

Summary: Collection of Perl modules for working with XML
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-XML-Parser perl-devel

%description
libxml-perl is a collection of smaller Perl modules, scripts, and documents
for working with XML in Perl.  libxml-perl software works in combination
with XML::Parser, PerlSAX, XML::DOM, XML::Grove and others.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README doc/* examples
%perl_vendor_privlib/XML
%perl_vendor_privlib/Data

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.08-alt3
- rebuilt as plain src.rpm

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 0.08-alt2
- rebuild

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.08-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 0.08-alt1
- 0.08
- Removed perl-libxml-perl-0.07-alt-fixes.patch

* Fri Sep 05 2003 Andrey Brindeew <abr@altlinux.ru> 0.07-alt4
- lib/XML/Perl2SAX.pm patched.

* Sun Aug 10 2003 Andrey Brindeew <abr@altlinux.ru> 0.07-alt3
- Buildreq's updated.
- changed URL.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 0.07-alt2
- Minor specfile changes.
- BuildArch was changed to `noarch'.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.07-alt1
- Release.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.07-alt0.2
- Docs and examples included.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.03-alt0.1
- First build for ALTLinux.
