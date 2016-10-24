Name: moarvm
Version: 2016.10
Release: alt1
Summary: 6model-based VM for NQP and Rakudo Perl 6

Group: Development/Other
License: Artistic 2
URL: http://moarvm.org

# Cloned from https://github.com/MoarVM/MoarVM
Source: %name-%version.tar
# Cloned from https://github.com/MoarVM/dynasm
Source2: dynasm.tar
# Cloned from https://github.com/MoarVM/dyncall
Source3: dyncall.tar

Patch: %name-%version-%release.patch

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libuv-devel libffi-devel perl-Pod-Usage perl-devel perl-podlators
# TODO:
# libatomic_ops-devel - sisyphus version is old and static only
# sha-devel - not exists in sisyphus
# libtommath-devel - sisyphus version 0.42 is old

Requires: lib%name = %version-%release

%description
MoarVM (short for Metamodel On A Runtime Virtual Machine) is a runtime built
for the 6model object system. It is primarily aimed at running NQP and Rakudo
Perl 6, but should be able to serve as a backend for any compilers built using
the NQP compiler toolchain.

%package -n lib%name
Summary:  MoarVM shared library
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary:  Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
%summary

%prep
%setup -a2 -a3
%patch -p1

rm -r 3rdparty/{libuv,dynasm,dyncall}
mv dynasm dyncall 3rdparty

%build
perl Configure.pl --prefix=%_prefix --libdir=%_libdir \
    --has-libffi --has-libuv
%make_build

%install
%makeinstall_std

%files
%_bindir/moar

%files -n lib%name
%_datadir/nqp/lib/MAST
%_libdir/libmoar.so
%doc LICENSE CREDITS docs

%files -n lib%name-devel
%_includedir/moar
%exclude %_includedir/libatomic_ops
%exclude %_includedir/libtommath
%_datadir/pkgconfig/moar.pc

%changelog
* Mon Oct 24 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.10-alt1
- 2016.10
- build with bundled libtommath (system libtommath is too old)

* Fri Oct 07 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.09-alt1
- 2016.09

* Mon Sep 12 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.08-alt1
- 2016.08

* Fri Apr 22 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.04-alt1
- 2016.04
- switch to system libuv

* Mon Feb 22 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.02-alt1
- 2016.02

* Tue Feb 02 2016 Vladimir Lettiev <crux@altlinux.ru> 2016.01-alt1
- 2016.01

* Fri Dec 25 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.12-alt1
- 2015.12

* Sun Nov 29 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.11-alt1
- 2015.11

* Tue Oct 27 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt1
- initial build

