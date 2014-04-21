Name: astra
Version: 4.2
Release: alt1
Summary: Astra is a high-customizable software to processing IPTV streams
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv3
Url: http://cesbo.com/astra
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libssl-devel

%description
Astra consists of the following components:

*   Core is an API to communicate with the operation system. Astra is a
    cross-platform software that supports:
    OS X, Linux (any distributives), BSD, Windows
*   Modules is a set of high-performance units that
    carries out specific functions
*   Lua is a scripting language to build a business logic for applications

%prep
%setup
%patch0 -p1

%build
pushd contrib
./ffmpeg.sh
popd
./configure.sh --bin=%_bindir/astra --scripts=%_sysconfdir/%name/scripts
%make_build

%install
install -m 0755 -D %name %buildroot%_bindir/%name
install -m 0755 -D scripts/analyze.lua %buildroot%_sysconfdir/%name/scripts/analyze.lua
install -m 0755 -D scripts/dvbls.lua %buildroot%_sysconfdir/%name/scripts/dvbls.lua
install -m 0755 -D scripts/xproxy.lua %buildroot%_sysconfdir/%name/scripts/xproxy.lua

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING README.md Astra.sublime-project scripts/stream.lua scripts/examples/*
#%config(noreplace) %_initdir/*
#%config(noreplace) %_sysconfdir/sysconfig/*
#%config %_sysconfdir/logrotate.d/*
#%config(noreplace) %_tmpfilesdir/*
%_sysconfdir/%name/
%_bindir/*

%changelog
* Mon Apr 21 2014 Alexei Takaseev <taf@altlinux.org> 4.2-alt1
- Initial RPM release
