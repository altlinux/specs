Name: rakudo
Version: 2017.09
Release: alt1
Summary: Perl 6 compiler for the MoarVM

Group: Development/Other
License: Artistic 2
URL: http://rakudo.org/

# Cloned from https://github.com/MoarVM/MoarVM
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Vladimir Lettiev <crux@altlinux.org>

Requires: nqp

BuildRequires: libmoarvm-devel moarvm nqp perl-devel libffi-devel libatomic_ops-devel-static
# Fake deps, only headers required (libraries already linked in libmoarvm)
BuildRequires: libuv-devel libtommath-devel

AutoReq: noperl
AutoProv: noperl

%description
%summary

%prep
%setup
%patch -p1

%build
perl Configure.pl --prefix=%_prefix --backends=moar
%make_build LIBDIR=%_libdir

%install
%makeinstall_std LIBDIR=%_libdir
mkdir -p %buildroot%_datadir/%name
cp tools/install-dist.pl %buildroot%_datadir/%name

%files
%_bindir/perl6*
%exclude %_bindir/perl6-lldb*
%_libdir/nqp/lib/Perl6
%dir %_libdir/perl6
%dir %_libdir/perl6/runtime
%dir %_libdir/perl6/bin
%dir %_libdir/perl6/dist
%dir %_libdir/perl6/precomp
%dir %_libdir/perl6/short
%dir %_libdir/perl6/site
%dir %_libdir/perl6/sources
%dir %_libdir/perl6/resources
%dir %_libdir/perl6/runtime
%dir %_libdir/perl6/vendor
%_libdir/perl6/dist/*
%_libdir/perl6/runtime/*
%_libdir/perl6/precomp/*
%_libdir/perl6/short/*
%_libdir/perl6/site/*
%_libdir/perl6/sources/*
%_libdir/perl6/vendor/*
%_libdir/perl6/version
%_datadir/%name
%doc LICENSE README.md CREDITS
%exclude %_libdir/perl6/repo.lock
%exclude %_libdir/perl6/precomp/.lock

%changelog
* Tue Sep 26 2017 Vladimir Lettiev <crux@altlinux.org> 2017.09-alt1
- 2017.09

* Mon Oct 24 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.10-alt1
- 2016.10

* Fri Oct 07 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.09-alt2
- rebuild

* Fri Oct 07 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.09-alt1
- 2016.09

* Mon Sep 12 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.08.1-alt1
- 2016.08.1

* Fri Apr 22 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.04-alt1
- 2016.04

* Mon Feb 22 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.02-alt1
- 2016.02

* Wed Feb 03 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.01.1-alt1
- 2016.01.1

* Tue Feb 02 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.01-alt1
- 2016.01

* Sat Dec 26 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.12-alt2
- fix install

* Sat Dec 26 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.12-alt1
- 2015.12

* Sun Nov 29 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.11-alt1
- 2015.11

* Tue Nov 10 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt2
- fixed install of shared lib

* Tue Oct 27 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt1
- initial build

