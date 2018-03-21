%define sover 0
%define liblastfm liblastfm
%define liblastfm_fingerprint liblastfm-fingerprint
%define liblastfm_common liblastfm-common
%define liblastfm_devel liblastfm%{sover}-devel
Name: liblastfm%sover
Version: 0.3.3
Release: alt4.1

Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services
License: GPLv3
Url: https://github.com/lastfm/liblastfm

Requires: %name-common = %version-%release

Source: %name-%version.tar
Patch2: liblastfm-0.3.3-alt-fix-configure.patch

# Automatically added by buildreq on Tue Sep 08 2009 (-bi)
BuildRequires: gcc-c++ libfftw3-devel libqt4-devel libsamplerate-devel ruby ruby-stdlibs libcurl-devel

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n %liblastfm_common
Group: System/Configuration/Other
Summary: Common package for %name
%description -n %liblastfm_common
Common package for %name

%package -n %liblastfm
Group: System/Libraries
Summary: Library to help you integrate Last.fm services
Requires: %liblastfm_common = %version-%release
%description -n %liblastfm
Common package for %name

%package -n %liblastfm_fingerprint
Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services
Requires: %liblastfm_common = %version-%release
%description -n %liblastfm_fingerprint
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n %liblastfm_devel
Group: Development/C++
Summary: %name development files
Requires: %liblastfm_common = %version-%release
Conflicts: liblastfm-devel
%description -n %liblastfm_devel
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


%files -n %liblastfm_common

%files -n %liblastfm
%_libdir/liblastfm.so.%sover
%_libdir/liblastfm.so.%sover.*

%files -n %liblastfm_fingerprint
%_libdir/liblastfm_fingerprint.so.%sover
%_libdir/liblastfm_fingerprint.so.%sover.*

%files -n %liblastfm_devel
%doc README*
%_libdir/*.so
%_includedir/*

%changelog
* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt4.1
- NMU: added URL

* Mon Jan 28 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt4
- rebuilt witn new rpm

* Tue Jan 22 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt3
- rename to liblastfm0

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
