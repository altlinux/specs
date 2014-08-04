%define _unpackaged_files_terminate_build 1
%define module Apache-Reload
%define m_distro Apache-Reload
%define m_name Apache2::Reload
%define m_author_id unknown
%define _enable_test 1

Name: perl-Apache-Reload
Version: 0.12
Release: alt1

Summary: Apache2::Reload - Reload Perl Modules when Changed on Disk
Group: Development/Perl
License: Artistic
Url: http://www.cpan.org

BuildRequires(pre): apache2-devel
BuildRequires: apache2-mod_perl-devel

BuildArch: noarch

Source: http://www.cpan.org/authors/id/P/PH/PHRED/Apache-Reload-%{version}.tar.gz

Conflicts: perl-Apache2-Reload < 0.11
Obsoletes: perl-Apache2-Reload < 0.11

%description
Apache2::Reload reloads modules that change on the disk.

When Perl pulls a file via require, it stores the filename in the global hash %%INC.
The next time Perl tries to require the same file, it sees the file in %%INC and does
not reload from disk. This module's handler can be configured to iterate over the
modules in %%INC and reload those that have changed on disk or only specific modules
that have registered themselves with Apache2::Reload. It can also do the check for
modified modules, when a special touch-file has been modified.

%prep
%setup -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/*

%files
%perl_vendor_privlib/Apache2/*
%perl_vendor_privlib/Apache/*

%changelog
* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- renamed to Apache-Reload
- automated CPAN update

* Thu Apr 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt1
- Initial

