## SPEC file for Perl module Git::Wrapper

%define real_name Git-Wrapper

Name: perl-Git-Wrapper
Version: 0.047
Release: alt1

Summary: Wrap git command-line interface

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Git-Wrapper/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Encode perl-Sub-Uplevel perl-devel perl-parent python-base python-modules python3-base
BuildRequires: git-core perl-Devel-CheckBin perl-File-chdir perl-IPC-Cmd perl-Path-Class perl-Sort-Versions perl-Test-Deep perl-Test-Exception

%description
Perl module Git::Wrapper provides an API for git(7) that uses
Perl data structures for argument passing, instead of 
CLI-style --options as Git does.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/Git/Wrapper*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.047-alt1
- Initial build for ALT Linux Sisyphus
