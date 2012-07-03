%define m_distro Directory-Scratch
Name: perl-Directory-Scratch
Version: 0.14
Release: alt1
Summary: Easy-to-use self-cleaning scratch space

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~jrockway/Directory-Scratch/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-File-Slurp perl-Path-Class perl-devel perl-Module-Install

%description
Directory::Scratch creates a scratch space for your application to
(portably) manipulate files.  Designed for testing File::* modules,
but may be useful elsewhere.

%prep
%setup -q -n %m_distro-%version
rm -rf t/os

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Directory/Scratch*
%doc Changes README 

%changelog
* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
