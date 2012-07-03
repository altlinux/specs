%define dist Lingua-Stem-Snowball-Da
Name: perl-%dist
Version: 1.01
Release: alt1

Summary: Porters stemming algorithm for Denmark
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-devel

%description
Lingua::Stem::Snowball::Da is a perl port of the danish stemmer
at http://snowball.sourceforge.net, it was originally altered
from the Lingua::Stem::Snowball::Se.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build
rm blib/lib/Lingua/Stem/Snowball/stemmer.pl

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- decoupled from perl-Lingua-Stem
