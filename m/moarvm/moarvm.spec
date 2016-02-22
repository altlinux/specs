Name: moarvm
Version: 2016.02
Release: alt1
Summary: 6model-based VM for NQP and Rakudo Perl 6

Group: Development/Other
License: Artistic 2
URL: http://moarvm.org

# Cloned from https://github.com/MoarVM/MoarVM
Source: %name-%version.tar
# Cloned from  https://github.com/libuv/libuv
Source1: libuv.tar
# Cloned from https://github.com/MoarVM/dynasm
Source2: dynasm.tar
# Cloned from https://github.com/MoarVM/dyncall
Source3: dyncall.tar

Patch: %name-%version-%release.patch

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libtommath-devel libffi-devel perl-Pod-Usage perl-devel perl-podlators
# TODO:
# libuv-devel - sisyphus version is too old
# libatomic_ops-devel - sisyphus version is old and static only
# sha-devel - not exists in sisyphus

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
%setup -a1 -a2 -a3
%patch -p1

rm -r 3rdparty/{libuv,dynasm,dyncall}
mv libuv dynasm dyncall 3rdparty

%build
perl Configure.pl --prefix=%_prefix --libdir=%_libdir \
    --has-libtommath  --has-libffi
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
%exclude %_includedir/libtommath
%exclude %_includedir/libatomic_ops
%exclude %_includedir/libuv
%_datadir/pkgconfig/moar.pc

%changelog
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

