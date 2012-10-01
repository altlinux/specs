Name: perl-URI-Find
Version: 20111103
Release: alt1

Summary: URI::Find - Find URIs in arbitrary text
License: Perl
Group: Development/Perl

Url: %CPAN URI-Find
# Cloned from git://github.com/schwern/uri-find.git
Source: %name-%version.tar

BuildRequires: perl-devel perl-Module-Build perl-URI
BuildArch: noarch

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/urifind
%perl_vendor_privlib/URI/Find*
%doc TODO Changes README 

%changelog
* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 20111103-alt1
- 20100505 -> 20111103

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 20100505-alt1
- initial build
