Name: perl-Git-Repository
Version: 1.25
Release: alt1

Summary: Git::Repository - Perl interface to Git repositories
Group: Development/Perl
License: Perl

Url: %CPAN Git-Repository
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-System-Command perl-Module-Build git-core

%description
%summary

%prep
%setup -q

%build
git config --global user.email "hasher@example.com"
git config --global user.name "Hasher Bot"
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Git/Repository*
%perl_vendor_privlib/Test/Git.pm
%doc Changes README 

%changelog
* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.25-alt1
- 1.22 -> 1.25

* Mon Sep 19 2011 Vladimir Lettiev <crux@altlinux.ru> 1.22-alt1
- 1.20 -> 1.22

* Fri Jun 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt1
- New version 1.20

* Thu Jun 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt1
- initial build
