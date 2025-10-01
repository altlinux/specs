%define module_name Log-Syslog-Fast
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 0.68
Release: alt1
Summary: Perl extension for sending syslog messages over TCP, UDP, or UNIX sockets with minimal CPU overhead
Group: Development/Perl
License: %perl_license
URL: %CPAN %module_name
Vcs: https://github.com/athomason/Log-Syslog-Fast

Source0: https://cpan.metacpan.org/authors/id/A/AT/ATHOMASON/%module_name-%version.tar

BuildRequires: rpm-build-perl perl-devel perl-podlators perl-Log-Syslog-Constants perl-IO-Socket-IP
BuildRequires(pre): rpm-build-licenses

# never worked on %%ix86
ExclusiveArch: x86_64 aarch64

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
%perl_vendor_archlib/L*
%perl_vendor_autolib/L*

%changelog
* Thu Sep 18 2025 L.A. Kostis <lakostis@altlinux.ru> 0.68-alt1
- Initial build for ALTLinux.

