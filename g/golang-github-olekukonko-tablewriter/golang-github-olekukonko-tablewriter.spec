%global import_path github.com/olekukonko/tablewriter

%global commit febf2d34b54a69ce7530036c7503b1c9fbfdf0bb
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-olekukonko-tablewriter
Version: 0
Release: alt3.git%abbrev
Summary: Generate ASCII table on the fly...
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
Generate ASCII table on the fly...

%package devel
Summary: Generate ASCII table on the fly...
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release
Requires: golang(github.com/mattn/go-runewidth)

%description devel
Generate ASCII table on the fly...

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

rm -rf -- %buildroot/%go_path/src/%import_path/csv2table


%files devel
%doc README.md LICENCE.md
%go_path/src/*

%changelog
* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 0-alt3.gitfebf2d34
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.gitdaf2955e
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitcca8bbc0
- Initial package

