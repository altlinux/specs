# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/update-mime-database gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define shortname lcf
%define major   0
%define libname lib%{shortname}%{major}
%define devname lib%{shortname}-devel

Name:           liblcf
Version:        0.7.0
Release:        alt1_2
Summary:        Library to handle RPG Maker 2000/2003 and EasyRPG projects
Group:          System/Libraries
License:        MIT
URL:            https://easyrpg.org
Source0:        https://easyrpg.org/downloads/player/%{version}/%{name}-%{version}.tar.xz
# liblcf is not detected without this patch https://github.com/EasyRPG/Editor/issues/214
Patch0:         liblcf-0.7.0-fix-cmake-detection.patch

BuildRequires:  ccmake cmake ctest
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(expat)
Source44: import.info

%description
liblcf is a library to handle RPG Maker 2000 and 2003 game data.
It can read and write LCF and XML files. Part of C++ source files
can be regenerated from templates and CSV files using a Python script.

liblcf is part of the EasyRPG Project. More information is available
at the project website: easy-rpg.org

%files
%{_bindir}/lcf2xml
%{_bindir}/lcfstrings

#----------------------------------------------------------------------

%package -n     %{libname}
Summary:        Library to handle RPG Maker 2000/2003 and EasyRPG projects
Group:          System/Libraries
Requires:	%name = %version-%release

%description -n %{libname}
liblcf is a library to handle RPG Maker 2000 and 2003 game data.
It can read and write LCF and XML files. Part of C++ source files
can be regenerated from templates and CSV files using a Python script.

liblcf is part of the EasyRPG Project. More information is available
at the project website: easy-rpg.org

%files -n       %{libname}
%doc AUTHORS.md COPYING README.md
%{_datadir}/mime/*
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{version}

#----------------------------------------------------------------------

%package -n     %{devname}
Summary:        Development headers and library for %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains development headers and library for %{name},
a library which handles RPG Maker 2000/2003 and EasyRPG projects.

%files -n       %{devname}
%{_includedir}/lcf/
%{_libdir}/%{name}.so
%{_libdir}/cmake/liblcf/
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1


%build
%{mageia_cmake} \
  -DDISABLE_UPDATE_MIMEDB=ON
%mageia_cmake_build

%install
%mageia_cmake_install

# FIXME: CMake should do it itself
pushd %{buildroot}%{_libdir}
ln -s %{name}.so.%{major} %{name}.so.%{version}


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.7.0-alt1_2
- update by mgaimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.6.2-alt1_3
- update by mgaimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_2
- update by mgaimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- update by mgaimport

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_6
- update by mgaimport

* Thu Apr 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_5
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_4
- fixed build

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_3
- update by mgaimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_2
- update by mgaimport

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1
- update by mgaimport

* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_2
- update by mgaimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_1
- update by mgaimport

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_2
- update by mgaimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_1
- update by mgaimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_2
- update by mgaimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_1
- update by mgaimport

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_1
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3
- converted for ALT Linux by srpmconvert tools

