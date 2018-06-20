# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 76e29488ca3a34e5ef58a4c83d8cd857b621de2a
%global date 20170201
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           eglexternalplatform
Version:        1.0
Release:        alt1_0
Summary:        EGL External Platform Interface headers
Group:		System/Libraries

License:        MIT
URL:            https://github.com/NVIDIA
Source0:        %url/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
Source44: import.info

%description
%summary

%package        devel
Group: System/Libraries
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{commit}


%build

%install
mkdir -p %{buildroot}%{_includedir}/
install -p -m 0644 interface/eglexternalplatform.h %{buildroot}%{_includedir}/
install -p -m 0644 interface/eglexternalplatformversion.h %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_datadir}/pkgconfig/
install -p -m 0644 eglexternalplatform.pc %{buildroot}%{_datadir}/pkgconfig/

%files devel
%doc README.md samples
%doc --no-dereference COPYING
%{_includedir}/*
%{_datadir}/pkgconfig/eglexternalplatform.pc




%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0
- new version

