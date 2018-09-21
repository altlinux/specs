Name: astra
Version: 4.4
Release: alt8
Summary: Astra is a highly-customizable software for processing IPTV streams
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv3
Url: http://cesbo.com/astra
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libssl-devel

%ifarch %ix86 x86_64
BuildRequires: libdvbcsa-devel
%endif

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
./configure.sh \
%ifarch %ix86 x86_64
	--with-libdvbcsa \
%endif
	--bin=%_bindir/astra

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
%_sysconfdir/%name/
%_bindir/*

%changelog
* Mon Sep 10 2018 Pavel Skrylev <majioa@altlinux.org> 4.4-alt8
- Rebuild fix

* Tue Sep 04 2018 Alexei Takaseev <taf@altlinux.org> 4.4-alt7
- Rebuild with OpenSSL-1.1.x
- Support libdvbcsa only on x86 arches (fix build on ARM)

* Sat Jul 25 2015 Alexei Takaseev <taf@altlinux.org> 4.4-alt6
- update to 4.4.187

* Mon Jun 01 2015 Alexei Takaseev <taf@altlinux.org> 4.4-alt5
- update to 4.4.186

* Thu Mar 26 2015 Alexei Takaseev <taf@altlinux.org> 4.4-alt4
- update to 4.4.151

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
