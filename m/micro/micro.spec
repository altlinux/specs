Name: micro
Version: 2.0.10
Release: alt1
Summary: A modern and intuitive terminal-based text editor
License: MIT/BSD/Apache-2.0/MPL-2.0
Group: Editors
Url: https://micro-editor.github.io/
Packager: Ivan Razzhivin <underwit@altlinux.org>
Source0: %name-%version.tar
BuildRequires: desktop-file-utils rpm-build-golang rpm-macros-golang
BuildRequires: golang >= 1.5

%description
Micro is a terminal-based text editor that aims to be easy to use and
intuitive, while also taking advantage of the full capabilities of modern
terminals. It comes as one single, batteries-included, static binary with no
dependencies, and you can download and use it right now. As the name
indicates, micro aims to be somewhat of a successor to the nano editor by
being easy to install and use in a pinch, but micro also aims to be enjoyable
to use full time, whether you work in the terminal because you prefer it (like
me), or because you need to (over ssh).

%prep
%setup -q

%build
%gobuild -mod=vendor ./cmd/micro

%install
install -D -m 0755 ./micro %buildroot/%_bindir/micro
install -D -m 0744 ./assets/packaging/micro.1 %buildroot/%_man1dir/micro.1
install -D -m 0744 ./assets/micro-logo.svg %buildroot/%_iconsdir/hicolor/scalable/apps/micro.svg
desktop-file-install --dir=%buildroot%_desktopdir ./assets/packaging/micro.desktop

%files
%doc LICENSE README.md LICENSE-THIRD-PARTY
%_bindir/micro
%_man1dir/micro.1*
%_iconsdir/hicolor/scalable/apps/micro.svg
%_desktopdir/micro.desktop

%changelog
* Mon Oct 04 2021 Ivan Razzhivin <underwit@altlinux.org> 2.0.10-alt1
- new version

* Thu Apr 22 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.1-alt2
- fix build with golang 1.16

* Mon Sep 3 2018 Ivan Razzhivin <underwit@altlinux.org> 1.4.1-alt1
- new version

* Wed Jul 11 2018 Ivan Razzhivin <underwit@altlinux.org> 1.4.0-alt1
- Build for ALT
