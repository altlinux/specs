%global import_path github.com/ContentSquare/chproxy

Name:     chproxy
Version:  1.26.3
Release:  alt1

Summary:  Open-Source ClickHouse http proxy and load balancer 
License:  MIT
Group:    Networking/Other
Url:      https://www.chproxy.org/

ExclusiveArch: %go_arches
Source:   %name-%version.tar
Source1:  %name.init
Source2:  %name.service
Source3:  %name.tmpfiles
Source4:  %name.yml.example

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.

%prep
%setup

cp -- %SOURCE4 %name.yml

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd $BUILDDIR/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -pDm755 %SOURCE1 %buildroot/%_initdir/%name
install -pDm644 %SOURCE2 %buildroot/%_unitdir/%name.service
install -pDm644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf
install -m 0750 -d -- %buildroot%_sysconfdir/%name

%pre
if [ $1 = 1 ]; then
# Add the "chproxy" user and group
    getent group chproxy > /dev/null || groupadd -r chproxy
    getent passwd chproxy > /dev/null || \
        useradd -r -g chproxy -s /sbin/nologin -d /var/lib/chproxy chproxy
fi

%files
%doc *.md %name.yml
%_bindir/*
%_unitdir/chproxy.service
%_initdir/chproxy
%dir %_sysconfdir/%name
%_tmpfilesdir/%name.conf

%changelog
* Mon Jun 10 2024 Nikolay Burykin <bne@altlinux.org> 1.26.3-alt1
- Initial build for ALT

