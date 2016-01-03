%global import_path     github.com/rekby/pflag
%global gopath          %_datadir/gocode

Name: golang-github-rekby-pflag
Version: 0
Release: alt1
Summary: pflag is a drop-in replacement for Go's flag package
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar
BuildArch: noarch

%description
pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

%package devel
Summary: pflag is a drop-in replacement for Go's flag package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

%prep
%setup

%build
%install
install -d %buildroot/%gopath/src/%import_path
cp -av *.go %buildroot/%gopath/src/%import_path

%files devel
%doc README.md LICENSE
# %dir %attr(755,root,root) %gopath
# %dir %attr(755,root,root) %gopath/src
# %dir %attr(755,root,root) %gopath/src/github.com
# %dir %attr(755,root,root) %gopath/src/github.com/rekby
# %dir %attr(755,root,root) %gopath/src/github.com/rekby/pflag
# %gopath/src/%import_path/*.go
%gopath/src/%import_path

%changelog
* Mon Jan  4 2016 Terechkov Evgenii <evg@altlinux.org> 0-alt1
- Initial build for ALT Linux Sisyphus
