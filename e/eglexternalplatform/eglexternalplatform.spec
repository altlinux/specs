# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 7c8f8e2218e46b1a4aa9538520919747f1184d86
%global date 20180916
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           eglexternalplatform
Version:        1.2
Release:        alt1
Summary:        EGL External Platform Interface headers
Group:		System/Libraries

License:        MIT
URL:            https://github.com/NVIDIA
#Source0:        %url/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source0:        %name-%version.tar.gz

Source44: import.info

Buildrequires: meson libglvnd-devel

%description
%summary

%package        devel
Group: System/Libraries
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.


%prep
#setup -q -n %{name}-%{commit}
%setup

%build
%meson
%meson_build

%install
%meson_install
#mkdir -p %{buildroot}%{_includedir}/
#install -p -m 0644 interface/eglexternalplatform.h %{buildroot}%{_includedir}/
#install -p -m 0644 interface/eglexternalplatformversion.h %{buildroot}%{_includedir}/
#mkdir -p %{buildroot}%{_datadir}/pkgconfig/
#install -p -m 0644 eglexternalplatform.pc %{buildroot}%{_datadir}/pkgconfig/

%files devel
%doc README.md samples
%doc --no-dereference COPYING
%{_includedir}/*
%{_libdir}/pkgconfig/eglexternalplatform.pc

%changelog
* Tue Oct 08 2024 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- update by mgaimport

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- new version

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0
- new version
