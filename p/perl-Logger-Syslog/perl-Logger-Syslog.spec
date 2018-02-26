%define module_name Logger-Syslog

Name: perl-%module_name
Version: 1.1
Release: alt1.1

Summary: A simple wrapper over Sys::Syslog perl module
License: Artistic
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/Logger/%module_name-%version.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Wed Jun 20 2007
BuildRequires: perl-devel

%description
An intuitive wrapper over Syslog for Perl. Provides one function per
syslog message level for sending message to syslog.

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -f %buildroot/.perl.req

%files
%perl_vendor_privlib/Logger

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Jun 20 2007 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- Initial build.
