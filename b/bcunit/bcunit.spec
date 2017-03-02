Name: bcunit
Version: 3.0
Release: alt1
Summary: Utilities library used by Belledonne Communications softwares

Group: System/Libraries

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPL
Url: http://www.belle-sip.org
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

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
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*

%files devel
%_includedir/BCUnit
%_libdir/libbcunit.so
%_libdir/pkgconfig/bcunit.pc
%_mandir/man3/*
%_datadir/BCUnit

%changelog
* Thu Mar 02 2017 Alexei Takaseev <taf@altlinux.org> 3.0-alt1
- Initial build for ALT Sisyphus
