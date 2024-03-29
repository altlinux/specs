%define _unpackaged_files_terminate_build 1
#
#   - App::Control -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       http://search.cpan.org/CPAN/authors/id/A/AW/AWRIGLEY/App-Control-1.02.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module App-Control
%define m_distro App-Control
%define m_name App::Control
%define m_author_id unknown
%define _enable_test 1

Name: perl-App-Control
Version: 1.07
Release: alt1

Summary: Perl module for apachectl style control of another script or

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/A/AW/AWRIGLEY/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Fri Jun 01 2007
BuildRequires: perl-devel

%description
App::Control is a simple module to replicate the kind of functionality you get
with apachectl to control apache, but for any script or executable. There is a
very simple OO interface, where the constructor is used to specify the
executable, command line arguments, and pidfile, and various methods (start,
stop, etc.) are used to control the executable in the obvious way.

The module is intended to be used in a simple wrapper control script. Currently
the module does a fork and exec to start the executable, and sets the signal
handler for SIGCHLD to 'IGNORE' to avoid zombie processes.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/App*

%changelog
* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 1.07-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2
- removed perl dir ownership

* Fri Jun 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- first build for ALT Linux Sisyphus

