%global import_path github.com/mattn/go-runewidth

%global commit e882a96ec18dd43fa283187b66af74497c9101c0
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-mattn-go-runewidth
Version: 0
Release: alt1.git%abbrev
Summary: Provides functions to get fixed width of the character or string.
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Provides functions to get fixed width of the character or string.

%package devel
Summary: Provides functions to get fixed width of the character or string.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Provides functions to get fixed width of the character or string.

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

mkdir -p -- %buildroot/%go_root/bin
for f in %buildroot/%_bindir/*; do
	[ -x "$f" ] || continue
	f="${f##*/}"
	what="$(relative %_bindir/$f %go_root/bin/$f)"
	ln -s -- "$what" %buildroot/%go_root/bin/$f
done


%files devel
%doc README.mkd
%go_path/src/*

%changelog
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gite882a96e
- Initial package

