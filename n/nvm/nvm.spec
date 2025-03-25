%def_disable   python

Name:          nvm
Version:       0.40.2
Release:       alt1
Summary:       Node Version Manager
License:       MIT
Group:         Development/Other
Url:           https://github.com/nvm-sh/nvm
Vcs:           https://github.com/nvm-sh/nvm.git
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       nvm.profile
Source2:       nvm.fish
Source3:       nvm.bash
Source4:       nvm.zsh
%if_enabled    python
Requires:      python3-devel
Requires:      python3-module-simplejson
%endif
Requires:      gcc-c++
Requires:      zlib-devel
Requires:      openssl-devel
Requires:      libbrotli-devel
Requires:      libuv-devel
Requires:      libicu-devel
Requires:      libnghttp2-devel
Requires:      libhttp-parser-devel
Requires:      libcares-devel
Requires:      curl
Conflicts:     zsh-completions

%description
Node Version Manager - POSIX-compliant bash script to manage multiple active
node.js versions.

nvm allows you to quickly install and use different versions of node via the
command line.


%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/nvm/ %buildroot%_sysconfdir/bash_completion.d/ %buildroot%_cachedir/nvm/
mkdir -p %buildroot%_localstatedir/nvm/alias %buildroot%_localstatedir/nvm/versions
chmod 755 ./bash_completion
ln -s ../../../%_localstatedir/nvm/alias/ ./alias
ln -s ../../../%_localstatedir/nvm/versions/ ./versions
ln -s ../../../%_cachedir/nvm/ ./.cache
cp -pr . %buildroot%_libexecdir/nvm/
install -D -m 755 %SOURCE1 %buildroot%_sysconfdir/profile.d/nvm.sh
install -D -m 755 %SOURCE2 %buildroot%_sysconfdir/fish/nvm
install -D -m 755 %SOURCE3 %buildroot%_sysconfdir/bashrc.d/nvm.sh
install -D -m 755 %SOURCE4 %buildroot%_datadir/zsh/site-functions/_nvm
ln -s ../../../%_libexecdir/nvm/bash_completion %buildroot%_sysconfdir/bash_completion.d/nvm

%post
[[ -s "/usr/lib/nvm/nvm.sh" ]] && source "/usr/lib/nvm/nvm.sh"

nvm alias default system

%files
%doc README.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md LICENSE.md PROJECT_CHARTER.md ROADMAP.md
%_libexecdir/nvm
%config(noreplace) %_sysconfdir/profile.d/nvm.sh
%_sysconfdir/fish/nvm
%_sysconfdir/bashrc.d/nvm.sh
%_datadir/zsh/site-functions/_nvm
%_sysconfdir/bash_completion.d/nvm
%dir %attr(775,root,root) %_cachedir/nvm/
%dir %attr(775,root,root) %_localstatedir/nvm/
%dir %attr(775,root,root) %_localstatedir/nvm/versions
%dir %attr(775,root,root) %_localstatedir/nvm/alias


%changelog
* Mon Aug 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.40.2-alt1
- ^ 0.39.3 -> 0.40.2
- ! use nvm with just users (closes #49588)
- * separated location of nvm node instances for root and regular users

* Wed Apr 05 2023 Pavel Skrylev <majioa@altlinux.org> 0.39.3-alt1
- initial build for Sisyphus
