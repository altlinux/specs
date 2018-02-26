Name: installer-feature-resolver-bind-stage3
Version: 0.2
Release: alt4

Summary: Setup bind as a main local resolver
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Stanislav Ievlev <inger@altlinux.org>
BuildArch: noarch
Requires: bind etcnet openresolv-bind
Source: %name-%version.tar

%description
This package contains installer stage3 hook to setup bind
as a main local resolver.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt4
- require openresolv-bind.

* Thu Aug 06 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt3
- create resolv.conf for 'lo' interface.

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- update for latest openresolv

* Mon Apr 13 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Cleanup.

* Sun Apr 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- touch included files to create correct configuration for bind

* Tue Mar 17 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- move to stage3

* Mon Mar 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
