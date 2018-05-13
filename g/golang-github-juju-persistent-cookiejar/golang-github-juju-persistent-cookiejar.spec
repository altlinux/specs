%global import_path     github.com/juju/persistent-cookiejar

%global commit d5e5a8405ef9633c84af42fbcc734ec8dd73c198
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-persistent-cookiejar
Version: 0
Release: alt1.git%abbrev
Summary: Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar.
This implementation is a fork of net/http/cookiejar which also implements methods 
for dumping the cookies to persistent storage and retrieving them.

%package devel
Summary: Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar
Group: Development/Other
Requires: golang
Requires: golang(github.com/juju/go4/lock)
Requires: golang(gopkg.in/retry.v1)
Requires: golang(gopkg.in/errgo.v1)
BuildRequires: golang(github.com/juju/go4/lock)
BuildRequires: golang(gopkg.in/retry.v1)
BuildRequires: golang(gopkg.in/errgo.v1)
Provides: golang(%import_path) = %version-%release

%description devel
Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar.
This implementation is a fork of net/http/cookiejar which also implements methods 
for dumping the cookies to persistent storage and retrieving them.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.gitd5e5a840
- Initial package

