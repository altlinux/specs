Name:    ansible-vim
Version: 2.1
Release: alt1

Summary: A vim plugin for syntax highlighting Ansible's common filetypes
License: MIT
Group:   Other
Url:     https://github.com/pearofducks/ansible-vim

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-vim

%description
This is a vim syntax plugin for Ansible 2.x, it supports YAML playbooks, Jinja2
templates, and Ansible's hosts files.

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a ftdetect ftplugin indent syntax %buildroot%vim_runtime_dir

%files
%doc *.md
%vim_runtime_dir/*/ansible.vim
%vim_runtime_dir/*/ansible_hosts.vim
%vim_runtime_dir/syntax/jinja2.vim*

%changelog
* Thu Jul 04 2024 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- Initial build for Sisyphus.
