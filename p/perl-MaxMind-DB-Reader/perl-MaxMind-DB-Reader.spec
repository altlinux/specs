%define module_name MaxMind-DB-Reader
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 1.000014
Release: alt4
Summary: Read MaxMind DB files and look up IP addresses
Group: Development/Perl
License: %artistic_license_v2
URL: http://metacpan.org/release/MaxMind-DB-Reader

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
BuildRequires: perl(Cpanel/JSON/XS.pm) perl(Data/IEEE754.pm) perl(Data/Printer.pm) perl(Data/Validate/IP.pm) perl(DateTime.pm) perl(Encode.pm) perl(File/Slurper.pm) perl(List/AllUtils.pm) perl(Math/BigInt.pm) perl(MaxMind/DB/Common.pm) perl(MaxMind/DB/Metadata.pm) perl(MaxMind/DB/Role/Debugs.pm) perl(MaxMind/DB/Types.pm) perl(Module/Implementation.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/StrictConstructor.pm) perl(Path/Class.pm) perl(Role/Tiny.pm) perl(Test/Bits.pm) perl(Test/Fatal.pm) perl(Test/MaxMind/DB/Common/Data.pm) perl(Test/MaxMind/DB/Common/Util.pm) perl(Test/Number/Delta.pm) perl(Test/Requires.pm) perl(autodie.pm) perl(namespace/autoclean.pm)
# END SourceDeps(oneline)

BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-perl perl-devel perl-podlators

%description
This module provides a low-level interface to the MaxMind DB file format.

If you are looking for an interface to MaxMind's GeoIP2 or GeoLite2 downloadable databases, you should also check
out the the GeoIP2 manpage distribution. That distribution provides a higher level OO
interface to those databases.

This API will work with any MaxMind DB databases, regardless of whether it is
a GeoIP2 database or not. In addition, if speed is critical, this API will
always be faster than the the GeoIP2 manpage modules, since it returns results as a raw
Perl data structure rather than as an object.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

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
%doc LICENSE Changes README.md CONTRIBUTING.md
%perl_vendor_privlib/M*
%if_disabled  girar_repacks_srpm
%perl_vendor_autolib/%module_name
%endif

%files scripts
%_bindir/*

%changelog
* Wed Mar 22 2023 Igor Vlasenko <viy@altlinux.org> 1.000014-alt4
- restored build on 32-bit arches
- updated BuildRequires

* Fri Mar 10 2023 L.A. Kostis <lakostis@altlinux.ru> 1.000014-alt3
- Exclude 32-bit arches.

* Tue Mar 07 2023 L.A. Kostis <lakostis@altlinux.ru> 1.000014-alt2
- Fix License.

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.000014-alt1
- updated by package builder

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.000013-alt1
- regenerated from template by package builder

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.000012-alt1
- initial import by package builder

