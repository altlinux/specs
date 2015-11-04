# BEGIN SourceDeps(oneline):
BuildRequires: libgtk+3-gir perl(ExtUtils/MakeMaker.pm) perl(Gtk3.pm)
# END SourceDeps(oneline)
%define module_version 0.15
%define module_name Gtk3-SimpleList
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.15
Release: alt1
Summary: A simple interface to Gtk3's complex MVC list widget
Group: Development/Perl
License: perl
URL: https://github.com/potyl/perl-Gtk3-SimpleList

Source0: http://cpan.org.ua/authors/id/T/TV/TVIGNAUD/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes COPYING
%perl_vendor_privlib/G*

%changelog
* Wed Nov 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

