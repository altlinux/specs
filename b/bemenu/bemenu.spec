Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/doxygen gcc-c++ libncurses-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit          442d2833f48590122e5ce54a2bca3a327ffa0311
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global checkout_date   20190819
%global snapshot        %{checkout_date}git%{shortcommit}

Name:       bemenu
Version:    0.1.0
Release:    alt1_3.%{snapshot}
Summary:    Dynamic menu library and client program inspired by dmenu

# Library and bindings are LGPLv3+, other files are GPLv3+
License:    GPLv3+ and LGPLv3+
URL:        https://github.com/Cloudef/bemenu
Source0:    %{url}/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  ctest cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
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
%setup -q -n %{name}-%{commit}


%build
%{fedora_cmake} \
    -DCURSES_NEED_WIDE=ON \
    -DBEMENU_WAYLAND_RENDERER=ON \
    "$PWD"
%make_build

%install
%makeinstall_std

%files
%doc README.md
%doc --no-dereference LICENSE-CLIENT LICENSE-LIB
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}*.1*
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.1.0
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_3.20190819git442d283
- new version

