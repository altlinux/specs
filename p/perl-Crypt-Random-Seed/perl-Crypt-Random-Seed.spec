# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Crypt/Random/TESHA2.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(IO/Socket.pm) perl(Math/Random/ISAAC.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(base.pm) perl(constant.pm)
# END SourceDeps(oneline)
%define module_version 0.03
%define module_name Crypt-Random-Seed
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: Provide strong randomness for seeding
Group: Development/Perl
License: perl
URL: https://github.com/danaj/Crypt-Random-Seed

Source0: http://cpan.org.ua/authors/id/D/DA/DANAJ/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
A simple mechanism to get strong randomness.  The main purpose of this.module is to provide a simple way to generate a seed for a PRNG such as
the Math::Random::ISAAC manpage, for use in cryptographic key generation, or as the
seed for an upstream module such as the Bytes::Random::Secure manpage.  Flags for
requiring non-blocking sources are allowed, as well as a very simple
method for plugging in a source.

The randomness sources used are, in order:

=over 4

=item User supplied.

If the constructor is called with a Source defined, then it is used.  It
is not checked vs. other flags (NonBlocking, Never, Only).

=item Win32 Crypto API.

This will use `CryptGenRandom' on Windows 2000 and `RtlGenRand' on
Windows XP and newer.  According to MSDN, these are well-seeded CSPRNGs
(FIPS 186-2 or AES-CTR), so will be non-blocking.

=item EGD / PRNGD.

This looks for sockets that speak the EGD
protocol, including PRNGD.  These are
userspace entropy daemons that are commonly used by OpenSSL, OpenSSH, and
GnuGP.  The locations searched are `/var/run/egd-pool', `/dev/egd-pool',
`/etc/egd-pool', and `/etc/entropy'.  EGD is blocking, while PRNGD is
non-blocking (like the Win32 API, it is really a seeded CSPRNG).  However
there is no way to tell them apart, so we treat it as blocking.  If your
O/S supports /dev/random, consider HAVEGED
as an alternative (a system daemon that refills /dev/random as needed).

=item /dev/random.

The strong source of randomness on most UNIX-like systems.  Cygwin uses
this, though it maps to the Win32 API.  On almost all systems this is a
blocking source of randomness -- if it runs out of estimated entropy, it
will hang until more has come into the system.  If this is an issue,
which it often is on embedded devices, running a tool such as
HAVEGED will help immensely.

=item /dev/urandom.

A nonblocking source of randomness that we label as weak, since it will
continue providing output even if the actual entropy has been exhausted.

=item TESHA2.

the Crypt::Random::TESHA2 manpage is a Perl module that generates random bytes from
an entropy pool fed with timer/scheduler variations.  Measurements and
tests are performed on installation to determine whether the source is
considered strong or weak.  This is entirely in portable userspace,
which is good for ease of use, but really requires user verification
that it is working as expected if we expect it to be strong.  The
concept is similar to the Math::TrulyRandom manpage though updated to something
closer to what TrueRand 2.1 does vs. the obsolete version 1 that
the Math::TrulyRandom manpage implements.  It is very slow and has wide speed
variability across platforms : I've seen numbers ranging from 40 to
150,000 bits per second.

=back

A source can also be supplied in the constructor.  Each of these sources will
have its debatable points about perceived strength.  E.g. Why is /dev/urandom
considered weak while Win32 is strong?  Can any userspace method such as
TrueRand or TESHA2 be considered strong?



%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE TODO Changes README examples
%perl_vendor_privlib/C*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

