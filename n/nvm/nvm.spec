%def_disable   python

Name:          nvm
Version:       0.40.2
Release:       alt1.1
Summary:       Node Version Manager
Summary(ru_RU.UTF-8): Справный урядник для ноды
License:       MIT
Group:         Development/Other
Url:           https://github.com/nvm-sh/nvm
Vcs:           https://github.com/nvm-sh/nvm.git
BuildArch:     noarch

Autoreq:       yes,noshell
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

%description   -l ru_RU.UTF-8
Справный урядник для ноды - POSIX-совместимый башев скрипт для управления
множествном установленных справ ноды.

сун (nvm) позволяет вам быстро установить и использовать различные справы ноды
в коммандной строке.


%package       tests
Summary:       Node Version Manager unit test modules
Summary(ru_RU.UTF-8): Проверочные звенья справного урядник для ноды
Group:         Development/Other
BuildArch:     noarch

Requires:      %name = %EVR

%description   tests
Node Version Manager unit test modules.

%description   tests -l ru_RU.UTF-8
Проверочные звенья справного урядника для ноды.


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
%exclude %_libexecdir/nvm/test
%exclude %_libexecdir/nvm/Dockerfile
%config(noreplace) %_sysconfdir/profile.d/nvm.sh
%_sysconfdir/fish/nvm
%_sysconfdir/bashrc.d/nvm.sh
%_datadir/zsh/site-functions/_nvm
%_sysconfdir/bash_completion.d/nvm
%dir %attr(775,root,root) %_cachedir/nvm/
%dir %attr(775,root,root) %_localstatedir/nvm/
%dir %attr(775,root,root) %_localstatedir/nvm/versions
%dir %attr(775,root,root) %_localstatedir/nvm/alias

%files         tests
%_libexecdir/nvm/test
%_libexecdir/nvm/Dockerfile

%changelog
* Fri Apr 18 2025 Pavel Skrylev <majioa@altlinux.org> 0.40.2-alt1.1
- ! fixed deps by splitting the packages and disabling some autos (ALT #53892)

* Mon Aug 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.40.2-alt1
- ^ 0.39.3 -> 0.40.2
- ! use nvm with just users (closes #49588)
- * separated location of nvm node instances for root and regular users

* Wed Apr 05 2023 Pavel Skrylev <majioa@altlinux.org> 0.39.3-alt1
- initial build for Sisyphus
