Name:           vim-plugin-nftables
Summary:        NFTables config file support for Vim
# TODO more thorough version from git
Version:        2020
Release:        alt1
License:        MIT
Group:          Editors
URL:            https://github.com/nfnty/vim-nftables

Source:         %name-%version.tar
BuildArch:      noarch

%description
NFTables config file support for Vim

%prep
%setup

%install
mkdir -p %buildroot%_datadir/vim
for i in [a-u]*; do
   cp -a $i %buildroot%_datadir/vim/
done

%files
%doc README.md
%_datadir/vim/*/*

%changelog
* Mon May 20 2024 Fr. Br. George <george@altlinux.org> 2020-alt1
- Initial release for ALT
