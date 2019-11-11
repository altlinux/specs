Name:     adp
Version:  1.0
Release:  alt2

Summary:  ALT Domain Policy
License:  GPL-3.0+
Group:    Other
Url:      http://altlinux.org/adp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): alterator
Requires: krb5-kinit
Requires: samba-client
Requires(preun): sssd-client
Requires(post): sssd-client
Requires: sssd-client
Requires: %name-templates
Requires: python3-modules-sqlite3

BuildArch: noarch

%description
Apply Linux-specific domain policies for Active Directory user or machine.

%package templates
Summary: Set of ALT Domain Policies templates
Group: Other

%description templates
Set of ALT Domain Policies templates.

%package -n alterator-domain-policy
Summary: Alterator module for configure ALT Domain Policy
Group: System/Configuration/Other
Requires: alterator
Requires: alterator-sh-functions
Requires: alterator-net-domain
Requires: alterator-l10n
Requires: %name-templates
Requires: task-samba-dc

%description -n alterator-domain-policy
Alterator module for configure ALT Domain Policy.

%prep
%setup

%build
cd alterator-domain-policy
%make_build

%install
install -Dm 0755 bin/adp %buildroot%_bindir/adp
install -Dm 0755 bin/adp-functions %buildroot%_bindir/adp-functions
install -Dm 0755 bin/adp-helper %buildroot%_bindir/adp-helper
install -Dm 0755 sbin/adp-fetch %buildroot%_sbindir/adp-fetch
install -Dm 0644 adp.sysconfig %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%python3_sitelibdir/%name
cp -av lib/*.py %buildroot%python3_sitelibdir/%name
mkdir -p %buildroot%_prefix/libexec/%name
cp -av templates/* %buildroot%_prefix/libexec/%name

install -d -m 0770 %buildroot%_sharedstatedir/%name
install -d -m 0770 %buildroot%_logdir/%name

install -Dm0644 %name.desktop %buildroot%_sysconfdir/xdg/autostart/%name.desktop
install -Dm0644 %name.service %buildroot%_unitdir/%name.service

cd alterator-domain-policy
%makeinstall

%preun
%preun_service adp
if [ $1 -eq 0 ]; then
    ### Remove adp-fetch from /etc/pam.d/system-auth-sss on package uninstall
    subst '/adp-fetch/d' /etc/pam.d/system-auth-sss
fi

%post
if [ $1 -eq 0 ]; then
    ### Add adp-fetch to /etc/pam.d/system-auth-sss on package install
    if ! grep -q 'adp-fetch' /etc/pam.d/system-auth-sss ; then
	echo -e "session\t\toptional\tpam_exec.so\t/usr/sbin/adp-fetch" >> /etc/pam.d/system-auth-sss
    fi
fi
%post_service adp

%check
make check

%files
%doc *.md
%doc examples
%_bindir/%name
%_sbindir/adp-fetch
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_prefix/libexec/%name
%attr(0770, root, users) %_sharedstatedir/%name
%attr(0770, root, users) %_logdir/%name
%_sysconfdir/xdg/autostart/%name.desktop
%_unitdir/%name.service
%python3_sitelibdir/%name
#python3_sitelibdir/*.egg-info

%files templates
%_bindir/adp-functions
%_prefix/libexec/%name/*

%files -n alterator-domain-policy
%_bindir/adp-helper
%_alterator_backend3dir/*
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/*

%changelog
* Mon Nov 11 2019 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Fix is in templates (ALT #37455).
- Add %%check in spec file.

* Fri Oct 25 2019 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
