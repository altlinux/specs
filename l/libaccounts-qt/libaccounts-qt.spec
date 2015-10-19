# BEGIN SourceDeps(oneline):
BuildRequires: accounts-qt5-devel gcc-c++ pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared

%global commit0 2a9cc22ff7b0b62b60541423763cb3dd992c0f40

Name:           libaccounts-qt
Summary:        Accounts framework Qt bindings
Version:        1.13
Release:        alt1_1

License:        LGPLv2
URL:            https://gitlab.com/accounts-sso/libaccounts-qt

Source0:        https://gitlab.com/accounts-sso/libaccounts-qt/repository/archive.tar.gz?ref=%{version}#/libaccounts-qt-%{version}-%{commit0}.tar.gz

Patch1:         libaccounts-qt-64bitarchs.patch

## upstream patches
Patch102: 0002-Fix-memory-leaks-found-by-valgrind.patch
patch105: 0005-Use-gboolean-instead-of-bool.patch

BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  doxygen
BuildRequires:  graphviz
Source44: import.info

%description
%{summary}.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


%prep
%setup -q -n libaccounts-qt-%{version}-%{commit0}

%patch1 -p1 -b .64bitarchs
%patch102 -p1 -b .0002
%patch105 -p1 -b .0005


%build
%{qmake_qt4} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    accounts-qt.pro

make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

rm -fv %{buildroot}%{_datadir}/doc/accounts-qt/html/installdox

#remove tests for now
rm -rfv %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -fv %{buildroot}%{_bindir}/accountstest

# move installed docs to include them in subpackage via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/accounts-qt __tmp_doc


%files
%doc COPYING
%{_libdir}/libaccounts-qt.so.*

%files devel
%{_libdir}/libaccounts-qt.so
%{_includedir}/accounts-qt/
%{_libdir}/pkgconfig/accounts-qt.pc
%{_libdir}/cmake/AccountsQt/
%doc __tmp_doc/accounts-qt/*


%changelog
* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_5
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_3
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_1
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3
- update to new release by fcimport

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_6
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_5
- update to new release by fcimport

* Mon Dec 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_4
- fixed build after mass spec cleanup

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_4
- initial import by fcimport

