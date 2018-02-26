Name: perl-Module-Install-CheckLib
Version: 0.08
Release: alt1
Summary: Module::Install::CheckLib - A Module::Install extension to check that a library is available

Group: Development/Perl
License: Perl
Url: %CPAN Module-Install-CheckLib

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires: perl-Devel-CheckLib perl-devel perl-Module-Install perl-Module-Install-AuthorTests perl-Capture-Tiny perl-Module-Install-ReadmeFromPod

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/CheckLib*
%doc Changes README 

%changelog
* Tue Aug 23 2011 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
