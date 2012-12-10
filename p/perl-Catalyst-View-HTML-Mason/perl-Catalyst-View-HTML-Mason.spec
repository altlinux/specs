# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Catalyst/ScriptRunner.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Catalyst-View-HTML-Mason
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Helper for L<Catalyst::View::HTML::Mason> views
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture/Tiny.pm)
BuildRequires: perl(Catalyst.pm)
BuildRequires: perl(Catalyst/Action/RenderView.pm)
BuildRequires: perl(Catalyst/Controller.pm)
BuildRequires: perl(Catalyst/Helper.pm)
BuildRequires: perl(Catalyst/Runtime.pm)
BuildRequires: perl(Catalyst/Test.pm)
BuildRequires: perl(Catalyst/View.pm)
BuildRequires: perl(Data/Visitor/Callback.pm)
BuildRequires: perl(Encode/Encoding.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(FindBin.pm)
BuildRequires: perl(HTML/Mason.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Moose/Util/TypeConstraints.pm)
BuildRequires: perl(MooseX/Types/Moose.pm)
BuildRequires: perl(MooseX/Types/Structured.pm)
BuildRequires: perl(Path/Class.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(namespace/autoclean.pm)
BuildRequires: perl(utf8.pm)
BuildArch: noarch
Source44: import.info

%description
This module provides rendering of HTML::Mason templates for Catalyst
applications.

It's basically a rewrite of Catalyst::View::Mason, which became
increasingly hard to maintain over time, while keeping backward
compatibility.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.18-alt1_1
- mageia import by cas@ requiest

