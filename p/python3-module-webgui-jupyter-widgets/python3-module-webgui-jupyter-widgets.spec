%define  modulename webgui-jupyter-widgets

Name:    python3-module-%modulename
Version: 0.2.9
Release: alt1.1

Summary: Jupyter widgetds library for webgui js visualization library
License: LGPL-2.1
Group:   Development/Python3
URL:     https://github.com/CERBSim/webgui_jupyter_widgets

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-jupyter-packaging

BuildArch: noarch

Source: webgui_jupyter_widgets-%version.tar
Source1: submodules.tar

# Nobody provides it.
%add_python3_req_skip webgui_jupyter_widgets.example
%description
%summary

%prep
%setup -n webgui_jupyter_widgets-%version -a 1

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/webgui_jupyter_widgets/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.2.9-alt1.1
- NMU: ignored unmet dependency.

* Tue Apr 19 2022 Andrey Cherepanov <cas@altlinux.org> 0.2.9-alt1
- Initial build for Sisyphus.
