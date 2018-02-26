%define module		Test-Manifest
%define m_distro	Test-Manifest
%define m_name		Test::Manifest
%define m_author_id	BDFOY
Name: perl-%module
Version: 1.23
Release: alt1

Summary: Interact with a t/test_manifest file
Group: Development/Perl
License: Artistic

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/B/BD/BDFOY/Test-Manifest-1.23.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Jul 30 2003
BuildRequires: perl-devel

%description
Test::Manifest looks in the t/test_manifest file to find out which tests you
want to run and the order in which you want to run them. It constructs the
right value for MakeMaker to do the right thing.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test
#%perl_vendor_man3dir/*
%doc Changes

%changelog
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

