%define rname kapidox

Name: kf5-%rname
Version: 5.19.0
Release: alt1
%K5init altplace
%setup_python_module %rname

Group: System/Libraries
Summary: KDE Frameworks 5 doxygen tools
Url: http://www.kde.org
License: BSD

Requires: kf5-filesystem

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Feb 18 2015 (-bi)
# optimized out: cmake-modules python-base python-modules python-modules-compiler python-modules-email
#BuildRequires: cmake graphviz python-devel python-module-google rpm-build-gir ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake graphviz python-devel

%description
This framework contains scripts and data for building API documentation (dox) in
a standard format and style.

%package -n python-module-%rname
Group: System/Libraries
Summary: KF5 doxygen tools bindings
#Requires: %name-common = %version-%release
%description -n python-module-%rname
KF5 doxygen tools bindings

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move bin all
%if "%_lib" == "lib64"
mkdir -p %buildroot/%_libdir
mv %buildroot/usr/lib/python* %buildroot/%_libdir/
%endif

%files
%doc LICENSE README.md
%_K5bin/depdiagram-*
%_K5bin/kgen*

%files -n python-module-%rname
%python_sitelibdir/kapidox/
%python_sitelibdir/kapidox-*

#%files devel
#%_K5inc/kapidox_version.h
#%_K5inc/kapidox/
#%_K5link/lib*.so
#%_K5lib/cmake/kapidox
#%_K5archdata/mkspecs/modules/qt_kapidox.pri

%changelog
* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- initial build
