%define _unpackaged_files_terminate_build 1
%define dist Log-Dispatch-FileRotate

Name: perl-%dist
Version: 1.23
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Log to files that archive/rotate themselves
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MS/MSCHOUT/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Dec 29 2008
BuildRequires: perl-Date-Manip perl-Log-Log4perl perl-devel perl(Path/Tiny.pm) perl(Test/Warn.pm)

%description
This module provides a simple object for logging to files under the
Log::Dispatch::* system, and automatically rotating them according to
different constraints.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/Log/

%changelog
* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 1.19-alt1
- 1.19

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 1.18-alt1
- 1.18

* Thu Jul 19 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt1
- Adopted an orphan.

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 1.13-alt1
- Initial build for ALT Linux
