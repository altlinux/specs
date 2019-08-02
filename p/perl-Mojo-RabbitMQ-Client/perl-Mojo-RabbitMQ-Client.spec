Name: perl-Mojo-RabbitMQ-Client
Version: 0.2.3
Release: alt1
Summary: Mojo::IOLoop based RabbitMQ client
License: Artistic 2.0 and BSD
Group: Development/Perl
Url: https://metacpan.org/release/Mojo-RabbitMQ-Client
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl(Module/Build/Tiny.pm)
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(Net/AMQP.pm)

%description
Mojo::RabbitMQ::Client is a rewrite of AnyEvent::RabbitMQ to work on top of
Mojo::IOLoop.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/Mojo*
%perl_vendorlib/auto
%doc examples Changes README.md

%changelog
* Wed Jul 31 2019 Alexandr Antonov <aas@altlinux.org> 0.2.3-alt1
- initial build for ALT

