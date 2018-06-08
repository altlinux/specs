
Name:    yq
Version: 2.6.0
Release: alt1

Summary: Command-line YAML and XML processor
License: Apache-2.0
Group:   Other
URL:     https://github.com/kislyuk/yq

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %name-%version.tar

Requires: jq
Requires: python-module-xmltodict >= 0.11.0

%description
yq is a command-line YAML/XML processor. It is a jq
wrapper for YAML and XML documents.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
* Fri Jun 08 2018 Ivan A. Melnikov <iv@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus
