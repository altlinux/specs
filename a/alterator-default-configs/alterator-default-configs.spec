Name: alterator-default-configs
Version: 0.0.2
Release: alt1

Source:%name-%version.tar

BuildArch: noarch

Summary: default configs for alterator modules
License: GPLv2+
Group: System/Configuration/Other

%description
Default configuration files for different alterator modules.

%prep
%setup -q

%build

%install
mkdir -p %buildroot/lib/alterator/defaults
cp etc/krb5.conf %buildroot/lib/alterator/defaults
cp etc/sssd/sssd.conf %buildroot/lib/alterator/defaults
cp etc/samba/smb.conf %buildroot/lib/alterator/defaults

mkdir -p %buildroot%_sbindir
install -m 0755 default-restore %buildroot%_sbindir/default-restore

%files
/lib/alterator/defaults/*.conf
%_sbindir/default-restore

%changelog
* Tue Jun 07 2022 Ivan Savin <svn17@altlinux.org> 0.0.2-alt1
- Add script to restore configuration files to default.

* Tue May 31 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- Initial commit.

