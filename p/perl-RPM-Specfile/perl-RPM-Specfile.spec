%define module RPM-Specfile

Name: perl-%module
Version: 1.51
Release: alt2.1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: RPM::Specfile - Perl extension for creating RPM Specfiles
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/RPM-Specfile
Patch0: RPM-Specfile-1.51-add-conflicts.patch
Patch1: RPM-Specfile-1.19-ALT-no-buildroot.patch

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel

%description
This is a simple module for creation of RPM Spec files.

%prep
%setup -q -n %module-%version
%patch -p1
%patch1 -p0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.51-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.51-alt2
- removed perl dir ownership

* Mon Jan 29 2007 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- new version

* Tue Nov 15 2005 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- First build for Sisyphus.
