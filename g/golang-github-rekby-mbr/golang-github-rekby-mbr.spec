%global import_path     github.com/rekby/mbr
%global gopath          %_datadir/gocode

Name: golang-github-rekby-mbr
Version: 0
Release: alt1
Summary: Library for direct work with MBR table
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar
BuildArch: noarch

%description
Library for direct work with MBR table.

%package devel
Summary: Library for direct work with MBR table
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Library for direct work with MBR table.

This package contains library source intended for building other packages
which use rekby/mbr.

%prep
%setup

%build
%install
install -d %buildroot/%gopath/src/%import_path
cp -av *.go %buildroot/%gopath/src/%import_path

%files devel
%doc LICENSE.txt README.txt
# %dir %attr(755,root,root) %gopath
# %dir %attr(755,root,root) %gopath/src
# %dir %attr(755,root,root) %gopath/src/github.com
# %dir %attr(755,root,root) %gopath/src/github.com/rekby
# %dir %attr(755,root,root) %gopath/src/github.com/rekby/mbr
# %gopath/src/%import_path/*.go
%gopath/src/%import_path

%changelog
* Mon Jan  4 2016 Terechkov Evgenii <evg@altlinux.org> 0-alt1
- Initial build for ALT Linux Sisyphus
