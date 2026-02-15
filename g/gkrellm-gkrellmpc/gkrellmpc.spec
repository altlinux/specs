%define git 0aef2b2e6a
%define plugin gkrellmpc

Name: gkrellm-%plugin
Version: 0.2.0
Release: alt1.g%{git}

Summary: GKrellM plugin to control Music Player Daemon
License: GPL-2.0-only
Group: Monitoring
Url: https://git.srcbox.net/gkrellm/gkrellmpc
Vcs: https://git.srcbox.net/gkrellm/gkrellmpc
Source: %plugin-%version.tar

Requires: gkrellm >= 2.0

BuildRequires(pre): meson
BuildRequires: gkrellm-devel libgtk+2-devel libcurl-devel

%description
GKrellMPC is a GKrellm plugin to control Music Player Daemon.

%prep
%if_enabled debug
%add_optflags %optflags_debug
%endif

%setup -q -n %plugin-%version

%build
%meson -Dplugindir=%_libdir/gkrellm2/plugins
%meson_build

%install
%meson_install
%find_lang %plugin

%files -f %plugin.lang
%doc README.md CHANGELOG.md
%_libdir/gkrellm2/plugins/%plugin.so

%changelog
* Sun Feb 15 2026 L.A. Kostis <lakostis@altlinux.ru> 0.2.0-alt1.g0aef2b2e6a
- Use alternate fork (which still supported).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1_beta10-alt4.qa1
- NMU: rebuilt for debuginfo.

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
