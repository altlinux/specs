Name: megafuse
Version: 1.0.0
Release: alt3.1

# commit 50bc488cb54826b452b54a960efc25181519b3ba

Summary: Megasimplesync console client for mega.co.nz

License: LGPL
Group: Office
Url: https://github.com/matteoserva/MegaFuse

Source: %name-%version.tar
#Source1: %name
Source2: %name.service
Source3: %name.conf

Packager: Danil Mikhailov <danil@altlinux.org>

# Automatically added by buildreq on Tue Aug 11 2015
# optimized out: libdb4-devel libstdc++-devel pkg-config python3-base
BuildRequires: gcc-c++ libcryptopp-devel libcurl-devel libdb4.7_cxx-devel libfreeimage-devel libfuse-devel libreadline-devel

#cppcheck doxygen  glibc-devel libcares-devel libcrypto7 libcryptopp-devel libcurl-devel libdb4-devel libfreeimage-devel libfuse-devel libreadline-devel libsqlite3-devel libssl-devel zlib-devel

%description
Megafuse client for mega.nz

%prep
%setup

%build
%make_build

%install

rm -rf %buildroot%_includedir/
#rm -rf %buildroot/%_libdir/pkgconfig/
#rm -f %buildroot/%_libdir/libmega.so

mkdir -p %buildroot%_initdir/ %buildroot/lib/systemd/system/ %buildroot/etc/ %buildroot%_bindir/
cp MegaFuse %buildroot%_bindir/%name 
ln -s %name %buildroot%_bindir/MegaFuse

cp %SOURCE2 %buildroot/lib/systemd/system/
cp %SOURCE3 %buildroot/etc/

%check

%pre
%files
%_bindir/%name
%_bindir/MegaFuse

/lib/systemd/system/%name.service
#Change rule because service start from user and he hasnt permission
%attr(644,root,root) /etc/%name.conf
%_bindir/%name


%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3.1
- NMU: autorebuild with libcryptopp-5.6.5

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt3
- Fixed build with new toolchain

* Wed Aug 12 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt2
- added MegaFuse link

* Tue Aug 11 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
