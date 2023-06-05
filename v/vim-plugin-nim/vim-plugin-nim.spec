Name:           vim-plugin-nim
Version:        1.1.2
Release:        alt1
Source:         %name-%version.tar
License:        MIT
Summary:        Nim language support for Vim
Group:          Editors
BuildArch:      noarch

%description
This provides Nim language support for Vim:
* Syntax highlighting
* Auto-indent
* Build/jump to errors within Vim
* Project navigation and Jump to Definition

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/vim
for i in [a-z]*; do
   cp -a $i %buildroot%_datadir/vim/
done

%files
%doc README.md
%_datadir/vim/*/*

%changelog
* Mon Jun 05 2023 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Initial build for ALT
