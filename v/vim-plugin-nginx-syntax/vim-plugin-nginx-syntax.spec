Name: vim-plugin-nginx-syntax
Version: 0.3.1
Release: alt2
URL: %vim_script_url 1886

License: The same as vim
Group: Editors
Source: nginx.vim
Source1: ftdetect.vim

BuildArch: noarch
Packager: VIm Plugins Development Team <vim-plugins at packages.altlinux.org>

Summary: Highlights configuration files for nginx, the high-performance web server
Group: Editors

BuildRequires(pre): rpm-build-vim

%description
%summary

%prep

%install
mkdir -p %buildroot{%vim_syntax_dir,%vim_ftdetect_dir}
install -m 644 %SOURCE0 %buildroot%vim_syntax_dir/nginx.vim
install -m 644 %SOURCE1 %buildroot%vim_ftdetect_dir/nginx.vim

%files
%vim_syntax_dir/nginx.vim
%vim_ftdetect_dir/nginx.vim


%changelog
* Sun Sep 05 2010 Michael A. Kangin <prividen@altlinux.org> 0.3.1-alt2
- Fix spec (was not rebuild, thx 2 wrar@)

* Mon Aug 02 2010 Michael A. Kangin <prividen@altlinux.org> 0.3.1-alt1
- Initial build


