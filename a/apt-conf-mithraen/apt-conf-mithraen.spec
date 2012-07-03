Name: apt-conf-mithraen
Summary: arepo repository by Denis Smirnov
Version: 1.0
Release: alt1

License: GPL
Group: System/Base
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildRequires: reponame

Source: %name-%version.tar

%description
%summary

%prep
%setup
%install
%if_with M51
install -D -m644 sources.list.M51 -p %buildroot%_sysconfdir/apt/sources.list.d/mithraen.list
%endif
%if_with sisyphus
install -D -m644 sources.list.sisyphus -p %buildroot%_sysconfdir/apt/sources.list.d/mithraen.list
%endif

%files
%_sysconfdir/apt/sources.list.d/mithraen.list
%changelog
* Tue May 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build for Sisyphus

