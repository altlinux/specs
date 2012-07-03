Name: perl-Net-OpenSSH
Version: 0.57
Release: alt1

Summary: Net::OpenSSH - Perl SSH client package implemented on top of OpenSSH
Group: Development/Perl
License: Perl

# Cloned from https://github.com/salva/p5-Net-OpenSSH.git
Source: %name-%version.tar
Url: %CPAN Net-OpenSSH

BuildArch: noarch
BuildRequires: openssh-clients perl-devel

%add_findreq_skiplist */OpenSSH/More.pm

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/OpenSSH*
%doc Changes README 

%changelog
* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.57-alt1
- 0.57

* Wed Aug 24 2011 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- initial build
