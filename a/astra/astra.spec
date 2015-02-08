Name: astra
Version: 4.4
Release: alt3
Summary: Astra is a highly-customizable software for processing IPTV streams
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv3
Url: http://cesbo.com/astra
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libssl-devel libdvbcsa-devel

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
#pushd contrib
#./ffmpeg.sh
#popd
./configure.sh --bin=%_bindir/astra --with-libdvbcsa
%make_build

%install
install -m 0755 -D %name %buildroot%_bindir/%name
install -m 0755 -D scripts/analyze.lua %buildroot%_sysconfdir/%name/scripts/analyze.lua
install -m 0755 -D scripts/base.lua %buildroot%_sysconfdir/%name/scripts/base.lua
install -m 0755 -D scripts/dvbls.lua %buildroot%_sysconfdir/%name/scripts/dvbls.lua
install -m 0755 -D scripts/relay.lua %buildroot%_sysconfdir/%name/scripts/relay.lua
install -m 0755 -D scripts/stream.lua %buildroot%_sysconfdir/%name/scripts/stream.lua

%files
%doc COPYING README.md Astra.sublime-project scripts/examples/*
#%config(noreplace) %_initdir/*
#%config(noreplace) %_sysconfdir/sysconfig/*
#%config %_sysconfdir/logrotate.d/*
#%config(noreplace) %_tmpfilesdir/*
%_sysconfdir/%name/
%_bindir/*

%changelog
* Sun Feb 08 2015 Alexei Takaseev <taf@altlinux.org> 4.4-alt3
- update to 4.4.111
- disable build ffmpeg libs

* Mon Feb 02 2015 Alexei Takaseev <taf@altlinux.org> 4.4-alt2
- update to 4.4.106

* Thu Nov 13 2014 Alexei Takaseev <taf@altlinux.org> 4.4-alt1
- update to 4.4.76

* Wed Oct 15 2014 Alexei Takaseev <taf@altlinux.org> 4.3-alt6
- ffmpeg libs: disable sse3, ssse3, sse4, sse42
- update to 4.3.118

* Sat Aug 30 2014 Alexei Takaseev <taf@altlinux.org> 4.3-alt5
- update to 4.3.117

* Fri Aug 15 2014 Alexei Takaseev <taf@altlinux.org> 4.3-alt4
- update to 4.3.114

* Sun Jun 29 2014 Alexei Takaseev <taf@altlinux.org> 4.3-alt3
- update to git:3a3c96e06263469b6ac0850e86105f602eea9564

* Thu May 29 2014 Alexei Takaseev <taf@altlinux.org> 4.3-alt2
- update to git:4552db1c6d80c797f505b9e51f8cb24c578f2893

* Tue Apr 29 2014 Alexei Takaseev <taf@altlinux.org> 4.3-alt1
- 4.3

* Mon Apr 21 2014 Alexei Takaseev <taf@altlinux.org> 4.2-alt1
- Initial RPM release
