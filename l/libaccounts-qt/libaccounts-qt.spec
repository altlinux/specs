# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libaccounts-qt
Version:	0.31
Release:	alt2_5
Summary:	Accounts framework
Group:		System/Libraries
License:	LGPLv2
URL:		http://gitorious.org/accounts-sso/accounts-qt
Source0:	accounts-qt-%{version}.tar.gz
# Fix compilation error in 64 bit arches
Patch0:		accounts-qt-0.28-fix-64bit-compilation.patch
# extracted from http://repo.meego.com/MeeGo/builds/trunk/daily/core/repos/source/libaccounts-qt-0.31-1.5.src.rpm
BuildRequires:	qt4-devel libaccounts-glib-devel
BuildRequires:	doxygen graphviz
Source44: import.info

%description
Framework to provide accounts.

%package devel
Summary:	Development files for accounts-qt
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	libqt4-devel

%description devel
Headers, development libraries and documentation for accounts-qt.

%prep
%setup -q -n accounts-qt-%{version}
%patch0 -p1

sed -i 's\{INSTALL_PREFIX}/lib\{INSTALL_PREFIX}/%{_lib}\g' common-installs-config.pri
sed -i 's\{INSTALL_PREFIX}/lib\{INSTALL_PREFIX}/%{_lib}\g' Accounts/Accounts.pro
sed -i 's\usr/lib\usr/%{_lib}\g' Accounts/accounts.prf
sed -i 's\usr/lib\usr/%{_lib}\g' Accounts/accounts-qt.pc
sed -i 's\{prefix}/lib\{prefix}/%{_lib}\g' Accounts/accounts-qt.pc

%build
export PATH=%{_qt4_bindir}:$PATH
qmake-qt4 QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release accounts-qt.pro

make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

rm -f %{buildroot}/%{_datadir}/doc/accounts-qt/html/installdox

#remove tests for now
rm -rf %{buildroot}%{_datadir}/%{name}-tests
rm -f %{buildroot}%{_bindir}/accountstest

mv %{buildroot}%{_docdir}/accounts-qt %{buildroot}%{_docdir}/libaccounts-qt

%files
%doc COPYING
%{_libdir}/lib*.so.*
%{_bindir}/account-tool

%files devel
%{_libdir}/lib*.so
%{_includedir}/accounts-qt/
%{_libdir}/pkgconfig/accounts-qt.pc
%{_datadir}/qt4/mkspecs/*
%{_docdir}/libaccounts-qt

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_5
- update to new release by fcimport

* Mon Dec 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_4
- fixed build after mass spec cleanup

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_4
- initial import by fcimport

