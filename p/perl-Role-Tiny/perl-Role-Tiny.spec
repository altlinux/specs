Name: perl-Role-Tiny
Version: 1.000000
Release: alt1

Summary: Role::Tiny - minimalist role composition tool
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/gitmo/Role-Tiny.git
Url: %CPAN Role-Tiny
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-MRO-Compat perl-devel perl-Class-Method-Modifiers perl-Test-Fatal
BuildArch: noarch

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Role/Tiny*
%doc Changes

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000000-alt1
- initial build

