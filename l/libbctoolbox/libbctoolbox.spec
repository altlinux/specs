Name: libbctoolbox
Version: 0.6.0
Release: alt5
Summary: Utilities library used by Belledonne Communications softwares

Group: System/Libraries

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: http://www.belle-sip.org
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Mar 02 2017
# optimized out: bcunit gnu-config libstdc++-devel perl pkg-config python-base
BuildRequires: bcunit-devel gcc8-c++ libmbedtls13-devel

%description
Utilities library used by Belledonne Communications
softwares like belle-sip, mediastreamer2 and linphone.

%package devel
Summary: Development libraries for bctoolbox
Group: Development/Other
Requires: %name = %version-%release

%description devel
Libraries and headers required to develop software with belle-sip, mediastreamer2 and linphone.

%prep
%setup
%patch0 -p1

%build
# Glibc 2.33 deprecated mallinfo() in favor of mallinfo2() 
sed -e 's,mallinfo,mallinfo2,g' -i src/tester.c

%ifnarch %e2k
%set_gcc_version 8
export CC="gcc-%{_gcc_version}"
export CXX="g++-%{_gcc_version}"
%endif
./autogen.sh
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%_libdir/*.so.*

%files devel
%_includedir/bctoolbox
%_libdir/libbctoolbox-tester.so
%_libdir/libbctoolbox.so
%_libdir/pkgconfig/bctoolbox-tester.pc
%_libdir/pkgconfig/bctoolbox.pc

%changelog
* Wed Jan 19 2022 Alexander Danilov <admsasha@altlinux.org> 0.6.0-alt5
- fixed FTBFS

* Sun Jul 11 2021 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt4
- Build with mbedtls 2.27.0
- Fix License

* Thu Oct 24 2019 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt3
- Build with gcc8

* Mon Mar 12 2018 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt2
- Rebuild with mbedtls 2.7.0

* Sat Jul 22 2017 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Mar 02 2017 Alexei Takaseev <taf@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus
