# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Test/More.pm) perl(Text/Template.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name Module-CAPIMaker
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires(pre): rpm-build-licenses

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: Provide a C API for your XS modules
Group: Development/Perl
License: %perl_license
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SA/SALVA/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/M*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Thu Mar 09 2023 L.A. Kostis <lakostis@altlinux.ru> 0.01-alt2
- Rebuild by human.

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

