%define dist Text-Format
Name: perl-%dist
Version: 0.53
Release: alt1

Summary: Various subroutines to format text
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-Module-Build

%description
The format routine will format under all circumstances even if the width
isn't enough to contain the longest words.  Text::Wrap will die under
these circumstances, although I am told this is fixed.  If columns is
set to a small number and words are longer than that and the leading
'whitespace' than there will be a single word on each line.  This will
let you make a simple word list which could be indented or right
aligned.  There is a chance for croaking if you try to subvert the
module.  If you don't pass in text then the internal text is worked on,
though not modfied.  Text::Format is meant for more powerful text
formatting than what Text::Wrap allows.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Text

%changelog
* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 0.53-alt1
- 0.52 -> 0.53

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.52-alt2
- fix directory ownership violation
- disable man packaging

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.52-alt1
- first build for ALT Linux Sisyphus
