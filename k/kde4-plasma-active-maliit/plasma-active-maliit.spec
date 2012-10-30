%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname plasma-active-maliit
Name: kde4-plasma-active-maliit
Version: 0.1
Release: alt1

Group: Graphical desktop/KDE
Summary: Virtual Keyboard for plasma-active
License: Nokia
Url: http://kde.org/

Requires: maliit-inputcontext-qt4
#Requires: maliit-plugins

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Oct 18 2012 (-bi)
# optimized out: libmaliit1.0-0 libqt4-core libqt4-devel libqt4-gui libstdc++-devel python-base
#BuildRequires: gcc-c++ glibc-devel-static maliit-framework-devel phonon-devel rpm-build-gir
BuildRequires: cmake gcc-c++ libqt4-devel libmaliit-devel

%description
Virtual Keyboard for plasma-active.

%prep
%setup -qn %rname-%version

%build
qmake-qt4 PREFIX=%prefix BINDIR=%_bindir LIBDIR=%_libdir INCLUDEDIR=%_includedir
%make_build

%install
%make install INSTALL_ROOT=%buildroot

%files
#%_sysconfdir/profile.d/maliitactiveinputmethod.sh
%_libdir/maliit
%_datadir/maliit

%changelog
* Thu Oct 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
