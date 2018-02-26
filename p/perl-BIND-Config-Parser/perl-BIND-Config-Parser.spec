%define module BIND-Config-Parser
%define m_distro BIND-Config-Parser
%define m_name BIND::Config::Parser
%define m_author_id unknown
%define _enable_test 1

Name: perl-BIND-Config-Parser
Version: 0.01
Release: alt1

Summary: Parse BIND Config file

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Egor Glukhov <kaman@altlinux.org>

BuildArch: noarch
Source: %name-%version.tar

# Automatically added by buildreq on Tue Aug 03 2010
BuildRequires: perl-Parse-RecDescent perl-devel

%description
BIND::Config::Parser provides a lightweight parser to the configuration
file syntax of BIND v8 and v9 using a "Parse::RecDescent" grammar.

It is in a similar vein to "BIND::Conf_Parser". However, as it has no
knowledge of the directives, it doesn't need to be kept updated as new
directives are added, it simply knows how to carve up a BIND configuration
file into logical chunks.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf -- %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/BIND/*

%changelog
* Tue Aug 03 2010 Egor Glukhov <kaman@altlinux.org> 0.01-alt1
- initial build for ALT Linux Sisyphus

