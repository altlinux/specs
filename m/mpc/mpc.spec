%define _unpackaged_files_terminate_build 1

%def_enable doc

%define subst_enable_meson_feature() %{expand:%%{?_enable_%{1}:-D%{2}=enabled}} %{expand:%%{?_disable_%{1}:-D%{2}=disabled}}
%define subst_enable_meson_bool() %{expand:%%{?_enable_%{1}:-D%{2}=true}} %{expand:%%{?_disable_%{1}:-D%{2}=false}}

Name: mpc
Version: 0.33
Release: alt1
Summary: Command line tool to interface MPD
License: %gpl2plus
Group: Sound
Url: https://mpd.wikia.com/?page=mpc

# https://github.com/MusicPlayerDaemon/mpc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): meson
BuildRequires: libmpdclient-devel
%if_enabled doc
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
%endif

%description
Music Player Command (%name) is a client for MPD, the Music Player
Daemon. %name connects to a MPD running on a machine via a network.

%prep
%setup

%build
%meson \
	-Diconv=enabled \
	%{subst_enable_meson_feature doc documentation} \
	%nil

%meson_build

%install
%meson_install

mkdir -p %buildroot%_sysconfdir/bash_completion.d

install -p -D -m0644 contrib/mpc-completion.bash \
    %buildroot%_sysconfdir/bash_completion.d/%name

rm -f %buildroot%_defaultdocdir/%name/contrib/mpc-completion.bash
rm -f %buildroot%_defaultdocdir/%name/html/.buildinfo

%check
%meson_test

%files
%config(noreplace) %_sysconfdir/bash_completion.d/%name
%_bindir/*
%if_enabled doc
%_man1dir/*
%endif
%_defaultdocdir/%name

%changelog
* Tue Jul 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.33-alt1
- Updated to upstream version 0.33.

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30-alt1
- Updated to upstream version 0.30.

* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.26-alt1.git20140603
- Version 0.26

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.19-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Oct 24 2010 Alexey Morsov <swi@altlinux.ru> 0.19-alt1
- new release version

* Mon Sep 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt2
- revert "disable character set conversion to/from pipe" (ALT #21080).

* Sun Aug 16 2009 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt1
- 0.17

* Sun Aug 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- 0.16
- thanks to led@ for his repository
- take upstream sources from the upstream git instead of tarballs

* Sun Dec 21 2008 Led <led@altlinux.ru> 0.14-alt1
- 0.14

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.12.1-alt0.3
- fixed Url

* Sun Aug 03 2008 Led <led@altlinux.ru> 0.12.1-alt0.2
- fixed Url (#9095)

* Sun Sep 09 2007 Led <led@altlinux.ru> 0.12.1-alt0.1
- 0.12.1
- cleaned up and fixed spec
- fixed License
- added %name-0.12.1-alt.patch

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.12.0-alt1
-  0.12.0.

* Wed Jan 18 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.2-alt1
-  0.11.2.

* Thu Feb 10 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.1-alt1
-  initial build.
