%define _unpackaged_files_terminate_build 1
%define module Mail-Sendmail

# test trying to send real e-mail, no benefit for automatic builds
%def_disable test

Name: perl-%module
Version: 0.80
Release: alt1

Summary: Simple platform independent mailer
License: Distributable
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/N/NE/NEILB/%{module}-%{version}.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Tue Jul 31 2007
BuildRequires: perl-devel

%description
Simple platform independent e-mail from your perl script. Only requires
Perl 5 and a network connection.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README Todo
%perl_vendor_privlib/Mail

%changelog
* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.79-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 31 2007 Victor Forsyuk <force@altlinux.org> 0.79-alt2
- Spec cleanups.
- Author did not choose standard license for this module (he just wrote
  "You can use this module freely"). So we will put just Distributable
  into License tag (as Fedora did).

* Tue Feb 22 2005 Vladimir Lettiev <crux@altlinux.ru> 0.79-alt1
- Initial release for ALTLinux Sisyphus
