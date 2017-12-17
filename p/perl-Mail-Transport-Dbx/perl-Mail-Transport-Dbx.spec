%define dist Mail-Transport-Dbx
Name: perl-%dist
Version: 0.07
Release: alt5.1.1.1.1

Summary: Parse Outlook Express mailboxes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Mail::Transport::Dbx is a wrapper around libdbx to read Outlook Express
mailboxes (more commonly known as .dbx files). It relies on a patched
version of libdbx to make it work on big-endian machines (like Solaris).

%prep
%setup -q -n %dist-%version

# drop me when upstream fix it
if [ %version = 0.07 ]; then
# encoding patch
sed -i -e 's,^=head1,=encoding ISO8859-1\n\n=head1,' `find . -name '*.pm'`
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Mail
%perl_vendor_autolib/Mail

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt5.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt5
- built for perl 5.18

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt4
- fixed build (pod encoding patch)

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt2.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- fix directory ownership violation

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus

