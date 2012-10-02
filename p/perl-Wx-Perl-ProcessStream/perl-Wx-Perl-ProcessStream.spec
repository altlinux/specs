%define dist Wx-Perl-ProcessStream
%define _perl_req_method relaxed

Name: perl-Wx-Perl-ProcessStream
Version: 0.32
Release: alt1

Summary: Wx::Perl::ProcessStream - access IO of external processes via events
License: Perl
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

# With relaxed perl.req method some deps are lost
Requires: perl-Wx

BuildRequires: perl-devel perl-Wx perl-Archive-Tar xvfb-run
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %dist-%version

%build
%def_without test
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Wx/Perl/ProcessStream*
%doc Changes README 

%changelog
* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.32-alt1
- 0.30 -> 0.32
- built as plain srpm

* Wed Mar 09 2011 Vladimir Lettiev <crux@altlinux.ru> 0.30-alt2
- Relaxed perl_req_method (due to failures while deparsing `use Wx')

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.30-alt1
- New version 0.30

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.29-alt1
- New version 0.29

* Fri Oct 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.28-alt1
- New version 0.28

* Fri Mar 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.27-alt1
- New version 0.27

* Tue Jan 26 2010 Vladimir Lettiev <crux@altlinux.ru> 0.24-alt1
- initial build
