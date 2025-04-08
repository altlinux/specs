Name: autorepo-altnode-cronbuild
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: scripts for an automated cronbuild node
Group: Other
License: GPLv2+ or ALT-Public-Domain
Url: http://cronbuild.altlinux.org
Source: %name-%version.tar

# for now; TODO: build our own statistics wrappers
Requires: /usr/bin/autorepo-altnode-misc-statistics-wrapper
Requires(pre): autorepo-altnode-config
#BuildRequires: /usr/bin/parentlock
Requires: hasher gear mutt
Requires: /usr/bin/parentlock

# for cronbuild
#BuildRequires: gear-cronbuild girar-tools /usr/bin/girar-nmu-filter-name /usr/bin/altlinux-acl-get-leader
Requires: gear-cronbuild girar-tools /usr/bin/girar-nmu-filter-name /usr/bin/altlinux-acl-get-leader
# for croncopy && cronport
#BuildRequires: /usr/bin/croncopy-girar-copymass /usr/bin/cronport-backportmass
Requires: /usr/bin/croncopy-girar-copymass
Requires: /usr/bin/cronport-backportmass

%description
scripts for an automated cronbuild node
in "autorepo" Automated Package Maintainance Cluster.

%prep
%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%_bindir
#install -m 755 repocop-* $RPM_BUILD_ROOT%_bindir

# no user yet :(
%if 0
%post
if ! [ -d /var/ftp/pub/cronbuild ]; then
    mkdir -p /var/ftp/pub/cron{build,port,copy}
    chmod 775 /var/ftp/pub/cron{build,port,copy}
fi
%endif

%files
%doc crontab.*
#%_bindir/*

%changelog
* Tue Nov 14 2023 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- First build for Sisyphus.
