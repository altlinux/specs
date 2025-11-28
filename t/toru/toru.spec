Name: toru
Version: 0.3.3
Release: alt2

Summary: Bittorrent streaming CLI tool. Stream anime torrents, real-time with no waiting for downloads.
License: MIT
Group: Video
Url: https://github.com/sweetbbak/toru
Vcs: https://github.com/sweetbbak/toru

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: go clang libstdc++-devel

%description
%summary

%prep
%setup -a1
subst 's|go mod tidy|# go mod tidy|' Makefile

%build
export CC=clang
export CXX=clang++
%make_build

%install
install -D %name %buildroot%_bindir/%name

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Fri Nov 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.3-alt2
- vendor cleanup

* Mon May 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.3-alt1
- Initial build for ALT Linux.
