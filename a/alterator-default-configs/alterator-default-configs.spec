%define _unpackaged_files_terminate_build 1
%define defaultsdir /lib/alterator/defaults

Name: alterator-default-configs
Version: 0.0.3
Release: alt1

Source: %name-%version.tar

BuildArch: noarch

Summary: default configs for alterator modules
License: GPLv2+
Group: System/Configuration/Other

%description
Default configuration files for different alterator modules.

%prep
%setup -q

%install
for f in krb5.conf \
         sssd/sssd.conf \
         samba/smb.conf \
         samba/usershares.conf;
do
    install -D "etc/$f" "%buildroot%defaultsdir/$f"
done

install -Dm 0755 default-restore %buildroot%_sbindir/default-restore

%files
%dir %defaultsdir
%dir %defaultsdir/sssd
%dir %defaultsdir/samba
%defaultsdir/*.conf
%defaultsdir/sssd/*.conf
%defaultsdir/samba/*.conf
%_sbindir/default-restore

%changelog
* Tue Nov 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.0.3-alt1
- Update samba defaults from samba-4.16.6-alt1 release.
- Update restore script with default configuration files actually placed in
  default directory as in the user's system.

* Tue Jun 07 2022 Ivan Savin <svn17@altlinux.org> 0.0.2-alt1
- Add script to restore configuration files to default.

* Tue May 31 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- Initial commit.

