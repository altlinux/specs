%define dist MooseX-AuthorizedMethods
Name: perl-%dist
Version: 0.006
Release: alt2

Summary: Syntax sugar for authorized methods
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Pod-Escapes perl-aliased perl-devel perl(Sub/Name.pm)

%description
This method exports the "authorized" declarator that makes a
verification if the user has the required permissions before the acual
invocation. The default verification method will take the "user"
method result and call "roles" to list the roles given to that user.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/MooseX

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 0.006-alt2
- fixed build

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1.1
- rebuild to restore role requires

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.006-alt1
- initial revision
