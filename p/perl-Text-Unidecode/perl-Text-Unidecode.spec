%define _unpackaged_files_terminate_build 1
%define dist Text-Unidecode
Name: perl-%dist
Version: 1.30
Release: alt1

Summary: US-ASCII transliterations of Unicode text
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SB/SBURKE/Text-Unidecode-%{version}.tar.gz

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
* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt

* Fri Mar 23 2007 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision (for Text::Soundex)
