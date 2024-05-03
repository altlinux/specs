
%def_enable apidox

%define _libexecdir %prefix/libexec
%define sover 1
%define libname libaccounts-qt6_%sover

Name: accounts-qt6
Version: 1.17
Release: alt1

Group: System/Libraries
Summary: Accounts framework Qt6 bindings
Url: https://gitlab.com/groups/accounts-sso
License: LGPL-2.1

# https://gitlab.com/accounts-sso/libaccounts-qt
Source: %name-%version.tar

BuildRequires: graphviz doxygen qt6-base-devel
%if_enabled apidox
BuildRequires: qt6-tools
%endif
BuildRequires: libaccounts-glib-devel

%description
Framework to provide accounts for Qt6.

%package -n %libname
Group: System/Libraries
Summary: %name library
%description -n %libname
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libaccounts-glib-devel qt6-base-devel
%description devel
Headers, development libraries and documentation for %name.

%prep
%setup -n %name-%version
sed -i '/^SUBDIRS/s|tests||'  accounts-qt.pro

%build
export PATH=%_qt6_bindir:$PATH
%qmake_qt6 \
    QMAKE_STRIP=echo \
    QMF_INSTALL_ROOT=%prefix \
    CONFIG+=release \
    PREFIX=%_prefix \
    LIBDIR=%_libdir \
    LIBEXECDIR=%_libexecdir \
    accounts-qt.pro \
    #
%make_build

%install
export PATH=%_qt6_bindir:$PATH
%install_qt6_qt STRIP=echo

%if_enabled apidox
# install docs
mkdir %buildroot/%_qt6_docdir
rm -f %buildroot/%_docdir/accounts-qt/html/installdox
mv %buildroot/%_docdir/accounts-qt/html %buildroot/%_qt6_docdir/accounts
#mv %buildroot/%_docdir/accounts-qt/qch/accounts.qch %buildroot/%_qt6_docdir/
%else
rm -rf %buildroot/%_docdir/accounts-qt/
%endif

%files -n %libname
%_libdir/libaccounts-qt6.so.%sover
%_libdir/libaccounts-qt6.so.*

%files devel
%doc doc/html
%_qt6_libdir/libaccounts-qt6.so
%_qt6_libdatadir/libaccounts-qt6.so
%_includedir/accounts-qt6/
%_pkgconfigdir/accounts-qt6.pc
%_libdir/cmake/AccountsQt6/
%if_enabled apidox
%_qt6_docdir/accounts/
#%_qt6_docdir/accounts.qch
%endif

%changelog
* Fri May 03 2024 Sergey V Turchin <zerg@altlinux.org> 1.17-alt1
- initial build
