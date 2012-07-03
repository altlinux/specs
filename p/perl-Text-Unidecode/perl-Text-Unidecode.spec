%define dist Text-Unidecode
Name: perl-%dist
Version: 0.04
Release: alt2

Summary: US-ASCII transliterations of Unicode text
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# avoid rpmdb bloat
%add_findprov_skiplist */Text/Unidecode/x*.pm

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
Text::Unidecode provides a function, `unidecode(...)' that takes Unicode
data and tries to represent it in US-ASCII characters (i.e., the universally
displayable characters between 0x00 and 0x7F). The representation is almost
always an attempt at *transliteration* -- i.e., conveying, in Roman letters,
the pronunciation expressed by the text in some other writing system.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Text

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt

* Fri Mar 23 2007 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision (for Text::Soundex)
