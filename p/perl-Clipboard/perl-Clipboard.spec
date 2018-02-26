%define module Clipboard
%define m_distro Clipboard
%define m_name Clipboard
%define m_author_id unknown
%define _enable_test 1

Name: perl-Clipboard
Version: 0.13
Release: alt1

Summary: Cliboard - Copy and Paste with any OS

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/K/KI/KING/%m_distro-%version.tar.gz

# Automatically added by buildreq on Tue Feb 08 2011 (-bb)
BuildRequires: perl-Module-Install xclip

%description
None.

%prep
%setup -n %m_distro-%version
rm -f lib/Clipboard/MacPasteboard.pm
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Clipboard/*
%perl_vendor_privlib/Clipboard.pm

%changelog
* Tue Feb 08 2011 Denis Smirnov <mithraen@altlinux.ru> 0.13-alt1
- 0.13

* Tue Oct 27 2009 Denis Smirnov <mithraen@altlinux.ru> 0.09-alt1
- initial build for ALT Linux Sisyphus

