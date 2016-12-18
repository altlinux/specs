# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
Name:           libUnihan
%global         libUnihan_ver_major 0
%global         libUnihan_ver_minor 5
Version:        %{libUnihan_ver_major}.%{libUnihan_ver_minor}.3
Release:        alt4_16
License:        LGPLv2+
Summary:        C library for Unihan character database in fifth normal form 
Summary(zh_CN): 用于符合第五正规化之统汉字(Unihan)数据库的 C 库文件
Summary(zh_TW): 用於符合第五正規化之統漢字(Unihan)資料庫的 C 函式庫

BuildRequires: glib2-devel libgio libgio-devel  libsqlite3-devel ctest cmake

URL:            http://sourceforge.net/projects/libunihan
Source0:        http://downloads.sourceforge.net/libunihan/%{name}-%{version}-Source.tar.gz

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Source44: import.info

%description
libUnihan provides a C library for Unihan character database in fifth
normal form (5NF).

%package devel
Group: Development/C
Summary:    Development files of libUnihan
License:        LGPLv2+
Requires:       %{name} = %{version}
Requires: libgio

%description devel
Development files of libUnihan such as header files.

%package doc
Group: Documentation
Summary:    The libUnihan C API documents in Doxygen style
License:        LGPLv2+
BuildRequires:  doxygen
Requires:       %{name} = %{version}

%description doc
The libUnihan C API documents in Doxygen style.

%prep
%setup -q -n %{name}-%{version}-Source

# HACK: Replace hard-coded docdir in CMakeList.txt
sed -i \
  -e "s|\${docdir}/\${DB_PRJ_NAME}|%{_docdir}/%{name}|" \
  -e "s|\${docdir}/\${PROJECT_NAME}-\${PRJ_VER}|%{_docdir}/%{name}|" \
  CMakeLists.txt

%build
%{fedora_cmake} .
cmake .
make VERBOSE=1 C_DEFINES="$RPM_OPT_FLAGS" %{?_smp_mflags}
make doxygen


%install
%makeinstall_std

#%check
#make test

%files
%doc AUTHORS NEWS README
%doc COPYING COPYING.LESSER
%{_bindir}/unihan_query
%{_libdir}/%{name}.so.%{libUnihan_ver_major}
%{_libdir}/%{name}.so.%{libUnihan_ver_major}.%{libUnihan_ver_minor}

%files devel
%doc COPYING COPYING.LESSER
%doc ChangeLog
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_bindir}/unihan_converter

%files doc
%doc %{_docdir}/%{name}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_12
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_11
- update to new release by fcimport

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.3-alt4_9.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libUnihan-doc

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_9
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt4_8
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt3_8
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt3_7
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_6
- initial import by fcimport

