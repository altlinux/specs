%define m_distro Wx-Perl-ProcessStream
%define _perl_req_method relaxed

Name: perl-Wx-Perl-ProcessStream
Version: 0.30
Release: alt2
Summary: Wx::Perl::ProcessStream - access IO of external processes via events

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~mdootson/Wx-Perl-ProcessStream/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Wx perl-Archive-Tar xvfb-run

# With relaxed perl.req method some deps are lost
Requires: perl-Wx

%description
%summary

%prep
%setup -q -n %m_distro-%version

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
