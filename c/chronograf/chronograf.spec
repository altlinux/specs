%global import_path github.com/influxdata/chronograf
%global commit de18060ef3b625466233484149505c35719f7642

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name:		chronograf
Version:	1.7.7
Release:	alt1
Summary:	Open source framework for processing, monitoring, and alerting on time series data

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/chronograf

Source0:	%name-%version.tar

Source100: %name.sysconfig
Source101: %name.logrotate
Source102: %name.init
Source103: %name.service
Source104: %name.tmpfiles

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64
BuildRequires(pre): rpm-build-golang
BuildRequires: npm yarn
BuildRequires: go-bindata
BuildRequires: /proc

%description
Open source framework for processing, monitoring, and alerting on time series data.

%prep
%setup -q

%build
# Important!!!
# The %%builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ export GOPATH="$PWD/.gopath"
# $ git rm -rf -- "$GOPATH"
# $ make
# $ find $GOPATH -type d -name .git |xargs rm -rf --
# $ git add "$GOPATH"
#
##cd ui && yarn --no-progress --no-emoji --verbose

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export PATH="$PATH:$BUILDDIR/bin"

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

%golang_prepare

pushd .gopath/src/%import_path
make
popd

#%golang_build cmd/*
#go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"

pushd .gopath/src/%import_path
go install github.com/influxdata/chronograf/cmd/chronograf
popd

install -p -D -m 755 $BUILDDIR/bin/chronograf %buildroot%_bindir/%name
install -d -m 755 %buildroot%_datadir/%name
cp -pr canned %buildroot%_datadir/%name
#%golang_install

#rm -rf -- %buildroot%_datadir

# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install sysconfig
install -p -D -m 640 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name
# Install logrotate
install -p -D -m 644 %SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Chronograf Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/sysconfig/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name
%_datadir/%name

%changelog
* Mon Jan 21 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.7-alt1
- 1.7.7

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.10.0-alt1%ubt
- 1.3.10.0

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.7.0-alt1%ubt
- 1.3.7.0

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5.0-alt1%ubt
- rebuild with Universal Branch Tag
- fix run with sysv init script

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5.0-alt1
- First build for ALTLinux.

