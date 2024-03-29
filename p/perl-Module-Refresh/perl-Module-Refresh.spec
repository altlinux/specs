%define _unpackaged_files_terminate_build 1
#
#   - Module-Refresh -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Module::Refresh
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Module-Refresh
%define m_distro Module-Refresh
%define m_name Module-Refresh
%define m_author_id unknown
%define _enable_test 1

Name: perl-Module-Refresh
Version: 0.18
Release: alt1

Summary: Module-Refresh - Refresh INC files when updated on disk

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/B/BP/BPS/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Fri Sep 02 2005
BuildRequires: perl-devel perl(Path/Class.pm)

%description
This module is a generalization of the functionality provided by
Apache::StatINC and Apache::Reload. It's designed to make it easy to do
simple iterative development when working in a persistent environment.
It does not require mod_perl.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Module/

%changelog
* Wed May 11 2022 Igor Vlasenko <viy@altlinux.org> 0.18-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- new version 0.13 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt3
- fix directory ownership violation

* Tue Oct 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt2
- fix unexpanded macro
- add doc

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- first build for ALT Linux Sisyphus
