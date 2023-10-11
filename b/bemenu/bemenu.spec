Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

Name:       bemenu
Version:    0.6.16
Release:    alt1_1
Summary:    Dynamic menu library and client program inspired by dmenu

# In case upstream do not bump program version when tagging; this should usually just resolve to %%{version}
%global     soversion   %{version}

# Library and bindings are LGPLv3+, other files are GPLv3+
License:    GPLv3+ and LGPLv3+
URL:        https://github.com/Cloudef/bemenu
Source0:    https://github.com/Cloudef/bemenu/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:    https://github.com/Cloudef/bemenu/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:    https://cloudef.pw/bemenu-pgp.txt

Patch:      respect-env-build-flags.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc
Source44: import.info

%description
%{summary}.

%package devel
Group: Other
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
Development files for extending %{name}.

%prep
%setup -q
%patch0 -p1


%build

%make_build   PREFIX='%{_prefix}' libdir='/%{_lib}'

%install
%makeinstall_std PREFIX='%{_prefix}' libdir='/%{_lib}'

%files
%doc README.md
%doc --no-dereference LICENSE-CLIENT LICENSE-LIB
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}*.1*
# Long live escaping! %%%% resolves to %%; $v%%.* strips everything after first dot
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{soversion}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.6.16-alt1_1
- update to new release by fcimport

* Fri Aug 25 2023 Igor Vlasenko <viy@altlinux.org> 0.6.3-alt2_1
- NMU: fixed build

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.6.3-alt1_1
- update to new release by fcimport

* Sun Mar 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- new version

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_3.20190819git442d283
- new version

