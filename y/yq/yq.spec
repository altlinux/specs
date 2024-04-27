
%define _unpackaged_files_terminate_build 1
%def_enable check

Name:    yq
Version: 3.4.3
Release: alt1
Summary: Command-line YAML, XML and TOML processor
License: Apache-2.0
Group:   Other
URL:     https://github.com/kislyuk/yq

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3(pip) python3(setuptools_scm)
%if_enabled check
BuildRequires: jq
BuildRequires: python3-module-xmltodict >= 0.11.0
BuildRequires: python3-module-tomlkit >= 0.11.6
BuildRequires: python3(argcomplete)
BuildRequires: python3(yaml)
BuildRequires: /proc
%endif

BuildArch: noarch

Source:  %name-%version.tar

Requires: jq
Requires: python3-module-xmltodict >= 0.11.0
Requires: python3-module-tomlkit >= 0.11.6

%description
yq is a command-line YAML, XML and TOML processor.
It is a jq wrapper for YAML, XML and TOML documents.

%prep
%setup -n %name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
%__python3 ./test/test.py -v

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Sat Apr 27 2024 Ivan A. Melnikov <iv@altlinux.org> 3.4.3-alt1
- 3.4.3

* Tue Apr 16 2024 Ivan A. Melnikov <iv@altlinux.org> 3.3.1-alt1
- 3.3.1

* Sun Apr 14 2024 Ivan A. Melnikov <iv@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sun Sep 10 2023 Ivan A. Melnikov <iv@altlinux.org> 3.2.3-alt1
- 3.2.3

* Wed May 03 2023 Ivan A. Melnikov <iv@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Apr 10 2023 Ivan A. Melnikov <iv@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Feb 22 2023 Ivan A. Melnikov <iv@altlinux.org> 3.1.1-alt1
- 3.1.1

* Thu Aug 04 2022 Ivan A. Melnikov <iv@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Jul 18 2022 Ivan A. Melnikov <iv@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Feb 22 2022 Ivan A. Melnikov <iv@altlinux.org> 2.14.0-alt1
- 2.14.0

* Fri Dec 03 2021 Ivan A. Melnikov <iv@altlinux.org> 2.13.0-alt1
- 2.13.0

* Mon Jun 14 2021 Ivan A. Melnikov <iv@altlinux.org> 2.12.2-alt1
- 2.12.2

* Tue Feb 09 2021 Ivan A. Melnikov <iv@altlinux.org> 2.12.0-alt2
- add %%check section

* Tue Feb 09 2021 Ivan A. Melnikov <iv@altlinux.org> 2.12.0-alt1
- 2.12.0

* Mon Sep 07 2020 Ivan A. Melnikov <iv@altlinux.org> 2.11.0-alt1
- 2.11.0

* Tue May 12 2020 Ivan A. Melnikov <iv@altlinux.org> 2.10.1-alt1
- 2.10.1

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
