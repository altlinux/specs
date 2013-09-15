# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize gobject-introspection-devel pkgconfig(check) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: liblangtag
Version: 0.5.2
Release: alt1_1
Summary: An interface library to access tags for identifying languages

Group: System/Libraries
License: (LGPLv3+ or MPLv2.0) and UCD
URL: http://tagoh.bitbucket.org/liblangtag/
Source0: https://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gtk-doc
BuildRequires: libtool
BuildRequires: libxml2-devel
Source44: import.info

%description
%{name} is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-shared --disable-introspection
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags} V=1 \
    LD_LIBRARY_PATH=`pwd`/liblangtag/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/%{name}/*.la


%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc COPYING
%{_datadir}/gtk-doc/html/%{name}


%changelog
* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_3
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_3
- initial fc import

