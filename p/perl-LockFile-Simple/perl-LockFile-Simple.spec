%define module LockFile-Simple

Name: perl-%module
Version: 0.207
Release: alt1.1

Summary: %{module} module for perl
License: Artistic
Group: Development/Perl

Source: %module-%version.tar.gz
BuildArch: noarch

Packager: Afanasov Dmitry <ender@altlinux.org>

# Automatically added by buildreq on Mon Oct 06 2003
BuildRequires: perl-devel

%description
%{module} module for perl

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%perl_vendor_privlib/LockFile*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.207-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 05 2008 Afanasov Dmitry <ender@altlinux.org> 0.207-alt1
- 0.207 release

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.5-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Oct 06 2003 Michael Shigorin <mike@altlinux.ru> 0.2.5-alt1
- built for ALT Linux

