%define module_name Data-MethodProxy
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(Module/Build/Tiny.pm) perl(Module/Runtime.pm) perl(Scalar/Util.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Inject dynamic data into static data.
Group: Development/Perl
License: perl
URL: https://github.com/bluefeet/Data-MethodProxy

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BL/BLUEFEET/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
A method proxy is an array ref describing a class method to call and the
arguments to pass to it.  The first value of the array ref is the scalar
`$proxy', followed by a package name, then a subroutine name which must
callable in the package, and a list of any subroutine arguments.

    [ '$proxy', 'Foo::Bar', 'baz', 123, 4 ]

The above is saying, do this:

    Foo::Bar->baz( 123, 4 );

The the render entry elsewhere in this document method is the main entry point for replacing all found
method proxies in an arbitrary data structure with the return value of
calling the methods.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes
%perl_vendor_privlib/C*
%perl_vendor_privlib/D*

%changelog
* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 0.05-alt2
- to Sisyphus as MooX-Role-Parameterized dep

* Fri Feb 05 2021 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Mon Apr 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

