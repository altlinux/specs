%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-Valgrind
Summary:	Generate suppressions, analyze and test any command with valgrind
Version:	1.19
Release:	alt2
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-Valgrind/
Source:	http://www.cpan.org/authors/id/V/VP/VPIT/Test-Valgrind-%{version}.tar.gz

BuildRequires(pre): rpm-macros-valgrind

BuildRequires:	perl(base.pm)
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Digest/MD5.pm)
BuildRequires:	perl(Env/Sanctify.pm)
BuildRequires:	perl(ExtUtils/Install.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(Fcntl.pm)
BuildRequires:	perl(File/HomeDir.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Filter/Util/Call.pm)
BuildRequires:	perl(lib.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(POSIX.pm)
BuildRequires:	perl(Perl/Destruct/Level.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(XML/Twig.pm)
BuildRequires:	perl(XSLoader.pm)
BuildRequires:	perl(version.pm)
Requires:	perl(Carp.pm)
Requires:	perl(Digest/MD5.pm)
Requires:	perl(File/HomeDir.pm) >= 0.86
Requires:	perl(File/Path.pm)
Requires:	perl(File/Temp.pm) >= 0.14
Requires:	perl(Filter/Util/Call.pm)
Requires:	perl(List/Util.pm)
Requires:	perl(Perl/Destruct/Level.pm)
Requires:	perl(XML/Twig.pm)

%ifarch %valgrind_arches
BuildRequires:	valgrind >= 3.1.0
Requires:	valgrind >= 3.1.0
%endif

# Don't "provide" private Perl libs

Source44: import.info

%description
The Test::Valgrind::* API lets you run Perl code through the memcheck tool of
the valgrind memory debugger, to test for memory errors and leaks. The
Test::Valgrind module itself is a front-end to this API. If they aren't
available yet, it will first generate suppressions for the current perl
interpreter and store them in the portable flavor of
~/.perl/Test-Valgrind/suppressions/$VERSION. The actual run will then take
place, and tests will be passed or failed according to the result of the
analysis.

The complete API is much more versatile than this. By declaring an appropriate
Test::Valgrind::Command class, you can run any executable (that is, not only
Perl scripts) under valgrind, generate the corresponding suppressions
on-the-fly and convert the analysis result to TAP output so that it can be
incorporated into your project's test suite. If you're not interested in
producing TAP, you can output the results in whatever format you like (for
example HTML pages) by defining your own Test::Valgrind::Action class.

%prep
%setup -q -n Test-Valgrind-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

# The package is noarch; the XS code included is for testing purposes and is
# not part of the module itself
if [ "%{perl_vendor_archlib}" != "%{perl_vendor_privlib}" ]; then
	mkdir -p %{buildroot}%{perl_vendor_privlib}
	mv %{buildroot}%{perl_vendor_archlib}/* %{buildroot}%{perl_vendor_privlib}/
fi

# If we have ExtUtils::Install < 1.3702, INSTALL.SKIP will be ignored
# and valgrind.so will have been installed, so remove it
if perl -MExtUtils::Install -e 'exit (($ExtUtils::Install::VERSION < 1.3702) ? 0 : 1);'; then
	rm %{buildroot}%{perl_vendor_privlib}/auto/Test/Valgrind/Valgrind.so
fi

%files
%doc Changes README samples/
%{perl_vendor_privlib}/Test/

%changelog
* Mon Oct 04 2021 Ivan A. Melnikov <iv@altlinux.org> 1.19-alt2
- don't require valgrind (and do nothing) on
  architectures that valgrind does not support

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Fri Nov 13 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2_2
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2_1
- Sisyphus build

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_6
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_3
- fc import

