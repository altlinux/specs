%define module_name Module-Build-Using-PkgConfig
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/PkgConfig.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: extend C<Module::Build> to more easily use platform libraries provided by F<pkg-config>
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This subclass of the Module::Build manpage provides some handy methods to assist the
Build.PL script of XS-based module distributions that make use of platform
libraries managed by pkg-config.

As well as supporting libraries installed on a platform-wide basis and thus
visible to pkg-config itself, this subclass also assists with
`Alien::'-based wrappers of these system libraries, allowing them to be
dynamically installed at build time if the platform does not provide them.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_privlib/M*

%changelog
* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- to Sisyphus as perl-Net-LibAsyncNS dep

* Fri Apr 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- updated by package builder

* Thu Feb 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

