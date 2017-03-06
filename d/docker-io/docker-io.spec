%define _libexecdir /usr/libexec

%global provider        github
%global provider_tld    com
%global project         docker
%global repo            %{project}

%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit      8eab29edd820017901796eb60d4bea28d760f16f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       %{repo}-io
Version:    17.03.0
Release: alt1
Summary: Automates deployment of containerized applications
License: ASL 2.0
Group: System/Configuration/Other

%global versuffix ce
%global fullversion %{version}-%{versuffix}

Url: http://www.docker.io
# only x86_64 for now: https://github.com/docker/docker/issues/136
ExclusiveArch: x86_64
Conflicts: docker

# https://github.com/crosbymichael/docker
Source0: %name-%version.tar

BuildRequires: /proc gcc golang >= 1.3 systemd-devel libdevmapper-devel-static libsqlite3-devel-static libbtrfs-devel
BuildRequires: python-module-sphinx-devel python-module-sphinxcontrib-httpdomain pandoc
Requires: tar lxc xz
Provides: lxc-docker
Requires: /usr/bin/docker-proxy

%define gopath %_datadir/gocode

# do not extract debuginfo
%define __find_debuginfo_files %nil

# do not run debugedit for them
%add_debuginfo_skiplist /usr/bin/docker

%description
Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on
and between virtually any server. The same container that a developer builds
and tests on a laptop will run at scale, in production*, on VMs, bare-metal
servers, OpenStack clusters, public instances, or combinations of the above.

%package devel
Group: Development/Other
Requires: golang
Provides: docker-io-pkg-devel = %{version}-%{release}
Obsoletes: docker-io-pkg-devel <= 1.9.1
Summary: A golang registry for global request variables (source libraries)

%description devel
This is the source libraries for docker.

%prep
%setup
#rm -rf vendor
find . -name "*.go" \
        -print |\
        xargs sed -i 's/github.com\/docker\/docker\/vendor\/src\/code.google.com\/p\/go\/src\/pkg\///g'
sed -i 's/\!bash//g' contrib/completion/bash/docker
sed -i 's/go-md2man -in "$FILE" -out/pandoc -s -t man "$FILE" -o/g' man/md2man-all.sh

%build
# set up temporary build gopath, and put our directory there
mkdir -p ./_build/src/github.com/docker
ln -s $(pwd) ./_build/src/%{import_path}

export DOCKER_GITCOMMIT="%{shortcommit}/%{version}"
export DOCKER_BUILDTAGS='selinux journald'
export GOPATH=$(pwd)/_build:%{gopath}:$(pwd)/vendor

hack/make.sh dynbinary
man/md2man-all.sh
cp contrib/syntax/vim/LICENSE LICENSE-vim-syntax
cp contrib/syntax/vim/README.md README-vim-syntax.md

%install
# install binary
install -d %{buildroot}%{_bindir}
ls -la bundles/%{version}-%{versuffix}
install -p -m 755 bundles/%{fullversion}/dynbinary-client/docker-%{fullversion} %{buildroot}%{_bindir}/docker
install -p -m 755 bundles/%{fullversion}/dynbinary-daemon/dockerd-%{fullversion} %{buildroot}%{_bindir}/dockerd

# create symlinks on runc/containerd
ln -s %_bindir/runc %{buildroot}%{_bindir}/docker-runc
ln -s %_sbindir/containerd %{buildroot}%{_bindir}/docker-containerd
ln -s %_sbindir/containerd-shim %{buildroot}%{_bindir}/docker-containerd-shim
ln -s %_sbindir/ctr %{buildroot}%{_bindir}/docker-containerd-ctr

install -d %{buildroot}%{_libexecdir}/docker

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/man1/docker*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -p -m 644 man/man5/Dockerfile.5 %{buildroot}%{_mandir}/man5

# install bash completion
install -dp %{buildroot}%{_datadir}/bash-completion/completions
install -p -m 644 contrib/completion/bash/docker %{buildroot}%{_datadir}/bash-completion/completions

# install vim syntax highlighting
# (in process of being included in default vim)
install -d %{buildroot}%{_datadir}/vim/vimfiles/{doc,ftdetect,syntax}
install -p -m 644 contrib/syntax/vim/doc/dockerfile.txt %{buildroot}%{_datadir}/vim/vimfiles/doc
install -p -m 644 contrib/syntax/vim/ftdetect/dockerfile.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
install -p -m 644 contrib/syntax/vim/syntax/dockerfile.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax

# install udev rules
install -d %{buildroot}%{_sysconfdir}/udev/rules.d
install -p contrib/udev/80-docker.rules %{buildroot}%{_sysconfdir}/udev/rules.d

# install storage dir
install -d %{buildroot}%{_sharedstatedir}/%{repo}

# install systemd/init scripts
install -d %{buildroot}%{_unitdir}
install -p -m 644 altlinux/%{repo}.service %{buildroot}%{_unitdir}
install -p -m 644 altlinux/%{repo}-containerd.service %{buildroot}%{_unitdir}
install -p -D -m 755 altlinux/%{repo}.init %{buildroot}%{_initddir}/%{repo}

