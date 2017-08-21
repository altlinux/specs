%define plugname nerdcommenter
%define plugver  2.5.0

Name: vim-plugin-%plugname
Version: %plugver
Release: alt2
Summary: A commenter plugin for the editor Vim
Group: Editors

License: WTFPL
Url: https://github.com/scrooloose/nerdcommenter
Source0: %plugname-%version.tar
Source1: WTFPL
Patch1:  vim-plugin-nerdcommenter-2.5.0-alt-fix-double-space.patch
Patch2:  vim-plugin-nerdcommenter-2.5.0-alt-set-default-NERDSpaceDelims-to-1.patch

BuildRequires(pre): rpm-build-vim

Requires: %_bindir/vim

BuildArch: noarch

%description
Comment functions so powerful -- no comment necessary.

%prep
%setup -n %plugname-%version
%patch1 -p1
%patch2 -p2
cp %SOURCE1 .

%install
mkdir -p %buildroot%vim_runtime_dir
cp -ar doc plugin %buildroot%vim_runtime_dir

%postun
rm %vim_runtime_dir/doc/tags

%files
%doc README.md
%doc WTFPL
%doc %vim_runtime_dir/doc/*
%vim_runtime_dir/plugin/*

%changelog
* Sun Aug 20 2017 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.0-alt2
- add patch fixing double spaces
- add patch for changing default value for NERDSpaceDelims to 1

* Thu Mar 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.0-alt1
- first build for ALT Linux
