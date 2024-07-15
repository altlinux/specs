
%define _unpackaged_files_terminate_build 1

Name: mle
Version: 1.7.2
Release: alt1
Summary: flexible terminal-based text editor (C) 
License:  Apache-2.0
Group: Other
Url: https://github.com/adsr/mle

Source: %name-%version.tar

BuildRequires: liblua-devel
BuildRequires: libpcre-devel
BuildRequires: libuthash-devel
BuildRequires: libpcre2-devel

%description
Mle is a small, flexible, terminal-based text editor written in C.

%prep
%setup
sed -i '/prefix?=/s,/usr/local,%prefix,' Makefile
sed -i 's|-llua5.4|-llua|g' Makefile
sed -i 's|<lua5.4/lua.h>|<lua.h>|g' mle.h
sed -i 's|<lua5.4/lualib.h>|<lualib.h>|g' mle.h
sed -i 's|<lua5.4/lauxlib.h>|<lauxlib.h>|g' mle.h

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std
mkdir -p %buildroot%_man1dir
install -m 0644 %name.1* %buildroot%_man1dir

%files
%doc README.*
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Fri Mar 01 2024 Pavel Shilov <zerospirit@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus
