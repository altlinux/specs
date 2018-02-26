%define dist Lingua-Stem
Name: perl-%dist
Version: 0.84
Release: alt1

Summary: Provides word stemming algorithms localized by language
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-Lingua-PT-Stemmer perl-Lingua-Stem-Fr perl-Lingua-Stem-It perl-Lingua-Stem-Snowball-Da perl-Module-Build perl-Snowball-Norwegian perl-Snowball-Swedish perl-Text-German

%description
This routine applies stemming algorithms to its parameters,
returning the stemmed words as appropriate to the selected
locale.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.84-alt1
- 0.81 -> 0.84
- decoupled language-specific modules

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 0.81-alt2
- Text-German: 0.03 -> 0.06
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.81-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jul 30 2004 Alexey Tourbin <at@altlinux.ru> 0.81-alt1
- 0.70 -> 0.81
- packaged %dist-Ru here (laziness is virtue)

* Thu May 20 2004 Alexey Tourbin <at@altlinux.ru> 0.70-alt1
- initial revision
- packaged a bunch of language-specific modules here, see description
