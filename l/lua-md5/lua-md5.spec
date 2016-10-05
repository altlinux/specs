%global luaver 5.2
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-md5
Version:        1.1.2
Release:        alt1_12
Summary:        Cryptographic Library for MD5 hashes for Lua

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/md5/
Source0:        http://luaforge.net/frs/download.php/3355/md5-1.1.2.tar.gz
# https://github.com/keplerproject/md5/commit/ceb84044ad481409ea1179f1bed98440c29abb59
Patch0:		lua-md5-lua-5.2.patch

BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
Requires:       lua >= %{luaver}
Source44: import.info

%description
MD5 offers basic cryptographic facilities for Lua 5.1: a hash (digest)
function, a pair crypt/decrypt based on MD5 and CFB, and a pair crypt/decrypt
based on DES with 56-bit keys.

%prep
%setup -q -n md5-%{version}
%patch0 -p1 -b .lua-52


%build
make CFLAGS="%{optflags} -fPIC"


%install
mkdir -p %{buildroot}%{lualibdir}
mkdir -p %{buildroot}%{luapkgdir}
make install LUA_DIR=%{buildroot}%{luapkgdir} LUA_LIBDIR=%{buildroot}%{lualibdir}


%files
%doc README doc/us/*
%{luapkgdir}/*
%{lualibdir}/*


%changelog
* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.2-alt1_12
- converted for ALT Linux by srpmconvert tools

