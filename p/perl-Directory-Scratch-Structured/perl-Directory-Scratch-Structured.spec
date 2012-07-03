%define m_distro Directory-Scratch-Structured
Name: perl-Directory-Scratch-Structured
Version: 0.04
Release: alt1
Summary: creates temporary files and directories from a structured description

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~nkh/Directory-Scratch-Structured/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Module-Build perl-Readonly perl-Sub-Exporter perl-Sub-Install perl-Data-TreeDumper perl-Directory-Scratch perl-Test-Exception perl-Test-NoWarnings perl-Test-Warn perl-Test-Block perl-Test-Strict

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Directory/Scratch/Structured*
%doc Changes README 

%changelog
* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build
