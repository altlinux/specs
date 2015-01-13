
Name:       opencc
Version:    1.0.2
Release:    alt1
Summary:    Libraries for Simplified-Traditional Chinese Conversion

License:    ASL 2.0
Group:      System/Libraries
URL:        http://code.google.com/p/opencc/
Source0:    %{name}-%{version}.tar
# VCS:      https://github.com/BYVoid/OpenCC.git

Patch1:     opencc-fixes-cmake.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: ctest
BuildRequires: doxygen
BuildRequires: python-modules-encodings

%description
OpenCC is a library for converting characters and phrases between
Traditional Chinese and Simplified Chinese.

%package doc
Summary:    Documentation for OpenCC
Group:      Text tools
Requires:   %{name} = %{version}-%{release}

%description doc
Doxygen generated documentation for OpenCC.

%package tools
Summary:    Command line tools for OpenCC
Group:      Text tools
Requires:   %{name} = %{version}-%{release}

%description tools
Command line tools for OpenCC, including tools for conversion via CLI
and for building dictionaries.

%package devel
Summary:    Development files for OpenCC
Group:      Development/C
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch1 -p1

%build
%cmake -DENABLE_GETTEXT:BOOL=ON \
       -DBUILD_DOCUMENTATION:BOOL=ON
export LD_LIBRARY_PATH=%_builddir/%name-%version/BUILD/src
%cmake_build #VERBOSE=1

%install
%cmakeinstall_std
rm -f %buildroot%_libdir/*.a

%check
ctest

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS LICENSE README.md
%_libdir/lib*.so.*
%_datadir/opencc/
%exclude %_datadir/opencc/doc

%files doc
%_datadir/opencc/doc

%files tools
%_bindir/*
#%%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon Jan 12 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version
- Build from upstream Git repository https://github.com/BYVoid/OpenCC.git

* Mon May 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.3-alt2
- Move from Autoimports to Sisyphus

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1_1
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_4
- initial fc import

