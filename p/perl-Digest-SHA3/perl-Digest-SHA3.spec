%define module_name Digest-SHA3
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Digest/base.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.04
Release: alt3
Summary: Perl extension for SHA-3
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MS/MSHELOR/%{module_name}-%{version}.tar.gz

%description
Digest::SHA3 is written in C for speed.  If your platform lacks a C
compiler, perhaps you can find the module in a binary form compatible
with your particular processor and operating system.

The programming interface is easy to use: it's the same one found
in CPAN's the Digest manpage module.  So, if your applications currently use
the Digest::SHA manpage and you'd prefer the newer flavor of the NIST standard,
it's a simple matter to convert them.

The interface provides two ways to calculate digests:  all-at-once,
or in stages.  To illustrate, the following short program computes
the SHA3-256 digest of "hello world" using each approach:

_use Digest::SHA3 qw(sha3_256_hex);

_$data = "hello world";
_@frags = split(//, $data);

_# all-at-once (Functional style)
_$digest1 = sha3_256_hex($data);

_# in-stages (OOP style)
_$state = Digest::SHA3->new(256);
_for (@frags) { $state->add($_) }
_$digest2 = $state->hexdigest;

_print $digest1 eq $digest2 ?
__"that's the ticket!\n" : "oops!\n";

To calculate the digest of an n-bit message where *n* is not a
multiple of 8, use the *add_bits()* method.  For example, consider
the 446-bit message consisting of the bit-string "110" repeated
148 times, followed by "11".  Here's how to display its SHA3-512
digest:

_use Digest::SHA3;
_$bits = "110" x 148 . "11";
_$sha3 = Digest::SHA3->new(512)->add_bits($bits);
_print $sha3->hexdigest, "\n";

Note that for larger bit-strings, it's more efficient to use the
two-argument version *add_bits($data, $nbits)*, where *$data* is
in the customary packed binary format used for Perl strings.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description scripts
scripts for %module_name


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3
- to Sisyphus as Crypt-CBC dep

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 1.04-alt1.1
- rebuild with perl 5.28.1

* Tue Apr 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- regenerated from template by package builder

* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- regenerated from template by package builder

* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- rebuild with perl 5.26

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- regenerated from template by package builder

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- regenerated from template by package builder

* Sun Oct 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- regenerated from template by package builder

* Sun Sep 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.25-alt2
- rebuild to get rid of unmets

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- regenerated from template by package builder

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1.1
- rebuild with perl 5.22

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.22-alt2
- rebuild to get rid of unmets

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Sat Feb 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

