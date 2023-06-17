%global import_path github.com/hashicorp/vault
%define vault_user vault
%define vault_group vault
%define config_dir vault.d

Name:    vault
Version: 1.13.3
Release: alt2

Summary: A tool for secrets management, encryption as a service, and privileged access management
License: MPL-2.0
Group:   Other
Url:     https://github.com/hashicorp/vault

Source: %name-%version.tar
Source1: %name.hcl.example
Source2: %name.service
Source3: %name.init
Source4: %name.tmpfiles
Source5: %name.sysconfig

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -pDm644 %SOURCE1 %buildroot%_sysconfdir/%config_dir/%name.hcl
install -pDm644 %SOURCE2 %buildroot%_unitdir/%name.service
touch %buildroot%_sysconfdir/%config_dir/%name.env
chmod 0644 %buildroot%_sysconfdir/%config_dir/%name.env
install -pDm755 %SOURCE3 %buildroot%_initdir/%name
install -pDm644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
install -pDm640 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name

%pre
if [ $1 == 1 ]; then
#Add the "vault" user
	%_sbindir/groupadd -r -f %vault_group 2>/dev/null ||:
	%_sbindir/useradd  -r -g %vault_group -c 'Vault daemon' \
		-s /dev/null -d /dev/null %vault_user 2>/dev/null ||:
fi

%post
# CAP_IPC_LOCK capability is needed for vault
setcap -q cap_ipc_lock+ep %_bindir/%name 2>/dev/null ||:

%files
%doc *.md
%_bindir/*
%dir %_sysconfdir/%config_dir
%config(noreplace) %_sysconfdir/%config_dir/%name.hcl
%config(noreplace) %_sysconfdir/%config_dir/%name.env
%_unitdir/%name.service
%_initdir/%name
%_sysconfdir/sysconfig/%name
%_tmpfilesdir/%name.conf

%changelog
* Sat Jun 17 2023 Nikolay Burykin <bne@altlinux.org> 1.13.3-alt2
- Fix repocop warning init-condrestart

* Wed Jun 14 2023 Nikolay Burykin <bne@altlinux.org> 1.13.3-alt1
- Initial build for Sisyphus
