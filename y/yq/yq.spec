
%define _unpackaged_files_terminate_build 1

Name:    yq
Version: 2.10.0
Release: alt1

Summary: Command-line YAML and XML processor
License: Apache-2.0
Group:   Other
URL:     https://github.com/kislyuk/yq

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildRequires: rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

Requires: jq
Requires: python3-module-xmltodict >= 0.11.0
Requires: python3-module-toml >= 0.9.4

%description
yq is a command-line YAML/XML processor. It is a jq
wrapper for YAML and XML documents.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Dec 23 2019 Ivan A. Melnikov <iv@altlinux.org> 2.10.0-alt1
- 2.10.0
- switch to python3

* Tue Nov 05 2019 Ivan A. Melnikov <iv@altlinux.org> 2.9.2-alt1
- 2.9.2

* Wed Jan 30 2019 Ivan A. Melnikov <iv@altlinux.org> 2.7.2-alt1
- 2.7.2
- require python-module-toml (closes: #36001)

* Fri Oct 12 2018 Ivan A. Melnikov <iv@altlinux.org> 2.7.0-alt1
- 2.7.0

* Fri Jun 08 2018 Ivan A. Melnikov <iv@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus
