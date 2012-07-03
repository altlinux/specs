%define dist XML-Bare
Name: perl-%dist
Version: 0.45
Release: alt1.2

Summary: A minimal XML parser / schema checker / pretty-printer using C internally
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod

%description
This module is a 'Bare' XML parser. It is implemented in C. The parser
itself is a simple state engine that is less than 500 lines of C. The
parser builds a C struct tree from input text. That C struct tree is
converted to a Perl hash by a Perl function that makes basic calls back
to the C to go through the nodes sequentially.

The parser itself will only cease parsing if it encounters tags that
are not closed properly. All other inputs will parse, even invalid
inputs. To allowing checking for validity, a schema checker is included
in the module as well.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/XML
%perl_vendor_autolib/XML

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt1.1
- rebuilt with perl 5.12

* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.45-alt1
- initial build for ALT Linux Sisyphus
