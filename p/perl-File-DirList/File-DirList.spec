%define _unpackaged_files_terminate_build 1
%define dist File-DirList
Name: perl-%dist
Version: 0.05
Release: alt1

Summary: provide a sorted list of directory content
License: Perl
Group: Development/Perl
URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RE/REHSACK/%{dist}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File



%changelog
* Mon Jun 20 2022 Fr. Br. George <george@altlinux.org> 0.05-alt1
- Initial build for ALT
