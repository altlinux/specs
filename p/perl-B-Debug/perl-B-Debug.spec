Name: perl-B-Debug
Version: 1.17
Release: alt1
Summary: B::Debug - Walk Perl syntax tree, printing debug info about ops

Group: Development/Perl
License: Perl
Url: %CPAN B-Debug

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/B/Debug.pm
%doc Changes README Artistic Copying

%changelog
* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.17-alt1
- New version 1.17

* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- initial build
