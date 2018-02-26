%define dist Text-Autoformat
Name: perl-%dist
Version: 1.669002
Release: alt1

Summary: Automatic text wrapping and reformatting
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Module-Build perl-Text-Reform

%description
Text::Autoformat provides intelligent formatting of plaintext without the need
for any kind of embedded mark-up. The module recognizes Internet quoting
conventions, a wide range of bulleting and number schemes, centred text, and
block quotations, and reformats each appropriately. Other options allow the
user to adjust inter-word and inter-paragraph spacing, justify text, and impose
various capitalization schemes.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Text

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.669002-alt1
- 1.14.0 -> 1.669002

* Tue Mar 04 2008 Alexey Tourbin <at@altlinux.ru> 1.14.0-alt1
- 1.13 -> 1.14.0

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 1.13-alt1
- 1.13

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.12-alt4
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.12-alt3
- Minor specfile fixes.
- BuildArch was changed to `noarch'.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.12-alt2
- Fixed {,Build}Requires

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.12-alt1
- First build for ALTLinux.


