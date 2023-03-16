%define module_name MaxMind-DB-Reader
%define _unpackaged_files_terminate_build 1
# due Net-Works->Int128 deps
ExcludeArch: %ix86 armh

Name: perl-%module_name
Version: 1.000014
Release: alt3
Summary: Read MaxMind DB files and look up IP addresses
Group: Development/Perl
License: %artistic_license_v2
URL: http://metacpan.org/release/MaxMind-DB-Reader

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MAXMIND/%{module_name}-%{version}.tar.gz

# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Cpanel/JSON/XS.pm) perl(Data/IEEE754.pm) perl(Data/Printer.pm) perl(Data/Validate/IP.pm) perl(DateTime.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurper.pm) perl(File/Spec.pm) perl(Getopt/Long.pm) perl(List/AllUtils.pm) perl(Math/BigInt.pm) perl(Math/Int128.pm) perl(MaxMind/DB/Common.pm) perl(MaxMind/DB/Metadata.pm) perl(MaxMind/DB/Role/Debugs.pm) perl(MaxMind/DB/Types.pm) perl(Module/Implementation.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/StrictConstructor.pm) perl(Net/Works/Network.pm) perl(Path/Class.pm) perl(Role/Tiny.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/Bits.pm) perl(Test/Fatal.pm) perl(Test/MaxMind/DB/Common/Data.pm) perl(Test/MaxMind/DB/Common/Util.pm)
BuildRequires: perl(Test/More.pm) perl(Test/Number/Delta.pm) perl(Test/Requires.pm) perl(autodie.pm) perl(bytes.pm) perl(constant.pm) perl(lib.pm) perl(namespace/autoclean.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
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

%files
%doc LICENSE Changes README.md CONTRIBUTING.md
%perl_vendor_privlib/M*

%files scripts
%_bindir/*

%changelog
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

