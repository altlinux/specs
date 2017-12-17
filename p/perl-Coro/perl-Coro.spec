Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-macros-fedora-compat
BuildRequires: perl(AnyEvent/AIO.pm) perl(AnyEvent/BDB.pm) perl(BDB.pm) perl(IO/AIO.pm) perl(LWP/Simple.pm) perl(Net/Config.pm) perl(Net/FTP.pm) perl(Net/HTTP.pm) perl(Net/NNTP.pm) perl(Term/ReadLine.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Coro
Version:        6.514
Release:        alt1_1.1
Summary:        The only real threads in perl
# Coro/libcoro:    GPLv2 or BSD
# Rest of package: GPL+ or Artistic
License:        (GPL+ or Artistic) and (GPLv2 or BSD)
URL:            http://search.cpan.org/dist/Coro/
Source0:        http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Coro-%{version}.tar.gz
Patch0:         %{name}-5.25-ucontext-default.patch
# Do not disable hardening
Patch1:         Coro-6.512-Disable-disabling-FORTIFY_SOURCE.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-common
BuildRequires:  libecb-devel
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Canary/Stability.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(EV.pm)
BuildRequires:  perl(EV/MakeMaker.pm)
BuildRequires:  perl(Event.pm)
BuildRequires:  perl(Event/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(AnyEvent.pm)
# AnyEvent::AIO >= 1 not used at tests
# AnyEvent::BDB >= 1 not used at tests
# AnyEvent::DNS not used at tests
BuildRequires:  perl(AnyEvent/Socket.pm)
BuildRequires:  perl(AnyEvent/Util.pm)
BuildRequires:  perl(base.pm)
# BDB not used at tests
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(common/sense.pm)
BuildRequires:  perl(Errno.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Guard.pm)
# IO::AIO >= 3.1 not used at tests
BuildRequires:  perl(IO/Socket/INET.pm)
# Net::Config not used at tests
# Net::FTP not used at tests
# Net::HTTP not used at tests
# Net::NNTP not used at tests
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XSLoader.pm)
# Export correct required versions
Requires:       perl(AnyEvent.pm) >= 7
Requires:       perl(AnyEvent/AIO.pm) >= 1
Requires:       perl(AnyEvent/BDB.pm) >= 1
Requires:       perl(EV.pm) >= 4
Requires:       perl(Event.pm) >= 1.080
Requires:       perl(Guard.pm) >= 0.500
Requires:       perl(Storable.pm) >= 2.150
Requires:       perl(warnings.pm)



# Filter underspecified dependencies









Source44: import.info
%filter_from_requires /:__requires_exclude|}^perl\\(AnyEvent.pm\\)$/d
%filter_from_requires /^perl\\(AnyEvent.pm\\) >= 4.800001$/d
%filter_from_requires /^perl\\(AnyEvent.AIO.pm\\)$/d
%filter_from_requires /^perl\\(AnyEvent.BDB.pm\\)$/d
%filter_from_requires /^perl\\(EV.pm\\)$/d
%filter_from_requires /^perl\\(Event.pm\\)$/d
%filter_from_requires /^perl\\(Guard.pm\\)$/d
%filter_from_requires /^perl\\(Storable.pm\\)$/d
%filter_from_provides /:__provides_exclude|}^perl\\(Coro.pm\\)$/d


%description
This module collection manages continuations in general, most often in the
form of cooperative threads (also called coros, or simply "coro" in the
documentation). They are similar to kernel threads but don't (in general) run
in parallel at the same time even on SMP machines. The specific flavor of
thread offered by this module also guarantees you that it will not switch
between threads unless necessary, at easily-identified points in your
program, so locking and parallel access are rarely an issue, making thread
programming much safer and easier than using other thread models.


%prep
%setup -q -n Coro-%{version}

%ifnarch %{ix86} x86_64 %{arm}
# use ucontext backend on non-x86 (setjmp didn't work on s390(x))
%patch0 -p1 -b .ucontext-default
%endif
%patch1 -p1

# Unbundle libecb
rm Coro/ecb.h
sed -i '/^Coro\/ecb\.h$/d' MANIFEST
sed -i 's/ecb\.h//' Coro/Makefile.PL

for F in Coro/jit-*.pl; do
    sed -i -e '/^#!/d' "$F"
    chmod -x "$F"
done

%fix_shbang_line eg/myhttpd


%build
# Disable FORTIFY_SOURCE on ARM as it breaks setjmp - RHBZ 750805
%ifarch %{arm}
RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -Wp,-U_FORTIFY_SOURCE -Wp,-D_FORTIFY_SOURCE=0"
%endif

# Interractive configuration. Use default values.
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=perl NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS" </dev/null
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc COPYING
%doc Changes README README.linux-glibc
%doc doc/* eg
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Coro*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.514-alt1_1.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.514-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 6.511-alt1_2
- update to new release by fcimport

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 6.511-alt1_1
- new release

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 6.511-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 6.49-alt2.1
- rebuild with new perl 5.22.0

* Sun Nov 22 2015 Vladimir Lettiev <crux@altlinux.ru> 6.49-alt2
- Fixed build for perl 5.22 (based on patch from Reini Urban)

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 6.49-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 6.43-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 6.42-alt1
- New version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 6.41-alt1.1
- rebuild with new perl 5.20.1

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 6.41-alt1
- New version

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 6.33-alt1
- New version

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 6.31-alt2
- built for perl 5.18

* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 6.31-alt1
- New version

* Fri Mar 01 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.23-alt2
- explicitly select ucontext method on arm

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 6.23-alt1
- New version

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 6.10-alt1
- New version

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 6.08-alt1
- 6.06 -> 6.08
- built for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 6.06-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Sat May 28 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.372-alt1
- New version
- Fix tests to build with current libpthread

* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 5.25-alt1
- Initial build for ALT Linux Sisyphus
