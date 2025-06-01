Name: plasma-addon-krohnkite
Version: 0.9.9.1
Release: alt2

Summary: A dynamic tiling extension for KWin 6 only
License: MIT
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2144146
Vcs: https://github.com/anametologin/krohnkite

Source0: %name-%version.tar
Source1: node_modules.tar

ExcludeArch: i586

BuildRequires(Pre): rpm-macros-make
BuildRequires: git npm node

%description
%summary

%prep
%setup -a1

%build
git config --global user.email "user at altlinux.org"
git config --global user.name "user"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version
%make_build

%install
mkdir -p %buildroot%_datadir/kwin/scripts/krohnkite
%make_install
cp -a -r pkg/* %buildroot%_datadir/kwin/scripts/krohnkite/


%files
%doc *.md LICENSE
%_datadir/kwin/scripts/krohnkite

%changelog
* Sun Jun 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.9.1-alt2
- Fix FTBFS: exclude i586 arch due to idle time limit exceeded.

* Mon May 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.9.1-alt1
- Initial build for ALT Linux.
