%define branch_release_num 1
Name: gitalt-tasker
Version: 0.0.1.13

%define branch_switch 

Summary: The useful script that creating tasks for package builder to ALT Linux's repositories
Summary(ru_RU.UTF-8): Полезный скрипт для отправки заданий на сборку в репозитории ALTLinux-a
License: GPL
Group: Development/Other
Packager: Dmitry Kharitonov <kharpost@altlinux.ru>

Url: http://git.altlinux.org/people/kharpost/packages/gitalt-tasker.git
Source: %name-%version.tgz
BuildRequires(pre): rpm-macros-branch
BuildRequires: coreutils
Requires: coreutils git-core rsync openssh rpm-utils rpm-macros-branch
Release: %branch_release alt1.6

BuildArch: noarch

%define gitalt_confdir %_sysconfdir
%define subpackage1 server
%define cachedir %_localstatedir/%name
%define cacherepos %cachedir/repos

%description
%name -- The useful script that creating tasks for package builder to ALT Linux's repositories

%description -l ru_RU.UTF-8
%name -- Полезный скрипт для отправки заданий на сборку в репозитории ALTLinux-a

%package %subpackage1
Summary: Server for %name
Summary(ru_RU.UTF-8): Сервер для %name
License: GPL
Group: Development/Other
Requires: %name = %version-%release
Requires: git-core openssh

%description %subpackage1
Server for %name

%prep
%setup -n %name-%version

%install
mkdir -p %buildroot%gitalt_confdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir/cron.d/
mkdir -p %buildroot%cachedir
touch %buildroot%cacherepos

# install bin
sed -i "s|source[[:space:]]*\"/etc/g.*|source \"%gitalt_confdir/git-task.conf\"|" git-task{,-server}
sed -i "s|cacherepos=\"/var/.*|cacherepos=\"%cacherepos\"|" git-task{,-server}
sed -i "s|version[[:space:]]\+.*\"|version %version-%release\"|" git-task{,-server}
install -p git-task{,-server} %buildroot%_bindir/

# install configs
install -p git-task.conf %buildroot%gitalt_confdir

# install cron
cat > %buildroot%_sysconfdir/cron.d/%name-server << EOF
*/10 * * * * root %_bindir/git-task-server

EOF

# install cache
cat > %buildroot%cacherepos << EOF
sisyphus
EOF

%files
#%dir %attr(1755,root,root) %gitalt_confdir
%config(noreplace) %attr(0644,root,root) %verify(not md5 size mtime) %gitalt_confdir/git-task.conf
%attr(0755,root,root) %_bindir/git-task
%attr(0666,root,root) %cacherepos


%files %subpackage1
#%_bindir
#%dir %attr(1755,root,root) %gitalt_confdir
%config(noreplace) %attr(0644,root,root) %verify(not md5 size mtime) %gitalt_confdir/git-task.conf
%attr(0744,root,root) %_bindir/git-task-server
%config(noreplace) %attr(0644,root,root) %verify(not md5 size mtime) %_sysconfdir/cron.d/%name-server

%changelog
* Wed Feb 17 2010 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.13-alt1.6
- Autocommit for branch sisyphus

* Wed Feb 17 2010 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.13-alt1.4.M40.1
- Fix analysing donetasks

* Wed Feb 17 2010 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.13-alt1.3.M40.1
- Add donetask analysing

* Tue Feb 16 2010 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.12-alt1.1.M40.1
- Add blacklist

* Fri Dec 04 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.12-alt1.1.5.M40.1
- Fix "server" option
- Fix git-*

* Thu Dec 03 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.12-alt1.1.0.M40.1
- Add repository name table
- Fix adding changelog

* Fri Oct 30 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.11-alt1.1.0.M40.1
- Fix gramar mistakes ALT #21901, ALT #21902

* Sun Oct 18 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.10-alt0.M40.1
- Add branch_release_num support

* Sat Sep 26 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.1.0-alt0.M41.1
- fix many bugs

* Thu Aug 27 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 0.0.0.1-alt0.M41.1
- initial release
