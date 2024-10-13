%define oname vim-repeat

Name: vim-plugin-repeat
Version: 1.2.0.15.git6584602
Release: alt1

Summary: Vim plugin to remap "." in a plugin-friendly way

License: Vim
Group: Editors
Url: https://github.com/tpope/vim-repeat

VCS: git://git.altlinux.org/gears/v/vim-plugin-repeat.git
Source: %name-%version-%release.tar
Source1: %name.watch

Provides: %oname

BuildRequires: rpm-build-vim
BuildArch: noarch

%description
If you've ever tried using the `.` command after a plugin map, you were
likely disappointed to discover it only repeated the last native command
inside that map, rather than the map as a whole.  That disappointment
ends today.  Repeat.vim remaps `.` in a way that plugins can tap into
it.

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a autoload %buildroot%vim_runtime_dir

%files
%doc README.*
%vim_runtime_dir/*/*

%changelog
* Sat Oct 12 2024 Arseny Maslennikov <arseny@altlinux.org> 1.2.0.15.git6584602-alt1
- Initial build for ALT Sisyphus.
