%define sover 1
%define liblastfm liblastfm%sover
%define liblastfm_fingerprint liblastfm_fingerprint%sover
%define liblastfm_common liblastfm-common%sover
Name: liblastfm
Version: 1.0.3
Release: alt2

Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services
License: GPLv3

Requires: %name-common = %version-%release

Source: %name-%version.tar

# Automatically added by buildreq on Tue Jan 22 2013 (-bi)
# optimized out: cmake-modules elfutils libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ libfftw3-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libsamplerate-devel phonon-devel rpm-build-ruby
BuildRequires: cmake gcc-c++ libfftw3-devel libqt4-devel libsamplerate-devel phonon-devel
BuildRequires: kde-common-devel

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

%package devel
Group: Development/C++
Summary: %name development files
Requires: %liblastfm_common = %version-%release
%description devel
Install this package if you want do compile applications using the %name library.


%prep
%setup -q

%build
%Kbuild

%install
%Kinstall


%files -n %liblastfm_common

%files -n %liblastfm
%_libdir/liblastfm.so.%sover
%_libdir/liblastfm.so.%sover.*

%files -n %liblastfm_fingerprint
%_libdir/liblastfm_fingerprint.so.%sover
%_libdir/liblastfm_fingerprint.so.%sover.*

%files devel
%doc README*
%_libdir/*.so
%_includedir/*

%changelog
* Mon Jan 28 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt2
- rebuilt with new rpm (ALT#28443)

* Tue Jan 22 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

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
