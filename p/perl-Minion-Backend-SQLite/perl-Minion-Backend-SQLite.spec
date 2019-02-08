%define _unpackaged_files_terminate_build 1

Name:           perl-Minion-Backend-SQLite
Version:        4.002
Release:        alt1
Summary:        SQLite backend for Minion job queue
License:        Artistic 2.0
Group: 		Development/Perl
URL:            https://metacpan.org/release/Minion-Backend-SQLite/
Source:        	%name-%version.tar

BuildArch:      noarch
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Mojo/Base.pm)
BuildRequires:  perl(Mojo/SQLite.pm)
BuildRequires:  perl(Mojo/Util.pm)
BuildRequires:  perl(Sys/Hostname.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Minion.pm)
BuildRequires:  perl(Minion/Backend.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(Mojo/IOLoop.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)

%description
Minion::Backend::SQLite is a backend for Minion based on Mojo::SQLite. All
necessary tables will be created automatically with a set of migrations
named minion. If no connection string or :temp: is provided, the database
will be created in a temporary directory.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md examples LICENSE
%{perl_vendorlib}/Minion*

%changelog
* Thu Nov 29 2018 Alexandr Antonov <aas@altlinux.org> 4.002-alt1
- initial build for ALT
