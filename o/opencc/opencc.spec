Name:       opencc
Version:    1.1.6
Release:    alt1
Summary:    Libraries for Simplified-Traditional Chinese Conversion

License:    Apache-2.0
Group:      System/Libraries
URL:        http://code.google.com/p/opencc/
Source0:    %{name}-%{version}.tar
# VCS:      https://github.com/BYVoid/OpenCC.git

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
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
BuildArch: noarch

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

%build
%cmake -GNinja -DBUILD_DOCUMENTATION=ON
# Build in four threads to prevent race condition
%define __nprocs 4
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

%find_lang %name

%check
# the target does nothing...
%cmake_build --target test

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
* Fri Dec 09 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Sun Dec 04 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version.

* Sun Jun 05 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- New version.

* Sat Sep 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version.

* Sun Apr 25 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.2-alt1.1
- NMU: spec: adapt to new cmake macros.

* Thu Mar 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt2
- Use rpm-build-ninja for build.
- Really use four threads to build by ninja-build.

* Sat May 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.
- Use ninja-build for build.

* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.
- Fix License tag according to SPDX.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Tue Apr 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.qa3
- Build in one thread to prevent race condition.

* Mon Nov 19 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.5-alt1.qa2
- spec: moved %%find_lang to %%install section.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.qa1
- NMU: applied repocop patch

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Tue Feb 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- New version

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

