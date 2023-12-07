%define module_name Gtk3-Helper
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Glib.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt2
Summary: Convenience functions for the Gtk3 module
Group: Development/Perl
License: see COPYING
URL: https://github.com/potyl/perl-Gtk3-Helper

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TV/TVIGNAUD/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README COPYING Changes
%perl_vendor_privlib/G*

%changelog
* Thu Dec 07 2023 Igor Vlasenko <viy@altlinux.org> 0.06-alt2
- moved to Sisyphus as perl-App-Asciio dep

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

