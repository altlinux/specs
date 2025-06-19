Name: devzat
Version: 20250617
Release: alt1
License: MIT

Summary: The devs are over here at devzat, chat over SSH

Group: Networking/Instant messaging

Url: https://github.com/quackduck/devzat
Vcs: https://github.com/quackduck/devzat.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Devzat is a custom SSH server that takes you to a chat
instead of a shell prompt.

Because there's SSH apps on all platforms (even on phones)
you can connect to Devzat on any device!

%prep
%setup -a1

%build
%gobuild -mod=vendor

%install
install -D -m 0755 ./%name %buildroot/%_bindir/%name

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Thu Jun 19 2025 Kirill Unitsaev <fiersik@altlinux.org> 20250617-alt1
- Initial build
