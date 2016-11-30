%define module_version 1.27
%define module_name Mango
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Authen/SCRAM/Client.pm) perl(B.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Hash/Util/FieldHash.pm) perl(List/Util.pm) perl(Mojolicious.pm) perl(Scalar/Util.pm) perl(Sys/Hostname.pm) perl(Time/HiRes.pm) perl(overload.pm) perl(re.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.27
Release: alt2
Summary: Pure-Perl non-blocking I/O MongoDB driver
Group: Development/Perl
License: artistic_2
URL: http://mojolicio.us

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/O/OD/ODC/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch
Patch: Mango-1.27-no64-todo.patch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}
if [ %version == 1.27 ]; then
%patch -p1
%define _without_test 1
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/M*

%changelog
* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.27-alt2
- to Sisyphus

* Sun Apr 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