# sources
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
done

install -d %buildroot%_sysconfdir/sysconfig
install -p -m 644 altlinux/docker.sysconf %buildroot%_sysconfdir/sysconfig/docker
install -p -m 644 altlinux/docker-storage.sysconf %buildroot%_sysconfdir/sysconfig/docker-storage

%pre
getent group docker > /dev/null || %{_sbindir}/groupadd -r docker
exit 0

%post
%post_service docker

%preun
%preun_service docker

%files
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md
%doc LICENSE-vim-syntax README-vim-syntax.md
%config(noreplace) %{_sysconfdir}/sysconfig/docker
%config(noreplace) %{_sysconfdir}/sysconfig/docker-storage
%{_mandir}/man1/docker*.1.*
%{_mandir}/man5/Dockerfile.5.*
%{_bindir}/docker
%{_bindir}/dockerd
%{_bindir}/docker-runc
%{_bindir}/docker-containerd
%{_bindir}/docker-containerd-shim
%{_bindir}/docker-containerd-ctr
%dir %{_libexecdir}/docker
%{_unitdir}/docker.service
%{_unitdir}/docker-containerd.service
%_initdir/docker
%{_datadir}/bash-completion/completions/docker
%dir %{_sharedstatedir}/docker
%{_sysconfdir}/udev/rules.d/80-docker.rules
%{_datadir}/vim/vimfiles/doc/dockerfile.txt
%{_datadir}/vim/vimfiles/ftdetect/dockerfile.vim
%{_datadir}/vim/vimfiles/syntax/dockerfile.vim

%files devel
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}/

%changelog
* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 17.03.0-alt1
- New version

* Fri Feb 10 2017 Vladimir Didenko <cow@altlinux.org> 1.13.1-alt1
- New version

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.org> 1.13.0-alt1
- New version

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.org> 1.12.5-alt1
- New version

* Tue Nov 29 2016 Vladimir Didenko <cow@altlinux.org> 1.12.3-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.org> 1.12.2-alt1
- New version

* Tue Sep 20 2016 Alexandr Boltris <alex@altlinux.org> 1.12.1-alt2
- add docker-proxy. fixes #32489

* Fri Aug 19 2016 Vladimir Didenko <cow@altlinux.org> 1.12.1-alt1
- New version

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.org> 1.12.0-alt1
- New version

* Thu Jun 2 2016 Vladimir Didenko <cow@altlinux.org> 1.11.2-alt1
- New version

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.org> 1.11.1-alt1
- New version
- Remove manual provides

* Thu May 5 2016 Vladimir Didenko <cow@altlinux.org> 1.11.0-alt1
- New version

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.org> 1.10.3-alt1
- New version

* Thu Feb 25 2016 Vladimir Didenko <cow@altlinux.org> 1.10.2-alt1
- New version

* Tue Feb 16 2016 Vladimir Didenko <cow@altlinux.org> 1.10.1-alt1
- New version
- Restore bash completions

* Wed Feb 10 2016 Vladimir Didenko <cow@altlinux.org> 1.10.0-alt1.1
- fix provides

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.org> 1.10.0-alt1
- New version.
- Merge devel and pkg-devel packages
- add init script for sysvinit

* Wed Nov 25 2015 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt1
- New version.

* Fri Nov 6 2015 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- New version.

* Tue Oct 13 2015 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version.
- Return CAP_AUDIT_READ since std-def kernel supports it now
- Fix build with golang 1.5

* Mon Aug 24 2015 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version.

* Fri May 08 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.1-alt1
- Update to new version with security updates
 + Fix read/write /proc paths (CVE-2015-3630)
 + Prohibit VOLUME /proc and VOLUME / (CVE-2015-3631)
 + Fix opening of file-descriptor 1 (CVE-2015-3627)
 + Fix symlink traversal on container respawn allowing
   local privilege escalation (CVE-2015-3629)
 + Prohibit mount of /sys

* Sat Apr 18 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.0-alt1
- Update to last stable version
- Avoid of using CAP_AUDIT_READ capability for support
  less than 3.16.x kernel versions
- Rename dockerversion to autogen (c40993777f152426ea029)

* Wed Nov 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.1-alt1
- New version.
- Updated spec to Fedora 1.3.1-2.

* Mon Sep 15 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.0-alt1
- New version.

* Wed Aug 13 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.2-alt1
- New version.

* Thu Jun 19 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt2
- Dropped %%_datadir/vim/vimfiles/{doc,ftdetect,syntax}.

* Wed Jun 11 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1
- New version.

* Mon May 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.11.1-alt1
- New version.

* Wed Apr 23 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt2
- %%post: restored creation of docker group.

* Tue Apr 22 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt1
- New version.

* Mon Jan 06 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt1
- New version

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- New version

* Tue Nov 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.0-alt1
- Release

* Mon Nov 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt3.rc7
- New RC

* Sat Oct 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt3.rc4
- New RC

* Fri Oct 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt2.rc3
- Update up to upstream/v0.7-rc3 branch
- Add ExclusiveArch: x86_64
- Build docker-init statically

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt1.rc3
- Build for ALT
