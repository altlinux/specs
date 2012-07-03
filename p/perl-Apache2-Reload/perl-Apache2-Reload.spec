%define module Apache2-Reload
%define m_distro Apache2-Reload
%define m_name Apache2::Reload
%define m_author_id unknown
%define _enable_test 1

Name: perl-Apache2-Reload
Version: 0.10
Release: alt1

Summary: Apache2::Reload - Reload Perl Modules when Changed on Disk
Group: Development/Perl
License: Artistic
Url: http://www.cpan.org

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

BuildRequires(pre): apache2-devel
BuildRequires: apache2-mod_perl-devel

BuildArch: noarch

Source: %m_distro-%version.tar

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

%changelog
* Thu Apr 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt1
- Initial

