Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-POE-Component-SSLify
Version:        1.012
Release:        alt1_17
Summary:        Makes using SSL in the world of POE easy!
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/POE-Component-SSLify
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SSLify-%{version}.tar.gz
# Do not use SSLv3 in tests. It's not supported by Net-SSLeay-1.68 with
# OpenSSL-1.0.2a, bug #1222521, CPAN RT#104493
Patch0:         POE-Component-SSLify-1.012-Use-default-SSL-version-in-tests.patch
# Work around a SIGPIPE bug in TLSv1.3 server, bug #1622999, CPAN RT#126976
Patch1:         POE-Component-SSLify-1.012-Disable-sessions-tickets-with-OpenSSL-1.1.1.patch
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(Net/SSLeay.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(POE.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Symbol.pm)
BuildRequires:  perl(Task/Weaken.pm)
# Tests:
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(POE/Component/Client/TCP.pm)
BuildRequires:  perl(POE/Component/Server/TCP.pm)
BuildRequires:  perl(POE/Filter/Stream.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Test/FailWarnings.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests:
# CPAN::Meta not usefull
BuildRequires:  perl(IO/Prompt/Tiny.pm)
# Disable using of Test::Apocalypse, because it cannot be built with Perl 5.22
# due to failing perl-Test-Vars
%if ! 0%(perl -e 'print $] >= 5.022')
BuildRequires:  perl(Test/Apocalypse.pm)
%endif
Requires:       perl(POE.pm) >= 1.267
Requires:       perl(warnings.pm)


# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl(POE.pm)/d

%description
This component represents the standard way to do SSL in POE.

%prep
%setup -q -n POE-Component-SSLify-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
# Clean debuginfo generator pollution breaking MANIFEST test
rm -f *.list
# AUTOMATED_TESTING triggers author tests (t/simple_parallel_superbig.t) which
# fails. Upstream says: "thus is marked as TODO." CPAN RT#100549.
AUTOMATED_TESTING=0 ./Build test

%files
%doc --no-dereference LICENSE
%doc README Changes
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_17
- update to new release by fcimport

* Wed Apr 03 2019 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_15
- fixed build (closes: #36474)

* Thu Dec 27 2018 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_14
- fixed build - use fedora patches

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.008-alt1
- 0.20 -> 1.008

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- 0.20
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- initial build for ALT Linux Sisyphus
