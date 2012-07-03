Name: liblastfm
Version: 0.3.3
Release: alt2

Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services
License: GPLv3

Requires: %name-common = %version-%release

Source: http://cdn.last.fm/src/%name-%version.tar
Patch2: liblastfm-0.3.3-alt-fix-configure.patch

# Automatically added by buildreq on Tue Sep 08 2009 (-bi)
BuildRequires: gcc-c++ libfftw3-devel libqt4-devel libsamplerate-devel ruby ruby-stdlibs libcurl-devel

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package common
Group: System/Configuration/Other
Summary: Common package for %name
%description common
Common package for %name

%package fingerprint
Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services
Requires: %name-common = %version-%release
Provides: lastfm_fingerprint = %version-%release
Obsoletes: lastfm_fingerprint < %version-%release
Provides: liblastfm-_fingerprint = %version-%release
Obsoletes: liblastfm-_fingerprint < %version-%release
%description fingerprint
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package devel
Group: Development/C++
Summary: %name development files
Requires: %name-common = %version-%release
%description devel
Install this package if you want do compile applications using the %name library.


%prep
%setup -q
%patch2 -p1

find -type f -name \*.pro | \
while read f
do
    echo -e "\nQMAKE_CXXFLAGS += %optflags" >> $f
    sed -i 's|^[[:space:]]*target\.path[[:space:]]*=[[:space:]]*/lib.*|target.path = %_libdir|' $f
done

%build
ruby configure \
    --release \
    --prefix=%prefix
%make_build

%install
%make install DESTDIR=%buildroot INSTALL_ROOT=%buildroot -C src
%make install DESTDIR=%buildroot INSTALL_ROOT=%buildroot -C src/fingerprint
mkdir %buildroot/%_includedir
cp -ar _include/* %buildroot/%_includedir/


%files common

%files
%_libdir/liblastfm.so.*

%files fingerprint
%_libdir/liblastfm_fingerprint.so.*

%files devel
%doc README
%_libdir/*.so
%_includedir/*

%changelog
* Thu Oct 21 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt2
- fix liblastfm_fingerprint package name

* Tue Oct 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt1
- new version
- fix compile with new ruby

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- new version
- add versioning

* Tue Sep 08 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial specfile
