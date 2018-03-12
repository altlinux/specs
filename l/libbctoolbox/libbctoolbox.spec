Name: libbctoolbox
Version: 0.6.0
Release: alt2
Summary: Utilities library used by Belledonne Communications softwares

Group: System/Libraries

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPL
Url: http://www.belle-sip.org
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Mar 02 2017
# optimized out: bcunit gnu-config libstdc++-devel perl pkg-config python-base
BuildRequires: bcunit-devel gcc-c++ libmbedtls-devel

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
* Mon Mar 12 2018 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt2
- Rebuild with mbedtls 2.7.0

* Sat Jul 22 2017 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Mar 02 2017 Alexei Takaseev <taf@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus
