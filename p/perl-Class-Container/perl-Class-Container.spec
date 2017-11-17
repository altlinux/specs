%define _unpackaged_files_terminate_build 1
%define dist Class-Container
Name: perl-%dist
Version: 0.13
Release: alt1.1

Summary: Glues object frameworks together transparently
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Module-Build perl-Params-Validate

%description
This class facilitates building frameworks of several classes that
inter-operate.  It was first designed and built for HTML::Mason,
in which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer,
and several other objects must create each other transparently,
passing the appropriate parameters to the right class, possibly
substituting other subclasses for any of these objects.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class*

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- 0.11 -> 0.12
- manual pages not packaged (use perldoc)

* Thu Jul 01 2004 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- initial revision
