%define dist XML-Encoding
Name: perl-%dist
Version: 2.08
Release: alt1

Summary: Module for parsing XML encoding maps
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-XML-Parser perl-devel

%description
This module, built as a subclass of XML::Parser, parses encoding map
XML files.  Included in the distribution is the compile_encoding script
that compiles these to the binary form used by XML::Parser in order to
parse scripts in the given encoding.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/make_encmap
%_bindir/compile_encoding
%dir %perl_vendor_privlib/XML
%perl_vendor_privlib/XML/Encoding.pm

%changelog
* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 2.08-alt1
- 2.07 -> 2.08

* Fri Apr 10 2009 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- 2.01 -> 2.07

* Mon Mar 03 2008 Alexey Tourbin <at@altlinux.ru> 2.01-alt1
- 1.01 -> 2.01, resurrected from orphaned

* Thu Aug 09 2001 Stanislav Ievlev <inger@altlinux.ru> 1.01-alt1
- We need it for foomatic too.

* Mon Jun 18 2001 Till Kamppeter <till@mandrakesoft.com> 1.01-1mdk
- Newly introduced for Foomatic.
