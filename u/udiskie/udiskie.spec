%define _unpackaged_files_terminate_build 1
%define pypi_name udiskie

%def_with check

Name:    %pypi_name
Version: 2.5.8
Release: alt1

Summary: Automounter for removable media
License: MIT
Group:   Other
URL:     https://github.com/coldfix/udiskie

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%if_with check
BuildRequires: python3-module-pygobject
BuildRequires: python3-module-pyyaml-env-tag
BuildRequires: python3-module-docopt
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Udiskie is a udisks2_ front-end that allows to manage removable media such
as CDs or flash drives from userspace.

%package -n python3-module-%pypi_name
Summary: module for %pypi_name
Group: Development/Python3

%description -n python3-module-%pypi_name
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files -n python3-module-%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files
%doc *.rst COPYING
%_bindir/*
%_datadir/bash-completion/completions/*
%_datadir/locale/de/LC_MESSAGES/udiskie.mo
%_datadir/locale/en_US/LC_MESSAGES/udiskie.mo
%_datadir/locale/es_ES/LC_MESSAGES/udiskie.mo
%_datadir/locale/it_IT/LC_MESSAGES/udiskie.mo
%_datadir/locale/ru_RU/LC_MESSAGES/udiskie.mo
%_datadir/locale/sk_SK/LC_MESSAGES/udiskie.mo
%_datadir/locale/tr_TR/LC_MESSAGES/udiskie.mo
%_datadir/locale/zh_CN/LC_MESSAGES/udiskie.mo
%_datadir/zsh/site-functions/_udiskie
%_datadir/zsh/site-functions/_udiskie-canonical_paths
%_datadir/zsh/site-functions/_udiskie-mount
%_datadir/zsh/site-functions/_udiskie-umount

%changelog
* Tue Aug 26 2025 Artem Semenov <savoptik@altlinux.org> 2.5.8-alt1
- Updated to 2.5.8
- Enabled check

* Tue Jan 28 2025 Artem Semenov <savoptik@altlinux.org> 2.5.7-alt1
- Initial build for Sisyphus
