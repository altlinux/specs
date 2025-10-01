%define module_name Log-Syslog-Constants
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 1.02
Release: alt1
Summary: Perl extension containing syslog priority constants as defined in RFC3164
Group: Development/Perl
License: %perl_license
URL: %CPAN %module_name
Vcs: https://github.com/athomason/Log-Syslog-Constants

Source0: https://cpan.metacpan.org/authors/id/A/AT/ATHOMASON/%module_name-%version.tar

BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires(pre): rpm-build-licenses

BuildArch: noarch

%description
%summary

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/L*

%changelog
* Thu Sep 18 2025 L.A. Kostis <lakostis@altlinux.ru> 1.02-alt1
- Initial build for ALTLinux.


