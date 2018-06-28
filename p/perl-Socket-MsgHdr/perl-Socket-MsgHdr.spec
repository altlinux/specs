%define _unpackaged_files_terminate_build 1
%define sname socket-msghdr

Name: perl-Socket-MsgHdr
Version: 0.04
Release: alt1
Summary: Sendmsg, recvmsg and ancillary data operations
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Socket-MsgHdr/
Source: %sname-%version.tar

BuildRequires: findutils
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(bytes.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(Socket.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(XSLoader.pm)

%description
Socket::MsgHdr provides advanced socket messaging operations via sendmsg
and recvmsg. Like their C counterparts, these functions accept few
parameters, instead stuffing a lot of information into a complex structure.

%prep
%setup -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendorarch/auto/Socket/MsgHdr*
%perl_vendorarch/Socket*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.04-alt1
- initial build for ALT
