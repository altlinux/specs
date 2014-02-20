# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Clone.pm) perl(Crypt/CBC.pm) perl(Crypt/DES.pm) perl(ExtUtils/MakeMaker.pm) perl(HTML/FormFu.pm) perl(HTML/FormFu/Attribute.pm) perl(HTML/FormFu/ObjectUtil.pm) perl(HTML/FormFu/QueryType/CGI.pm) perl(List/MoreUtils.pm) perl(Moose.pm) perl(MooseX/Attribute/Chained.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/Aggregate/Nested.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 1.00
%define module_name HTML-FormFu-MultiForm
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00
Release: alt1
Summary: Handle multi-page/stage forms
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/C/CF/CFRANKS/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/H*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- uploaded to Sisyphus as perl-Catalyst-Controller-HTML-FormFu dependency

