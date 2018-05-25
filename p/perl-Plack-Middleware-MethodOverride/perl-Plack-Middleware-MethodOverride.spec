%define _unpackaged_files_terminate_build 1
%define module_name Plack-Middleware-MethodOverride
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Plack/Middleware.pm) perl(Plack/Request.pm) perl(Plack/Test.pm) perl(Plack/Util/Accessor.pm) perl(Test/More.pm) perl(URI.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm) perl(Cpanel/JSON/XS.pm) perl(Module/Build/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.18
Release: alt1
Summary: Override REST methods to Plack apps via POST
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/Plack-Middleware-MethodOverride/

Source0: http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{module_name}-%{version}.tar.gz
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
%doc LICENSE Changes README
%perl_vendor_privlib/P*

%changelog
* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- fixed build

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- moved to Sisyphus as perl update dependency

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- initial import by package builder

