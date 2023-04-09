Name:          nvm
Version:       0.39.3
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
#Requires:      python3-devel
#Requires:      python3-module-simplejson
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

%pre
# Add the "foreman" user and group
getent group nvm >/dev/null || %_sbindir/groupadd -r nvm
getent passwd nvm >/dev/null || \
   %_sbindir/useradd -r -g nvm -G nvm -M -d %_localstatedir/nvm -s /bin/bash -c "NPM Version Manager" nvm
exit 0


%files
%doc README.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md LICENSE.md PROJECT_CHARTER.md ROADMAP.md
%_libexecdir/nvm
%config(noreplace) %_sysconfdir/profile.d/nvm.sh
%_sysconfdir/fish/nvm
%_sysconfdir/bashrc.d/nvm.sh
%_datadir/zsh/site-functions/_nvm
%_sysconfdir/bash_completion.d/nvm
%_sysconfdir/bash_completion.d/nvm
%dir %attr(775,nvm,nvm) %_cachedir/nvm/
%dir %attr(775,nvm,nvm) %_localstatedir/nvm/
%dir %attr(775,nvm,nvm) %_localstatedir/nvm/versions
%dir %attr(775,nvm,nvm) %_localstatedir/nvm/alias


%changelog
* Wed Apr 05 2023 Pavel Skrylev <majioa@altlinux.org> 0.39.3-alt1
- initial build for Sisyphus
