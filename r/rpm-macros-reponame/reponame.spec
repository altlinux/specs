Name: rpm-macros-reponame
Summary: rpm macro for repository detect
Version: 5.0
Release: alt3
License: GPLv2+
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
install -D -m644 reponame-sisyphus -p %buildroot%_rpmmacrosdir/reponame

%files
%_rpmmacrosdir/reponame

%changelog
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 5.0-alt3
- NMU: use %%_rpmmacrosdir instead of /etc/rpm

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 5.0-alt2
- rename to rpm-macros-reponame

* Thu May 06 2010 Denis Smirnov <mithraen@altlinux.ru> 5.0-alt1
- initial build for ALT Linux Sisyphus
