%define dist Variable-Magic
Name: perl-%dist
Version: 0.46
Release: alt2

Summary: Associate user-defined magic to variables from Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Capture-Tiny perl-Test-Pod perl-threads

%description
Magic is Perl's way of enhancing variables.  This mechanism lets the user
add extra data to any variable and hook syntactical operations (such as
access, assignment or destruction) that can be applied to it.  With this
module, you can add your own magic to any variable without having to write
a single line of XS.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Variable
%perl_vendor_autolib/Variable

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.46-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.43-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- initial revision, for B::Hooks::EndOfScope
