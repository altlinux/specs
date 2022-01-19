%define _unpackaged_files_terminate_build 1
%define module		Test-Manifest
%define m_distro	Test-Manifest
%define m_name		Test::Manifest
%define m_author_id	BDFOY
Name: perl-%module
Version: 2.023
Release: alt1

Summary: Interact with a t/test_manifest file
Group: Development/Perl
License: Artistic

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/B/BD/BDFOY/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Jul 30 2003
BuildRequires: perl-devel

%description
Test::Manifest looks in the t/test_manifest file to find out which tests you
want to run and the order in which you want to run them. It constructs the
right value for MakeMaker to do the right thing.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod Changes examples
%perl_vendor_privlib/Test
#%perl_vendor_man3dir/*
%doc Changes

%changelog
* Wed Jan 19 2022 Igor Vlasenko <viy@altlinux.org> 2.023-alt1
- automated CPAN update

* Thu Jan 21 2021 Igor Vlasenko <viy@altlinux.ru> 2.022-alt1
- automated CPAN update

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 2.021-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 1.14-alt1
- 1.11 -> 1.14

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 1.11-alt1
- 0.93 -> 1.11

* Sat Mar 06 2004 Andrey Brindeew <abr@altlinux.ru> 0.93-alt1
- 0.93

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 0.91-alt2
- Url and Summary tags was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 0.91-alt1
- First build for ALTLinux.

