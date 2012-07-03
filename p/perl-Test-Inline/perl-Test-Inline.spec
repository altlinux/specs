%define module Test-Inline
%define m_distro Test-Inline
%define m_name Test-Inline
%define m_author_id ADAMK
%define _enable_test 1

Name: perl-Test-Inline
Version: 2.212
Release: alt1

Summary: Test-Inline - Inlining your tests next to the code being tested

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/~adamk/%m_distro-%version

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/A/AD/ADAMK/Test-Inline-2.212.tar.gz

# Automatically added by buildreq on Sat Sep 24 2005
BuildRequires: perl-Algorithm-Dependency perl-Class-Autouse perl-Config-Tiny perl-File-Find-Rule perl-File-Flat perl-File-Slurp perl-Number-Compare perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Pod-Tests perl-Test-Pod perl-Text-Glob perl-devel perl-prefork

BuildRequires: perl-Algorithm-Dependency perl-Class-Autouse perl-devel perl-prefork perl-Pod-Tests perl-Test-ClassAPI perl-File-chmod perl-Test-Script

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
Embedding tests allows tests to be placed near the code its testing. This
is a nice supplement to the traditional .t files. It's like XUnit,
Perl-style.  Test::Tutorial is just documentation. To actually get
anything done you use pod2test. Read the Test::Inline::Tutoral, really.
A test is denoted using either "=for testing" or a "=begin/end testing"
block.

%prep
%setup -q -n %m_distro-%version
#%__subst "s|VCS { \$self|CVS { my \$self = shift; \$self|" lib/Test/Inline/IO/File/VCS.pm

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/*
%perl_vendor_privlib/Test/*
%_man1dir/*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.212-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.211-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 2.211-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.102-alt2
- fix directory ownership violation

* Sat Sep 24 2005 Vitaly Lipatov <lav@altlinux.ru> 2.102-alt1
- new version
- thanks Alexey Tourbin (at@) for bug fix

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- first build for ALT Linux Sisyphus
