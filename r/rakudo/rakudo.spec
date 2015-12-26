Name: rakudo
Version: 2015.12
Release: alt1
Summary: Perl 6 compiler for the MoarVM

Group: Development/Other
License: Artistic 2
URL: http://rakudo.org/

# Cloned from https://github.com/MoarVM/MoarVM
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Vladimir Lettiev <crux@altlinux.ru>

Requires: nqp

BuildRequires: libmoarvm-devel moarvm nqp perl-devel libffi-devel
# Fake deps, only headers required (libraries already linked in libmoarvm)
BuildRequires: libuv-devel libatomic_ops-devel-static libtommath-devel

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

mkdir -p %buildroot%_datadir/perl6/{vendor,site}/lib

%files
%_bindir/perl6*
%_datadir/nqp/lib/Perl6
%_datadir/perl6/lib/*
%_datadir/perl6/runtime/*
%_libdir/perl6/runtime/dynext
%dir %_datadir/perl6/vendor
%dir %_datadir/perl6/vendor/lib
%dir %_datadir/perl6/site
%dir %_datadir/perl6/site/lib
%doc LICENSE README.md CREDITS

%changelog
* Sat Dec 26 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.12-alt1
- 2015.12

* Sun Nov 29 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.11-alt1
- 2015.11

* Tue Nov 10 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt2
- fixed install of shared lib

* Tue Oct 27 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt1
- initial build

