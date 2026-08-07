Name:           vim-plugin-orgmode
# git log -1 --format="%%as" | tr - .
Version:        2026.03.09
Release:        alt1
Group:          Editors
VCS:            https://github.com/jceb/vim-orgmode
License:        AGPL-3.0
Summary:        Text outlining and task management for Vim based on Emacs Org-Mode
Source:         %name-%version.tar
BuildRequires(pre): rpm-build-vim rpm-build-python3
BuildArch:      noarch
Patch:          %name-%version-%release.patch
Requires:       python3-module-orgmode = %EVR
Requires:       vim-plugin-speeddating

%description
Text outlining and task management for Vim based on Emacs Org-Mode.

The idea for this plugin was born by listening to the Floss Weekly
podcast introducing Emacs Org-Mode. Org-Mode has a lot of strong
features like folding, views (sparse tree) and scheduling of tasks.
These are completed by hyperlinks, tags, todo states, priorities aso.

vim-orgmode aims at providing the same functionality for Vim.

%package -n python3-module-orgmode
Group:          Editors
Summary:        Supplemental python module for %name
%add_python3_req_skip vim
%description -n python3-module-orgmode
%summary

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a doc indent syntax ftdetect ftplugin %buildroot%vim_runtime_dir/
mkdir -p %buildroot%python3_sitelibdir_noarch
mv %buildroot%vim_runtime_dir/ftplugin/orgmode %buildroot%python3_sitelibdir_noarch

%files
%doc *.org examples
%vim_runtime_dir/*/*

%files -n python3-module-orgmode
%python3_sitelibdir_noarch/orgmode

%changelog
* Wed Aug 05 2026 Fr. Br. George <george@altlinux.org> 2026.03.09-alt1
- Initial build for ALT
