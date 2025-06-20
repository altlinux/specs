%define _unpackaged_files_terminate_build 1

Name: perl-Memory-Process
Version: 0.06
Release: alt1

Summary: Memory::Process - Perl class to determine actual memory usage
License: BSD-2-Clause
Group: Development/Perl
URL: https://metacpan.org/pod/Memory::Process
Vcs: https://github.com/michal-josef-spacek/Memory-Process
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: perl-devel
BuildRequires: perl-Capture-Tiny
BuildRequires: perl-Readonly
BuildRequires: perl-Memory-Usage
# Tests depenedencies
BuildRequires: /proc
BuildRequires: perl-Test-NoWarnings

%description
%summary.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Memory*

%changelog
* Wed Jun 11 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.06-alt1
- Initial build.
