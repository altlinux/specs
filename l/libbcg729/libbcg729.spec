Summary: Opensource implementation of the ITU G729 Annex A/B speech codec
Name: libbcg729
Version: 1.1.1
Release: alt1
License: GPLv3
Group: Communications
Url: http://www.belledonne-communications.com
# https://github.com/BelledonneCommunications/bcg729
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: cmake

%description
The library written in C 99 is fully portable and can be executed on many
platforms including both ARM and x86 processors. libbcg729 supports concurrent
channels encoding/decoding for multi call application such as conferencing.
This project was initially developed as part of Mediastreamer2,
the Linphone's media processing engine. This is why it also contains the
glue to be integrated in Linphone/Mediastreamer2.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the header files and libraries for
building programs which use %name.

%prep
%setup
%patch0 -p1


%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH=ON -DENABLE_TESTS=YES -DENABLE_STATIC=NO
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS.md CHANGELOG.md README.md
%_libdir/%name.*

%files devel
%_includedir/bcg729
%_pkgconfigdir/%name.pc
%_datadir/Bcg729

%changelog
* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.0.4 -> 1.1.1

* Tue Mar 19 2019 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- updated to 1.0.4
- switch to cmake
- rewritten specfile

* Fri Aug 14 2015 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt2
- incrementing Release for Sisyphus. Must be +1 then p(7/6/5) 

* Mon Feb 16 2015 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 12 2014 Margaux Clerc <margaux.clerc@belledonne-communications.com> 
- Creation of rpm for linphone
