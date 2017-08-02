%define _unpackaged_files_terminate_build 1
%define module Net-DNS-Resolver-Programmable

Name: perl-%module
Version: 0.009
Release: alt1

Summary: Perl module that implements a programmable DNS resolver class for offline emulation of DNS
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/B/BI/BIGPRESH/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 31 2008
BuildRequires: perl-Module-Build perl-Net-DNS

%description
Net-DNS-Resolver-Programmable is a Perl module that implements a programmable
DNS resolver class for offline emulation of DNS.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE CHANGES TODO README
%perl_vendor_privlib/Net/DNS/*

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 0.003-alt1
- 0.003

* Mon May 14 2007 Victor Forsyuk <force@altlinux.org> 0.002.2-alt1
- Initial build.
