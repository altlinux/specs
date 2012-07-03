Name: rpm-macros-reponame
Summary: rpm macro for repository detect
Version: 5.0
Release: alt2
License: GPL
Group: System/Base
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>

Provides: reponame = %version-%release
Obsoletes: reponame < %version-%release

Source: %name-%version.tar

%description
%summary

%prep
%setup
%install
install -D -m644 reponame-sisyphus -p %buildroot%_sysconfdir/rpm/macros.d/reponame

%files
%_sysconfdir/rpm/macros.d/reponame

%changelog
* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 5.0-alt2
- rename to rpm-macros-reponame

* Thu May 06 2010 Denis Smirnov <mithraen@altlinux.ru> 5.0-alt1
- initial build for ALT Linux Sisyphus
