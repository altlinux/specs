# spec file for package ssh_ping
#

Name: ssh_ping
Version: 0.1
Release: alt1

Summary: Utility for measuring SSH session latency

License: %asl 2.0
Group: Networking/Remote access
Url: https://github.com/jacobsa/ssh_ping

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-golang

# Automatically added by buildreq on Tue Oct 22 2024
# optimized out: golang golang-src libgpg-error python-modules python2-base python3-base sh5
#BuildRequires: rpm-build-golang

%description
ssh_ping is a utility for measuring SSH session latency.
It connects to a host over SSH, then repeatedly sends data
to be echoed back for five seconds and measures statistics
about the results.

%global import_path github.com/jacobsa/ssh_ping

%prep
%setup
%patch0 -p1

tar xf %SOURCE1

mv -f -- LICENSE LICENSE.ASL2.0.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE) LICENSE

%build
export GO111MODULE=auto
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
mkdir -p -- %buildroot%_bindir
cp .build/bin/%name  %buildroot%_bindir/

%files
%doc README.md
%doc --no-dereference LICENSE

%_bindir/%name

%changelog
* Tue Oct 22 2024 Nikolay A. Fetisov <naf@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
