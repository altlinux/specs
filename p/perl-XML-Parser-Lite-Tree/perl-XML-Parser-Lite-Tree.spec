%define module XML-Parser-Lite-Tree

Name: perl-%module
Version: 0.14
Release: alt1

Summary: Lightweight XML tree builder
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/XML/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 21 2011
BuildRequires: perl-devel

%description
This is a singleton class for parsing XML into a tree structure.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/XML/

%changelog
* Thu Jul 21 2011 Victor Forsiuk <force@altlinux.org> 0.14-alt1
- 0.14

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- 0.12

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 0.08-alt1
- 0.08

* Fri Jun 20 2008 Victor Forsyuk <force@altlinux.org> 0.03-alt1
- Initial build.
