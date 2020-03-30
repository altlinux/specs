# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libesedb
Version:        20181229
Release:        alt1_2
Summary:        Library to access the Extensible Storage Engine (ESE) Database File (EDB) format

%global         common_description \
Library and tools to access the Extensible Storage Engine (ESE) Database File \
(EDB) format. ESEDB is used in may different applications like Windows Search, \
Windows Mail, Exchange, Active Directory, etc.


%global         gituser         libyal
%global         gitname         libesedb
%global         commit          6b02d5d3d1ed9f3e9853aad0c33d64da2315b863
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

# Build with python3 package by default
%bcond_without  python3


License:        LGPLv3+
URL:            https://github.com/libyal/libesedb
#               https://github.com/libyal/libesedb/releases
# Source0:      https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/releases/download/%{version}/%{gitname}-experimental-%{version}.tar.gz

# Patch build to use the shared system libraries rather than using embedded ones
# Patch0:         %{name}-libs.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# autoreconf here needs autopoint from gettext-devel
BuildRequires:  gettext-tools libasprintf-devel


%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-module-distribute
%endif # if with_python3

Provides: bundled(libbfio)      = 20180910
Provides: bundled(libcdata)     = 20181228
Provides: bundled(libcerror)    = 20181117
Provides: bundled(libcfile)     = 20180102
Provides: bundled(libclocale)   = 20180721
Provides: bundled(libcnotify)   = 20180102
Provides: bundled(libcpath)     = 20181228
Provides: bundled(libcsplit)    = 20180103
Provides: bundled(libcthreads)  = 20180724
Provides: bundled(libfcache)    = 20181011
Provides: bundled(libfdata)     = 20181216
Provides: bundled(libfdatetime) = 20180910
Provides: bundled(libfguid)     = 20180724
Provides: bundled(libfmapi)     = 20180714
Provides: bundled(libfvalue)    = 20180817
Provides: bundled(libfwnt)      = 20181227
Provides: bundled(libmapidb)    = 20170304
Provides: bundled(libuna)       = 20181006
Source44: import.info

%description
%{common_description}


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%{common_description}


%if 0%{?with_python3}
%package -n python3-module-pyesedb
Group: Other
Summary:        Python3 binding for the library reading of esedb format
%{?python_provide:%python_provide python%{python3_pkgversion}-pyesedb}

%description -n python3-module-pyesedb
Python3 binding for the library reading of esedb format
%{common_description}
%endif


%prep
%setup -q -n %{gitname}-%{version}

#./autogen.sh
autoreconf --force --install
aclocal


%build
%configure --disable-static \
%if 0%{?with_python3}
           --enable-python3 \
%endif
           --enable-wide-character-type \
           --enable-multi-threading-support

%make_build


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{_bindir}/esedbexport
%{_bindir}/esedbinfo
%{_mandir}/man1/esedbinfo.1*
%{_mandir}/man3/libesedb.3*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libesedb.pc

%if 0%{?with_python3}
%files -n python3-module-pyesedb
%{python3_sitelibdir}/pyesedb*
%endif


%changelog
* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 20181229-alt1_2
- update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 20120102-alt2_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 20120102-alt2_11
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 20120102-alt2_10
- update to new release by fcimport

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 20120102-alt2_7
- fixed build

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_5
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_4
- initial fc import

