%define m_distro File-chmod
Name: perl-File-chmod
Version: 0.32
Release: alt1
Summary: File::chmod - Implements symbolic and ls chmod modes

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~pinyan/File-chmod/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/File/chmod*
%doc Changes 

%changelog
* Thu Jan 28 2010 Vladimir Lettiev <crux@altlinux.ru> 0.32-alt1
- initial build
