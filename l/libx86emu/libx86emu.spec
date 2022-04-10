# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 3
%define libname libx86emu%{major}
%define develname libx86emu-devel

Name:           libx86emu
License:        BSD
Group:          System/Libraries
Summary:        A small x86 emulation library
Version:        3.5
Release:        alt1_1
URL:		https://github.com/wfeldt/libx86emu
Source:         https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz
Source44: import.info
ExclusiveArch: %ix86 x86_64
 
%description
Small x86 emulation library with focus of easy usage and extended
execution logging functions.
 
%package -n     %{libname}
License:        BSD 3-Clause
Summary:        A small x86 emulation library
Group:          System/Libraries
 
%description -n %{libname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n     %{develname}
License:        BSD
Summary:        Headers for %{name}
Group:          System/Libraries
Provides: 	%{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}
 
%description -n %{develname}
Devel files for %{name}
 
%prep
%setup -q 
 
%build
echo %{version} > VERSION
make shared LIBDIR=%{_libdir}
 
%install
install -d -m 755 %{buildroot}%{_libdir}
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir}

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*
 
%files -n %{develname}
%{_libdir}/%{name}.so
%{_includedir}/x86emu.h
%doc README.md LICENSE


%changelog
* Sun Apr 10 2022 Igor Vlasenko <viy@altlinux.org> 3.5-alt1_1
- update by mgaimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_1
- update by mgaimport

* Mon Feb 17 2020 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_1
- update by mgaimport

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1
- new version

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

* Wed Jun 10 2009 snwint@suse.de
- avoid that error in future
* Tue Jun  9 2009 coolo@novell.com
- fix typo
* Tue Jun  9 2009 snwint@suse.de
- export only API functions in shared lib
* Wed Apr  8 2009 snwint@suse.de
- upgraded to version 1.0
- align to package conventions
