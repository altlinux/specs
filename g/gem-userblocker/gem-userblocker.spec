%define        _unpackaged_files_terminate_build 1
%define        gemname userblocker

Name:          gem-userblocker
Version:       0.0.1
Release:       alt2
Summary:       Squid lightsquid based userblocker
License:       GPLv3
Group:         Networking/WWW
Url:           https://git.altlinux.org/gears/u/userblocker.git
Vcs:           https://git.altlinux.org/gears/u/userblocker.git
Packager:      Timur Batyrshin <erthad@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ruby-ldap) >= 0
BuildRequires: gem(yaml) >= 0
BuildRequires: gem(date) >= 0
BuildRequires: gem(fileutils) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ruby-ldap) >= 0
Requires:      gem(yaml) >= 0
Requires:      gem(date) >= 0
Requires:      gem(fileutils) >= 0
Provides:      gem(userblocker) = 0.0.1


%description
UserBlocker is a simple program that blocks and unblocks the LDAP-stored Squid
users according to the traffic statistics collected by LightSquid.

It reads the usernames and blocking policy from LDAP, traffic statistics from
LightSquid reports and generates several text files to use in Squid or
redirecotr ACLs.


%package       -n userblocker
Version:       0.0.1
Release:       alt2
Summary:       Squid lightsquid based userblocker executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета userblocker
Group:         Other
BuildArch:     noarch

Requires:      gem(userblocker) = 0.0.1

%description   -n userblocker
Squid lightsquid based userblocker executable(s).

UserBlocker is a simple program that blocks and unblocks the LDAP-stored Squid
users according to the traffic statistics collected by LightSquid.

It reads the usernames and blocking policy from LDAP, traffic statistics from
LightSquid reports and generates several text files to use in Squid or
redirecotr ACLs.

%description   -n userblocker -l ru_RU.UTF-8
Исполнямка для самоцвета userblocker.


%package       -n gem-userblocker-devel
Version:       0.0.1
Release:       alt2
Summary:       Squid lightsquid based userblocker development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета userblocker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(userblocker) = 0.0.1

%description   -n gem-userblocker-devel
Squid lightsquid based userblocker development package.

UserBlocker is a simple program that blocks and unblocks the LDAP-stored Squid
users according to the traffic statistics collected by LightSquid.

It reads the usernames and blocking policy from LDAP, traffic statistics from
LightSquid reports and generates several text files to use in Squid or
redirecotr ACLs.

%description   -n gem-userblocker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета userblocker.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

mkdir -p %buildroot%_localstatedir/%gemname
mkdir -p %buildroot%_sysconfdir/cron.d
mkdir -p %buildroot%_sysconfdir/%gemname
mkdir -p %buildroot%_bindir
install -pm 755 exe/%gemname %buildroot%_bindir/%gemname
install -pm 640 config/%gemname.conf %buildroot%_sysconfdir/%gemname/%gemname.conf
install -pm 644 config/%gemname.cron %buildroot%_sysconfdir/cron.d/%gemname


%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n userblocker
%_bindir/userblocker
%dir %attr(0775,root,squid) %_localstatedir/%gemname
%dir %attr(0750,root,squid) %_sysconfdir/%gemname
%config %attr(0640,root,squid) %_sysconfdir/%gemname/%gemname.conf
%config %_sysconfdir/cron.d/%gemname

%files         -n gem-userblocker-devel


%changelog
* Mon Jun 19 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 04 2009 Timur Batyrshin <erthad@altlinux.org> 0.0.1-alt1
- initial package build
