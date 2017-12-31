Name: CuraEngine
Epoch: 1
Version: 3.0.3
Release: alt1

Summary: Engine for processing 3D models into G-code instructions for 3D printers
License: AGPL-3.0
Group: Engineering
Url: https://github.com/Ultimaker/CuraEngine

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: CuraEngine-rpath-%version.patch
Patch1: CuraEngine-static-libstdcpp-%version.patch
Patch2: CuraEngine-system-libs-%version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake libArcus-devel protobuf-compiler pkgconfig(protobuf) libpolyclipping-devel pkgconfig(RapidJSON)

%description
CuraEngine is a powerful, fast and robust engine for processing 3D
models into 3D printing instruction for Ultimaker and other GCode
based 3D printers. It is part of the larger open source project
called "Cura".

The CuraEngine is a C++ console application for 3D printing GCode
generation. It has been made as a better and faster alternative
to the old Skeinforge engine.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

# bundled libraries
rm -rf libs/clipper
sed -i 's|#include <clipper/clipper.hpp>|#include <polyclipping/clipper.hpp>|' src/utils/*.h src/*.cpp

# The -DCURA_ENGINE_VERSION does not work, so we sed-change the default value
sed -i 's/"DEV"/"%{version}"/' src/settings/settings.h

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DCURA_ENGINE_VERSION:STRING=%version
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%doc LICENSE README.md

%changelog
* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Sat Nov 25 2017 Igor Vlasenko <viy at altlinux.ru> 15.04-alt2_5
- rebuild with libpolyclipping

* Thu Mar 16 2017 Igor Vlasenko <viy at altlinux.ru> 15.04-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy at altlinux.ru> 15.04-alt1_2
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy at altlinux.ru> 14.12.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_1
- update to new release by fcimport

* Sat Jun 07 2014 Igor Vlasenko <viy at altlinux.ru> 14.01-alt1_1
- by request of Dmitry Derjavin <dd@>
