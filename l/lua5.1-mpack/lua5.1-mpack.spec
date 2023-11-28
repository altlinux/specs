Group: Development/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#%{!?lua_version: %global lua_version %(lua -e "print(string.sub(_VERSION, 5))")}
%global lua_version 5.1
%global lua_libdir %{_libdir}/lua/%{lua_version}
%global lua_pkgdir %{_datadir}/lua/%{lua_version}

BuildRequires:  lua5.1-devel

Name:           lua5.1-mpack
Version:        1.0.11
Release:        alt1

License:        MIT
Summary:        libmpack lua binding
Url:            https://github.com/libmpack/libmpack-lua

Requires:       lua(abi) = %{lua_version}
BuildRequires:  libmpack-devel

Source0:        libmpack-lua-%{version}.tar

%description
libmpack lua binding

%prep
%setup -q -n libmpack-lua-%{version}

%build
%make USE_SYSTEM_LUA=1 USE_SYSTEM_MPACK=1

%install
install -p -D -m 644 mpack.so %buildroot%{lua_libdir}/mpack.so

%files
%doc LICENSE-MIT
%doc README.md
%{lua_libdir}/mpack.so

%changelog
* Tue Nov 28 2023 Vladimir Didenko <cow@altlinux.ru> 1.0.11-alt1
- new version

* Fri May 5 2023 Vladimir Didenko <cow@altlinux.ru> 1.0.10-alt1
- new version

* Wed Nov 3 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.9-alt1
- new version

* Wed Sep 18 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.8-alt1
- new version for lua5.1

* Tue Jul 10 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.4-alt2_2
- rebuild for aarch architecture

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- new version
