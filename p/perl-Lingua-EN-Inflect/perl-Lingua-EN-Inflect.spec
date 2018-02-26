%define dist Lingua-EN-Inflect
Name: perl-%dist
Version: 1.893
Release: alt1

Summary: Convert singular to plural, select "a" or "an"
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-devel

%description
The exportable subroutines of Lingua::EN::Inflect provide plural
inflections, "a"/"an" selection for English words, and manipulation
of numbers as words.

%prep
%setup -q -n %dist-%version
rm Build.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 1.893-alt1
- 1.891 -> 1.893

* Mon Apr 26 2010 Alexey Tourbin <at@altlinux.ru> 1.891-alt1
- 1.89 -> 1.891

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 1.89-alt1
- initial revision
