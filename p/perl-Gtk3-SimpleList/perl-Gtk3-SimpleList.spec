%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: libgtk+3-gir perl(ExtUtils/MakeMaker.pm) perl(Gtk3.pm)
# END SourceDeps(oneline)
%define module_name Gtk3-SimpleList
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.17
Release: alt1.1
Summary: A simple interface to Gtk3's complex MVC list widget
Group: Development/Perl
License: perl
URL: https://github.com/potyl/perl-Gtk3-SimpleList

Source0: http://www.cpan.org/authors/id/T/TV/TVIGNAUD/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes COPYING
%perl_vendor_privlib/G*

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Wed Nov 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

