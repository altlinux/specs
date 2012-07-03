Name: perl-strictures
Version: 1.002002
Release: alt1

Summary: strictures - turn on strict and make all warnings fatal
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/p5sagit/strictures.git
Url: %CPAN strictures
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel
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
%perl_vendor_privlib/strictures*
%doc Changes

%changelog
* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.002002-alt1
- initial build
