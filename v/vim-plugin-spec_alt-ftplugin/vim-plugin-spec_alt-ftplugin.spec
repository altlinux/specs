Name: vim-plugin-spec_alt-ftplugin
Version: 0.3
Release: alt1

Summary: Vim plugin for easy ALT RPM spec editing
Group: Editors
License: GPL-2.0-or-later

Url: http://git.altlinux.org/gears/v/vim-plugin-spec_alt-ftplugin.git
Source: %name-%version.tar
Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

BuildPreReq: rpm-build-vim
PreReq: vim-common >= 4:6.3.007-alt1
Requires: describe-specfile

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
* Wed Jan 20 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt1
- Use describe-specfile from gear to parse spec for EVR.
- Added hasher and git as fallback methods to determine packager.
- Added new configuration variables:
  + g:spec_chglog_packager to set packager and skip automatic method;
  + g:spec_chglog_get_specfile_evr_method to parse spec for package EVR:
    - rpm (use rpm --specfile; UNSAFE);
    - gear (use gear's spec parser; default).

* Wed Sep 30 2020 Anton Farygin <rider@altlinux.ru> 0.2-alt1
- hid stderr from rpm with version request to avoid garbage in
  generated changelog

* Thu Mar 29 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- R: rpmspec (closes: #34730)

* Fri Apr 10 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- fixed Summary, thx ktirf@

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial package (only five years passed)
- based on /people/wrar/packages/vim-plugin-html-ftplugin.git
