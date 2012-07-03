Name: perl-URI-Find
Version: 20100505
Release: alt1
Summary: URI::Find - Find URIs in arbitrary text

Group: Development/Perl
License: Perl
Url: %CPAN URI-Find

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Build perl-URI

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
* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 20100505-alt1
- initial build
