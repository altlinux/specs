# BEGIN SourceDeps(oneline):
BuildRequires: libdb4-devel
# END SourceDeps(oneline)
Group: Other
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global snapshot 0

Name:           libpinyin
Version:        2.8.1
Release:        alt1_5
Summary:        Library to deal with pinyin

License:        GPL-3.0-or-later
URL:            https://github.com/libpinyin/libpinyin
Source0:        http://downloads.sourceforge.net/libpinyin/libpinyin/%{name}-%{version}.tar.gz
%if %snapshot
Patch0:         libpinyin-2.8.x-head.patch
%endif

BuildRequires:  gcc-c++
BuildRequires:  libkyotocabinet-devel glib2-devel libgio libgio-devel
Requires:       %{name}-data = %{version}-%{release}
Source44: import.info

%description
The libpinyin project aims to provide the algorithms core
for intelligent sentence-based Chinese pinyin input methods.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libzhuyin = %{version}-%{release}
Provides:       libzhuyin-devel = %{version}-%{release}
Obsoletes:      libzhuyin-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        data
Group: Other
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}

%description data
The %{name}-data package contains data files.

%package        tools
Group: Other
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools.

%package -n     libzhuyin
Group: Other
Summary:        Library to deal with zhuyin
Requires:       %{name} = %{version}-%{release}

%description -n libzhuyin
The libzhuyin package contains libzhuyin compatibility library.


%prep
%setup -q

%if %snapshot
%patch0 -p1 -b .head
%endif

%build
%configure --disable-static \
           --with-dbm=KyotoCabinet \
           --enable-libzhuyin
%make_build

%check
make check

%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'





%files
%doc AUTHORS COPYING README
%{_libdir}/libpinyin*.so.*
%dir %{_libdir}/libpinyin

%files devel
#doc %_docdir/%name
%dir %{_includedir}/libpinyin-%{version}
%{_includedir}/libpinyin-%{version}/*
%{_libdir}/libpinyin.so
%{_libdir}/pkgconfig/libpinyin.pc
%{_libdir}/libzhuyin.so
%{_libdir}/pkgconfig/libzhuyin.pc

%files data
#doc %_docdir/%name
%{_libdir}/libpinyin/data

%files tools
%{_bindir}/gen_binary_files
%{_bindir}/import_interpolation
%{_bindir}/gen_unigram
%{_mandir}/man1/*.1*

%files -n libzhuyin
%{_libdir}/libzhuyin*.so.*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 2.8.1-alt1_5
- update to new release by fcimport

* Sat Nov 13 2021 Igor Vlasenko <viy@altlinux.org> 2.6.1-alt1_2
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 2.6.1-alt1_1
- update to new release by fcimport

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_1
- update to new release by fcimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1
- update to new release by fcimport

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1
- update to new version by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.94-alt1_1
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.93-alt1_2
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.93-alt1_1
- update to new release by fcimport

* Mon Jun 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.92-alt1_1
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.91-alt1_1
- update to new release by fcimport

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.93-alt1_2
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.93-alt1_1
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.92-alt1_1
- update to new release by fcimport

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.91-alt1_1
- fc update

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_3
- update to new release by fcimport

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_2
- initial fc import

