# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_version 0.03
%define module_name Math-GMPn
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2.1.1.1.1
Summary: Fixed length integer arithmetic.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SA/SALVA/%module_name-%module_version.tar.gz

%description
This module provides a set of functions to perform arithmetic on fixed
length but arbitrarily large bit strings implemented on top of the GMP
library low level functions (see
http://gmplib.org/manual/Low_002dlevel-Functions.html).

Numbers are represented as arrays of GMP mp_limb_t integers (usually,
the native unsigned int) packed into Perl scalars without any
additional wrapping.

The bit length of the strings passed to the module must be a multiple
of the mp_limb_t bit size (32 and 64 bits for 32bit and 64bit machines
respectively). Most operations do not check that condition and their
results are unspecified when arguments with non conforming sizes are
used.

Also, the strings passed must by internally aligned on a mp_limb_t
boundary. That usually means not using the four argument variant of
`substr' on any scalar that would be passed to Math::GMPn. For
instance:

  # don't do that:
  $a = ...; $b = ...;
  substr($a, 0, 3, "");
  mpn_add($r, $a, $b); # croaks!

When strings of different length are used on the same operation, the
result lenght is equal to that of the largest input. For instance,
adding a 128bit string and a 256bit string will output a 256bit
string. Overflows are silently discarded.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2.1
- rebuild with new perl 5.20.1

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

