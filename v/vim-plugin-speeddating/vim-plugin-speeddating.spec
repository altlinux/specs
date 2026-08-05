Name:           vim-plugin-speeddating
Version:        20151024
Release:        alt1
Group:          Editors
BuildArch:      noarch
Source:         vim-speeddating-%version.tar.gz
VCS:            https://github.com/tpope/vim-speeddating
Summary:        In-/decrease dates the vim way: C-a and C-x
License:        Vim
BuildRequires(pre): rpm-build-vim

%description
In-/decrease dates the vim way: C-a and C-x. Dates and times in the
orgmode format can be in-/decreased if this plugins is installed.

%prep
%setup -n vim-speeddating-%version

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a [a-z]* %buildroot%vim_runtime_dir/

%files
%doc README*
%vim_runtime_dir/*/*

%changelog
* Wed Aug 05 2026 Fr. Br. George <george@altlinux.org> 20151024-alt1
- Initial build for ALT
