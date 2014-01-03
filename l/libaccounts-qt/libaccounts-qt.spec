# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ libqt4-devel pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libaccounts-qt
Version:	1.6
Release:	alt1_4
Summary:	Accounts framework Qt bindings
Group:		System/Libraries
License:	LGPLv2
URL:		http://code.google.com/p/accounts-sso/
Source0:	http://accounts-sso.googlecode.com/files/accounts-qt-%{version}.tar.bz2
Patch0:		accounts-qt-1.6-do-not-initialize-qstring-to-null.patch
Patch1:		libaccounts-qt-64bitarchs.patch
BuildRequires:	qt4-devel libaccounts-glib-devel
BuildRequires:	doxygen graphviz
Source44: import.info

%description
Framework to provide accounts for Qt.

%package devel
Summary:	Development files for accounts-qt
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	qt4-devel%{?_isa}

%description devel
Headers, development libraries and documentation for accounts-qt.

%prep
%setup -q -n accounts-qt-%{version}
%patch0 -p1 -b .do-not-initialize-qstring-to-null
%patch1 -p1 -b .64bitarchs

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

# move installed docs to include them in subpackage via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/accounts-qt __tmp_doc

%files
%doc COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/accounts-qt/
%{_libdir}/pkgconfig/accounts-qt.pc
%doc __tmp_doc/accounts-qt/*

%changelog
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

