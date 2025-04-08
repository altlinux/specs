# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major           3
%define libname         libcangjie%{major}
%define develname       libcangjie-devel

Name:             libcangjie
Summary:          Cangjie Input Method Library
Version:          1.4.0
Release:          alt1_1
License:          LGPLv3+
Group:            System/Internationalization
URL:              https://cangjie.pages.freedesktop.org/projects/libcangjie
Source0:          https://gitlab.freedesktop.org/cangjie/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:    meson
BuildRequires:    pkgconfig(sqlite3)
BuildRequires:    sqlite3
Source44: import.info

%description
Library implementing the Cangjie input method.

%package -n %{libname}
Summary:          Cangjie Input Method Library
Group:            System/Internationalization
# Split out so it can be noarch
Requires:         %{name}-data >= %{version}-%{release}

%description -n %{libname}
Library implementing the Cangjie input method.

%package data
Group: System/Internationalization
Summary:          Database for %{name}
BuildArch:        noarch

%description data
Database for %{name}.

%package -n %{develname}
Group: System/Internationalization
Summary:          Development files for %{name}
Requires:         %{libname} = %{version}-%{release}
Provides:         %{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q


%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n %{libname}
%doc AUTHORS README.md
%doc --no-dereference COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files data
%doc data/README.table.md
%{_datadir}/%{name}/

%files -n %{develname}
%{_bindir}/libcangjie*
%{_includedir}/cangjie/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/cangjie.pc



%changelog
* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt1_1
- update by mgaimport

* Sat Oct 12 2019 Michael Shigorin <mike@altlinux.org> 1.3-alt2_2
- E2K: strip UTF-8 BOM for lcc < 1.24
- autoreconf

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- new version

