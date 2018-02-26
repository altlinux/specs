Name: vim-plugin-spec_alt-ftplugin
Version: 0.1
Release: alt2

Summary: Vim plugin for easy ALT RPM spec editing
Group: Editors
License: GPL

Url: http://lists.altlinux.org/pipermail/devel/2003-June/094044.html
Source: %name-%version.tar
Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: rpm-build-vim
BuildArch: noarch

%description
This is an alternative spec file handling plugin which makes
maintaining %%changelog easier; it was written by Anton V. Denisov
instead of calling add_changelog by hand each time.

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a ftplugin %buildroot%vim_runtime_dir

%files 
%vim_ftplugin_dir/*

%changelog
* Fri Apr 10 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- fixed Summary, thx ktirf@

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial package (only five years passed)
- based on /people/wrar/packages/vim-plugin-html-ftplugin.git

