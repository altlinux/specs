%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Clone.pm) perl(Crypt/CBC.pm) perl(Crypt/DES.pm) perl(ExtUtils/MakeMaker.pm) perl(HTML/FormFu.pm) perl(HTML/FormFu/Attribute.pm) perl(HTML/FormFu/ObjectUtil.pm) perl(HTML/FormFu/QueryType/CGI.pm) perl(List/MoreUtils.pm) perl(Moose.pm) perl(MooseX/Attribute/Chained.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_name HTML-FormFu-MultiForm
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.03
Release: alt2
Summary: Handle multi-page/stage forms
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/N/NI/NIGELM/%{module_name}-%{version}.tar.gz
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
%doc README Changes LICENSE
%perl_vendor_privlib/H*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2
- fixed build with new perl 5.26

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- uploaded to Sisyphus as perl-Catalyst-Controller-HTML-FormFu dependency

