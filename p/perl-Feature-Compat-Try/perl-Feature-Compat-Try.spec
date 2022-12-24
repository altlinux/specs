%define module_name Feature-Compat-Try
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Future/AsyncAwait.pm) perl(Module/Build.pm) perl(Syntax/Keyword/Try.pm) perl(Test/More.pm) perl(XS/Parse/Keyword.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt1.1
Summary: make C<try/catch> syntax available
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module is written in the aspiration that one day perl will gain true
native syntax support for `try/catch' control flow, and that it will be
spelled using the syntax defined here. The intention here is that on such
a version of perl that provides this syntax this module will simply enable it,
equivalent to perhaps

   use feature 'try';

On older versions of perl before such syntax is available, it is currently
provided instead using the the Syntax::Keyword::Try manpage module, imported with a
special set of options to configure it to recognise exactly and only the same
syntax as this as-yet-aspirational core perl feature, thus ensuring that any
code using it will still continue to function on that newer perl.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/F*

%changelog
* Thu Dec 01 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Thu Feb 24 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt1
- updated by package builder

* Wed Apr 14 2021 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

