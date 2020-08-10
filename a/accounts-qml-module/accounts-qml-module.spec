%def_disable bootstrap

Name: accounts-qml-module
Version: 0.7
Release: alt2

Group: System/Libraries
Summary: QML bindings for libaccounts-qt + libsignon-qt
License: LGPL-2.1-only
Url: https://gitlab.com/accounts-sso/accounts-qml-module

Source: %name-%version.tar

BuildRequires: qt5-declarative-devel qt5-tools accounts-qt5-devel signon-devel

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%package doc
Summary: Documentation for accounts-qml-module
Group: Development/KDE and QT
BuildArch: noarch

%description doc
This package contains the developer documentation for accounts-qml-module.

%prep
%setup
%ifarch %e2k
# lcc 1.24.11: -Werror=invalid-offsetof in moc_account-service-model.cpp:29
sed -i 's,-Werror,,' common-project-config.pri
%endif

%build
mkdir build
pushd build
%qmake_qt5 \
    QMF_INSTALL_ROOT=%prefix \
    PREFIX=%prefix \
    CONFIG+=release \
%if_enabled bootstrap
    CONFIG+=no_docs \
%endif
    LIBDIR=%_libdir \
    ..
%make_build
popd

%install
pushd build
%installqt5
popd

# remove tests
rm %buildroot/%_bindir/tst_plugin

%files
%doc README.md
%dir %_qt5_qmldir/Ubuntu/
%_qt5_qmldir/Ubuntu/OnlineAccounts/

%files doc
%if_disabled bootstrap
%doc %_datadir/%name/
%endif

%changelog
* Mon Aug 10 2020 Sergey V Turchin <zerg@altlinux.org> 0.7-alt2
- fix build for e2k; thanks mike@alt

* Tue Jan 28 2020 Sergey V Turchin <zerg@altlinux.org> 0.7-alt1
- initial build
