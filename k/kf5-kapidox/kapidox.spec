%define rname kapidox
#add_python_req_skip gv

Name: kf5-%rname
Version: 5.7.0
Release: alt0.1
%K5init altplace
# FIXME graphviz-python
%setup_python_module rname

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
Group: Graphical desktop/KDE
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
* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- initial build
