%global import_path github.com/hashicorp/vault
%define vault_user vault
%define vault_group vault
%define config_dir vault.d
%def_with prebuild_webui

Name:    vault
Version: 1.13.12
Release: alt5

Summary: A tool for secrets management, encryption as a service, and privileged access management
License: MPL-2.0
Group:   Other
Url:     https://github.com/hashicorp/vault

Source: %name-%version.tar
Patch1: bbolt-loong64.patch
Patch2: gopsutil-loong64.patch
Patch3: vault-1.13.12-alt-fix-CVE-2024-2048.patch
Source1: %name.hcl.example
Source2: %name.service
Source3: %name.init
Source4: %name.tmpfiles
Source5: %name.sysconfig

BuildRequires(pre): rpm-build-golang
%if_without prebuild_webui
BuildRequires(pre): rpm-build-nodejs
BuildRequires: npm yarn
BuildRequires: node node-devel node-sass
%endif
BuildRequires: golang
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%if_without prebuild_webui
ln -sf %nodejs_sitelib/node-sass ui/node_modules
%endif

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="vault ui"
%if_without prebuild_webui
export PATH="$PATH:$PWD/webui/node_modules/.bin"
%endif

%golang_prepare

cd .build/src/%import_path

%if_without prebuild_webui
mkdir -p ./http/web_ui
pushd ui
#npm rebuild node-sass
npx browserslist@latest --update-db
yarn run --offline build
popd
%endif

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
* Thu Aug 29 2024 Nikolay Burykin <bne@altlinux.org> 1.13.12-alt5
- Fixes: CVE-2024-2048 (Closes: #51295)

* Fri Jun 14 2024 Nikolay Burykin <bne@altlinux.org> 1.13.12-alt4
- Fix duplicate entries in previous changelog note

* Fri Jun 14 2024 Nikolay Burykin <bne@altlinux.org> 1.13.12-alt3
- Bump go.mod for avoiding security risks
- Security fixes:
  + GHSA-9763-4f94-gfch
  + GHSA-mhpq-9638-x6pw
  + GHSA-7jwh-3vrq-q3m8
  + GHSA-5x4g-q5rc-36jp
  + CVE-2023-50658
  + CVE-2023-48795
  + CVE-2023-45288
  + CVE-2024-24786
  + CVE-2024-28180
  + CVE-2024-27289
  + CVE-2024-27304

* Wed Mar 06 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.13.12-alt2
- NMU: fixed FTBFS on LoongArch (patched vendored gopsutil and bbolt)

* Tue Mar 05 2024 Nikolay Burykin <bne@altlinux.org> 1.13.12-alt1
- New version 1.13.12
- CVE-2023-6337: Vault vulnerable to denial of service through memory exhaustion when handling large HTTP requests (High)

* Wed Aug 09 2023 Nikolay Burykin <bne@altlinux.org> 1.13.5-alt1
- 1.13.5
- build with webui (ALT #46783)

* Sat Jun 17 2023 Nikolay Burykin <bne@altlinux.org> 1.13.3-alt2
- Fix repocop warning init-condrestart

* Wed Jun 14 2023 Nikolay Burykin <bne@altlinux.org> 1.13.3-alt1
- Initial build for Sisyphus
