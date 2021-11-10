%define git %nil

Name: nvme
Version: 1.15
Release: alt1
Summary: Core nvme tools
License: GPL-2
Group: System/Configuration/Hardware
Url: https://github.com/linux-nvme/nvme-cli/
Source: nvme-%version.tar
Provides: nvme-cli
BuildRequires: libuuid-devel libjson-c-devel
Requires(post): util-linux

%description
NVMe is a fast, scalable, direct attached storage interface. The nvme
cli rpm installs core management tools with minimal dependencies.

%package -n bash-completion-%name
Summary: Bash completion for %name
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %version-%release

%description -n bash-completion-%name
Bash completion for %name.

%package -n zsh-completion-%name
Summary: Zsh completion for %name
Group: Shells
BuildArch: noarch
Requires: %name = %version-%release

%description -n zsh-completion-%name
Zsh completion for %name.

%prep
%setup

%build
# subst 's,$(NVME_VERSION),%%version-g%%{git},' Makefile
CFLAGS="%optflags" \
%make_build

%install
%make install \
   DESTDIR=%buildroot \
   UDEVRULESDIR=%_udevrulesdir \
   SYSTEMDDIR=/lib/systemd \
   PREFIX=/usr
touch %buildroot%_sysconfdir/%name/{hostnqn,hostid}

%files
%doc *.md LICENSE
%_sbindir/nvme
%_man1dir/nvme*.1*
%_udevrulesdir/*
%_unitdir/*
%dir %_sysconfdir/%name
%_sysconfdir/%name/*.conf
%ghost %attr(644,root,root) %config(missingok) %verify(not md5 mtime size) %_sysconfdir/%name/host*

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/_nvme

%post
if [ $1 = 1 ]; then # 1 : This package is being installed for the first time
                uuidgen > /etc/nvme/hostid
		nvme gen-hostnqn > /etc/nvme/hostnqn
fi

%changelog
* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 1.15-alt1
- 1.15 (closes #41284).

* Tue Jul 13 2021 L.A. Kostis <lakostis@altlinux.ru> 1.14-alt1
- 1.14.
- Added json-c into BR.
- Split shell completions into subpackages.

* Wed Sep 09 2020 L.A. Kostis <lakostis@altlinux.ru> 1.11.2-alt1
- 1.11.2.

* Fri May 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt1.g9c0660a
- GIT 9c0660a.

* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt5.g0b78004
- Fixed build.

* Tue Jan 02 2018 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt4.g0b78004
- GIT 0b78004.

* Thu Oct 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt3
- Remove invasive postun cmds, use %%ghost for configuration.

* Thu Oct 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt2
- Rebuild with uuid support.
- Re-organize documentation.

* Thu Oct 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1
- Initial build for ALTLinux.

* Thu Oct 15 2015 Keith Busch <keith.busch@intel.com>
- Initial RPM spec
