# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: Other
%add_optflags %optflags_shared
%global snapshot 1

Name:           libpinyin
Version:        0.8.0
Release:        alt1_3
Summary:        Library to deal with pinyin

License:        GPLv2+
URL:            https://github.com/libpinyin/libpinyin
Source0:        https://github.com/downloads/libpinyin/libpinyin/%{name}-%{version}.tar.gz
%if %snapshot
Patch0:         libpinyin-0.8.x-head.patch
%endif

BuildRequires:  libdb4.8-devel glib2-devel
Requires:       %{name}-data = %{version}-%{release}
Source44: import.info
Patch33: libpinyin-0.8.x-alt-linkage.patch

%description
The libpinyin project aims to provide the algorithms core
for intelligent sentence-based Chinese pinyin input methods.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %%{name}-devel package contains libraries and header files for
developing applications that use %%{name}.


%package        data
Group: Other
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}

%description data
The %%{name}-data package contains data files.


%package        tools
Group: Other
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
The %%{name}-tools package contains tools.


%prep
%setup -q

%if %snapshot
%patch0 -p1 -b .head
%endif
%patch33 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%dir %{_datadir}/libpinyin

%files devel
%doc
%dir %{_includedir}/libpinyin-%{version}
%{_includedir}/libpinyin-%{version}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpinyin.pc

%files data
%doc
%{_datadir}/libpinyin/data

%files tools
%{_bindir}/gen_binary_files
%{_bindir}/import_interpolation
%{_bindir}/gen_unigram
%{_mandir}/man1/*.1.*

%changelog
* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_3
- update to new release by fcimport

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_2
- initial fc import

