%def_without test
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBI.pm) perl(ExtUtils/MakeMaker.pm) perl(File/stat.pm) perl(Tk.pm) perl(Tk/Button.pm) perl(Tk/Derived.pm) perl(Tk/Frame.pm) perl(Tk/Listbox.pm) perl(Tk/Pane.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 1.11
%define module_name Tk-MListbox
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.11
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/R/RC/RCS/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n MListbox-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc readme Changes docs
%perl_vendor_privlib/T*

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2
- to Sisyphus

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- initial import by package builder

