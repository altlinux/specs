%define dist Text-Reform
Name: perl-%dist
Version: 1.20
Release: alt2

Summary: Manual text wrapping and reformatting
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Buildarch: noarch

# disable dependency on Tex::Hyphen
%filter_from_requires /^perl.TeX.Hyphen/d

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Module-Build perl-Test-Pod

%description
The module supplies a re-entrant, highly configurable replacement
for the built-in Perl format() mechanism.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README demo
%dir %perl_vendor_privlib/Text
%perl_vendor_privlib/Text/Reform.pm

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt2
- rebuilt as plain src.rpm

* Fri Feb 19 2010 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.12.2 -> 1.20

* Tue Mar 04 2008 Alexey Tourbin <at@altlinux.ru> 1.12.2-alt1
- 1.11 -> 1.12.2

* Fri Sep 02 2005 Andrey Brindeew <abr@altlinux.org> 1.11-alt6
- Fixed issue with perl(TeX/Hyphen.pm) dependency.

* Wed Aug 31 2005 Andrey Brindeew <abr@altlinux.org> 1.11-alt5
- Rebuild for version matching (thanks to at@ for discovering
  this issue).

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.11-alt4
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.11-alt3
- Minor specfile fixes.
- Buildarch was changed to `noarch'.
- All demos moved to docs.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.11-alt2
- Demos was patched.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.11-alt1
- First build for ALTLinux.


