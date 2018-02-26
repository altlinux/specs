%define module RT-Extension-ColumnMap
%define m_distro RT-Extension-ColumnMap
%define m_name RT::Extension::ColumnMap
%define m_author_id unknown
%def_without test

Name: request-tracker-extension-ColumnMap
Version: 0.02
Release: alt1

Summary: This extension provides API to turn ColumnMap like strings into values

License: GPL or Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %m_distro-%version.tar

# Automatically added by buildreq on Tue Mar 30 2010 (-bi)
BuildRequires: perl-Regexp-Common-WithActions perl-Storable perl-devel

%add_findreq_skiplist /usr/lib/rt/local/plugins/RT-Extension-ColumnMap/lib/RT/Extension/ColumnMap/Test.pm

%description
This extension provides API to turn ColumnMap like strings into values.
It can be used in other extensions and/or local customizations.


%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
mkdir -p %buildroot%_libexecdir/rt/local/plugins/%module/
cp -rp lib %buildroot%_libexecdir/rt/local/plugins/%module/

%files
%_libexecdir/rt/local/plugins/%module

%changelog
* Thu Apr 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.02-alt1
- Initial build for Sisyphus
