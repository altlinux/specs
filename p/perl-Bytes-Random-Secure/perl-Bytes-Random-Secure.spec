%define module_version 0.28
%define module_name Bytes-Random-Secure
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Crypt/Random/Seed.pm) perl(Digest/SHA.pm) perl(English.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(MIME/Base64.pm) perl(MIME/QuotedPrint.pm) perl(Math/Random/ISAAC.pm) perl(Scalar/Util.pm) perl(Test/Kwalitee.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Time/HiRes.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.28
Release: alt2
Summary: Perl extension to generate cryptographically-secure random bytes.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DA/DAVIDO/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
the Bytes::Random::Secure manpage provides two interfaces for obtaining crypto-quality.random bytes.  The simple interface is built around plain functions.  For
greater control over the Random Number Generator's seeding, there is an Object
Oriented interface that provides much more flexibility.

The "functions" interface provides functions that can be used any time you need
a string of a specific number of random bytes.  The random bytes are available
as simple strings, or as hex-digits, Quoted Printable, or MIME Base64.  There
are equivalent methods available from the OO interface, plus a few others.

This module can be a drop-in replacement for the Bytes::Random manpage, with the primary
enhancement of using a cryptographic-quality random number generator to create
the random data.  The `random_bytes' function emulates the user interface of
the Bytes::Random manpage's function by the same name.  But with Bytes::Random::Secure
the random number generator comes from the Math::Random::ISAAC manpage, and is suitable
for cryptographic purposes.  The harder problem to solve is how to seed the
generator.  This module uses the Crypt::Random::Seed manpage to generate the initial
seeds for Math::Random::ISAAC.

In addition to providing `random_bytes()', this module also provides several
functions not found in the Bytes::Random manpage: `random_string_from',
`random_bytes_base64()', `random_bytes_hex', and `random_bytes_qp'.

And finally, for those who need finer control over how the Crypt::Random::Seed manpage
generates its seed, there is an object oriented interface with a constructor
that facilitates configuring the seeding process, while providing methods that
do everything the "functions" interface can do (truth be told, the functions
interface is just a thin wrapper around the OO version, with some sane defaults
selected).  The OO interface also provides an `irand' method, not available
through the functions interface.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/B*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- regenerated from template by package builder

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- initial import by package builder

