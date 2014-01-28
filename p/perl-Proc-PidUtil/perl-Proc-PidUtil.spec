%define module Proc-PidUtil

Name: perl-%module
Version: 0.09
Release: alt1

Summary: Perl module: PID file management utilities
License: GPL
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/M/MI/MIKER/Proc-PidUtil-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 05 2007
BuildRequires: perl-devel

%description
Proc::PidUtil provides utilities to manage PID files.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Proc/

%changelog
* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 05 2007 Victor Forsyuk <force@altlinux.org> 0.08-alt1
- Initial build.
