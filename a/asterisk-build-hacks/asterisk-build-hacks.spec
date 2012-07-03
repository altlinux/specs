Name: asterisk-build-hacks
Summary: Some dirty hacks for Asterisk build
Version: 0.0.1
Release: alt2
License: GPL
Group: Development/C
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>
Url: http://sisyphus.ru/ru/srpm/Sisyphus/asterisk-build-hacks
AutoReq: no
Requires: liblua5-devel

%description
Some dirty hacks for Asterisk build


%install
mkdir -p %buildroot%_includedir/lua5.1
for s in lua.h lauxlib.h lualib.h; do
	ln -s %_includedir/"$s" %buildroot%_includedir/lua5.1/"$s"
done

%files
%_includedir/lua5.1

%changelog
* Sun Sep 27 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt2
- add Url tag

* Fri Sep 18 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

