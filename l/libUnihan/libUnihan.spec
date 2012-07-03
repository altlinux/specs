# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Summary(zh_TW): 用於符合第五正規化之統漢字(Unihan)資料庫的 C 函式庫
Summary(zh_CN): 用于符合第五正规化之统汉字(Unihan)数据库的 C 库文件
Summary(zh_TW): 用於符合第五正規化之統漢字(Unihan)資料庫的 C 函式庫
Summary(zh_CN): 用于符合第五正规化之统汉字(Unihan)数据库的 C 库文件
Summary(zh_CN): 用于符合第五正规化之统汉字(Unihan)数据库的 C 库文件
Summary(zh_TW): 用於符合第五正規化之統漢字(Unihan)資料庫的 C 函式庫
%add_optflags %optflags_shared
###
# This file is generated, please modified the .spec.in file instead!

Name:           libUnihan
%define         libUnihan_ver_major 0
%define         libUnihan_ver_minor 5
Version:        %{libUnihan_ver_major}.%{libUnihan_ver_minor}.3
Release:        alt3_7
Group:          System/Libraries
License:        LGPLv2+
Summary:        C library for Unihan character database in fifth normal form 
Summary(zh_CN): 用于符合第五正规化之统汉字(Unihan)数据库的 C 库文件
Summary(zh_TW): 用於符合第五正規化之統漢字(Unihan)資料庫的 C 函式庫

BuildRequires:  glib2-devel libsqlite3-devel ctest cmake >= 2.4

URL:            http://sourceforge.net/projects/libunihan
Source0:        http://downloads.sourceforge.net/libunihan/%{name}-%{version}-Source.tar.gz
Source44: import.info


%description
libUnihan provides a C library for Unihan character database in fifth
normal form (5NF).



%package devel
Summary:    Development files of libUnihan
Group:      Development/C
License:        LGPLv2+
Requires:       libUnihan = %{version}-%{release}

%description devel
Development files of libUnihan such as header files.

%package doc
Summary:    The libUnihan C API documents in Doxygen style
Group:      Documentation
License:        LGPLv2+
BuildRequires:  doxygen
Requires:       libUnihan = %{version}-%{release}

%description doc
The libUnihan C API documents in Doxygen style.


%prep
%setup -q -n %{name}-%{version}-Source

%build
%{fedora_cmake} .
cmake .
make VERBOSE=1 C_DEFINES="$RPM_OPT_FLAGS" %{?_smp_mflags}
make doxygen


%install
make install DESTDIR=$RPM_BUILD_ROOT

#%check
#make test

%files
%doc AUTHORS NEWS README COPYING COPYING.LESSER
%{_bindir}/unihan_query
%{_libdir}/%{name}.so.%{libUnihan_ver_major}
%{_libdir}/%{name}.so.%{libUnihan_ver_major}.%{libUnihan_ver_minor}

%files devel
%doc ChangeLog
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_bindir}/unihan_converter

%files doc
%doc doc/html

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt3_7
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_6
- initial import by fcimport

