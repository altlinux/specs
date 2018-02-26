%define dist Email-Simple
Name: perl-%dist
Version: 2.100
Release: alt2

Summary: Simple parsing of RFC2822 message format and headers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# see Makefile.PL
Conflicts: perl-Email-MIME < 1.857

# last released version was 1.424
Provides: perl-Email-Simple-Creator = 1.429
Obsoletes: perl-Email-Simple-Creator < 1.429

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-Email-Date-Format perl-Test-Pod

%description
Email::Simple is the first deliverable of the "Perl Email Project",
a reaction against the complexity and increasing bugginess of the
Mail::* modules. In contrast, Email::* modules are meant to be
simple to use and to maintain, pared to the bone, fast, minimal
in their external dependencies, and correct.

%prep
%setup -q -n %dist-%version

# avoid build dependency on Email::MIME
sed -i- '/^if .* require Email::MIME/,/^}/s/^/#/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.100-alt2
- rebuilt as plain src.rpm

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 2.100-alt1
- 2.004 -> 2.100
- provides and obsoletes perl-Email-Simple-Creator

* Sat Aug 30 2008 Alexey Tourbin <at@altlinux.ru> 2.004-alt1
- 1.94 -> 2.004

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.94-alt1
- initial revision
