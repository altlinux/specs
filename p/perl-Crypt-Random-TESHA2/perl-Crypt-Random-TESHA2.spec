# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Digest/SHA.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Statistics/Basic.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Time/HiRes.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name Crypt-Random-TESHA2
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: Random numbers using timer/schedule entropy, aka userspace voodoo entropy
Group: Development/Perl
License: perl
URL: https://github.com/danaj/Crypt-Random-TESHA2

Source0: http://cpan.org.ua/authors/id/D/DA/DANAJ/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Generate random numbers using entropy gathered from timer / scheduler jitter..
This can be used to generate non-pseudorandom data to seed a PRNG (e.g.
`srand'/`rand', the Math::Random::MT manpage, etc.) or CSPRNG (e.g. AES-CTR or
the Math::Random::ISAAC manpage).  You may use it directly or as part of a random
source module that first checks for O/S randomness sources.

Only Perl CORE modules are used, making this very portable.  However, systems
must have a high resolution timer and support `usleep' from the Time::HiRes manpage.

At installation time, measurements are taken of the estimated entropy gathered
by the timer differences.  If the results indicated we could not get good
results, then the module will consider itself "weak".  On the first use of
any of the functions that return randomness (e.g. random_bytes), the module
will carp about not being a strong randomness source.  However, two special
options, ":strong" and ":weak" may be given to the importer to change this
behavior.  If ":strong" is used, then the module will croak.  If ":weak" is
used, then no carp will be generated.  The function `is_strong' can be used
at any time for finer control.  Note that this should be an unusual case, and
neither flag has any effect if the module considers itself strong.



%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE TODO README examples
%perl_vendor_privlib/C*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

