Group: Development/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#%{!?lua_version: %global lua_version %(lua -e "print(string.sub(_VERSION, 5))")}
%global lua_version 5.3
%global lua_libdir %{_libdir}/lua/%{lua_version}
%global lua_pkgdir %{_datadir}/lua/%{lua_version}

BuildRequires:  libtool-common
BuildRequires:  lua5.3 >= 5.3
BuildRequires:  lua-devel >= 5.3

Name:           lua-mpack
Version:        1.0.4
Release:        alt1_2

License:        MIT
Summary:        Implementation of MessagePack for Lua
Url:            https://github.com/tarruda/libmpack/

Requires:       lua(abi) = %{lua_version}

Source0:        https://github.com/tarruda/libmpack/archive/%{version}/libmpack-%{version}.tar.gz
Source44: import.info

%description
mpack is a small binary serialization/RPC library that implements
both the msgpack and msgpack-rpc specifications.

%prep
%setup -q -n libmpack-%{version}

# hack to export flags
pushd binding/lua
echo '#!/bin/sh' > ./configure
chmod +x ./configure
popd

%build
pushd binding/lua
%configure
%make_build \
     USE_SYSTEM_LUA=yes \
     LUA_VERSION_MAJ_MIN=%{lua_version} \
     LUA_LIB=$(pkg-config --libs lua)
popd

%install
pushd binding/lua
make USE_SYSTEM_LUA=yes \
     LUA_CMOD_INSTALLDIR=%{lua_libdir} \
     DESTDIR=%{buildroot} \
     install
popd

%files
%doc LICENSE-MIT
%doc README.md
%{lua_libdir}/mpack.so

%changelog
* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- new version

