Name: perl-Object-Event
Version: 1.23
Release: alt1
Summary: Object::Event - A class that provides an event callback interface

Group: Development/Perl
License: Perl
Url: %CPAN Object-Event

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-common-sense perl-AnyEvent

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Object/Event*
%doc Changes

%changelog
* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 1.23-alt1
- initial build
