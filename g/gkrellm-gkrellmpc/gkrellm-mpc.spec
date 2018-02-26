%define plugin gkrellmpc

Name: gkrellm-%plugin
Version: 0.1_beta10
Release: alt4

Summary: GKrellM plugin to control Music Player Daemon
License: GPL
Group: Monitoring
Url: http://www.musicpd.org/wiki/moin.cgi/GKrellMPC
Source: http://www.topfx.com/dist/gkrellmpc-%version.tar.gz
Patch0: gkrellmpc-0.1_beta10-alt-makefile-fixes.patch
Patch1: gkrellmpc-0.1_beta10-alt-memleaks-fixes.patch
Patch2: gkrellmpc-0.1_beta10-alt-fd-leak-fix.patch

Requires: gkrellm >= 2.0

BuildPreReq: gkrellm-devel libgtk+2-devel libcurl-devel

%description
GKrellMPC is a GKrellm plugin to control Music Player Daemon.

%prep
%if_enabled debug
%add_optflags %optflags_debug
%endif

%setup -q -n gkrellmpc-%version
%patch0 -p1
%patch1 -p1
%patch2 -p2
%__subst 's|^CFLAGS +=.*|\0 %optflags|' Makefile

%build
%make_build 

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
install -m755 %plugin.so %buildroot%_libdir/gkrellm2/plugins/%plugin.so

%files
%doc README.txt Changelog
%_libdir/gkrellm2/plugins/%plugin.so

%changelog
* Wed May 02 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1_beta10-alt4
- fix fd leak

* Tue Mar 27 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1_beta10-alt3
- rebuild with libcurl.so.4

* Wed Oct 18 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.1_beta10-alt2
- fix building with --as-needed
- fix memory leaks
- use optflags

* Sat Mar  5 2005 Sergey Pinaev <dfo@altlinux.ru> 0.1_beta10-alt1
- 0.1_beta10

* Tue Mar  1 2005 Sergey Pinaev <dfo@altlinux.ru> 0.1_beta9-alt1
- First build for ALT Linux
