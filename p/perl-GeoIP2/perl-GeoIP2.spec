%define module_name GeoIP2
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 2.006002
Release: alt4
Summary: Perl API for MaxMind's GeoIP2 web services and databases
Group: Development/Perl
License: %perl_license
URL: http://metacpan.org/release/GeoIP2

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MAXMIND/%{module_name}-%{version}.tar.gz

%ifnarch %ix86 %arm
# required for test data
BuildRequires: perl(Net/Works/Network.pm) perl(Math/Int128.pm)
%else
%define _without_test 1
%endif
# see https://bugzilla.altlinux.org/show_bug.cgi?id=45638
%def_disable girar_repacks_srpm
%if_enabled  girar_repacks_srpm
BuildArch: noarch
%endif

# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cpanel/JSON/XS.pm) perl(Data/Validate/IP.pm) perl(File/Slurper.pm) perl(HTTP/Headers.pm) perl(HTTP/Request.pm) perl(HTTP/Response.pm) perl(HTTP/Status.pm) perl(IO/Compress/Gzip.pm) perl(JSON/MaybeXS.pm) perl(LWP/Protocol/https.pm) perl(LWP/UserAgent.pm) perl(List/SomeUtils.pm) perl(MaxMind/DB/Metadata.pm) perl(MaxMind/DB/Reader.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Params/Validate.pm) perl(Path/Class.pm) perl(Sub/Quote.pm) perl(Test/Fatal.pm) perl(Test/MaxMind/DB/Common/Util.pm) perl(Test/Number/Delta.pm) perl(Throwable/Error.pm) perl(Try/Tiny.pm) perl(URI.pm) perl(autodie.pm) perl(namespace/clean.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires(pre): rpm-build-licenses

%description
This distribution provides an API for the GeoIP2
web services and
databases. The API also
works with the free
GeoLite2 databases.

See the GeoIP2::WebService::Client manpage for details on the web service
client API and the GeoIP2::Database::Reader manpage for the database API.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %EVR

%description scripts
scripts for %module_name
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%if_disabled  girar_repacks_srpm
# something fake arch-like to bypass girar checks
mkdir -p %buildroot%perl_vendor_autolib/%module_name
%endif

%files
%doc CONTRIBUTING.md Changes README.md LICENSE
%perl_vendor_privlib/G*
%if_disabled  girar_repacks_srpm
%perl_vendor_autolib/%module_name
%endif

%files scripts
%_bindir/*

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 2.006002-alt4
- restored build on 32-bit arches
- updated BuildRequires

* Fri Mar 10 2023 L.A. Kostis <lakostis@altlinux.ru> 2.006002-alt3
- Exclude 32-bit arches.

* Thu Mar 09 2023 L.A. Kostis <lakostis@altlinux.ru> 2.006002-alt2
- Fix license.

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.006002-alt1
- updated by package builder

* Wed Sep 12 2018 Igor Vlasenko <viy@altlinux.ru> 2.006001-alt1
- regenerated from template by package builder

* Wed Apr 11 2018 Igor Vlasenko <viy@altlinux.ru> 2.005001-alt1
- regenerated from template by package builder

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 2.005000-alt1
- regenerated from template by package builder

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.004000-alt1
- regenerated from template by package builder

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.003005-alt1
- regenerated from template by package builder

* Fri Mar 24 2017 Igor Vlasenko <viy@altlinux.ru> 2.003004-alt1
- regenerated from template by package builder

* Mon Feb 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.003003-alt1
- regenerated from template by package builder

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.003002-alt1
- regenerated from template by package builder

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.003001-alt1
- initial import by package builder
