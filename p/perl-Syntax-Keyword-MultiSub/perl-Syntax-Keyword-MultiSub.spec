%define module_name Syntax-Keyword-MultiSub
#BuildRequires: perl(Future/AsyncAwait.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(XS/Parse/Sublike.pm) perl(XS/Parse/Sublike/Builder.pm) perl(experimental.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: multiple dispatch on subroutines
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides a new keyword, `multi', to put before subroutine
declarations, which permits multiple distinct function bodies to be provided,
which take different parameters. A call to a `multi sub' will invoke
whichever function body best fits the arguments passed.

Currently this module can only make dispatching decisions based on the number
of arguments as compared to the number of signature parameters each body was
expecting. It requires perl version 5.26 or above, in order to get enough
support from signatures. Note also enabling this module does not enable the
`signatures' feature; you must do that independently.

%prep
%setup -q -n %{module_name}-%{version}

%ifarch %arm
rm -f t/01multi.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.02-alt2
- to Sisyphus as Future-AsyncAwait dependency

* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.02-alt1
- updated by package builder

* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

