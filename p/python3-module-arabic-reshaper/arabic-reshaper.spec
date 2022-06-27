%define  modulename arabic-reshaper

Name:    python3-module-%modulename
Version: 2.1.3
Release: alt1

Summary: Python module for formatting Arabic sentences

License: MIT
Group:   Development/Python3
URL:     https://github.com/mpcabd/python-arabic-reshaper

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
A module for reconstructing Arabic sentences that are to be used in
applications that do not support Arabic.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE *.md
%python3_sitelibdir/arabic_reshaper
%python3_sitelibdir/arabic_reshaper-%version-py%_python3_version.egg-info

%changelog
* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus.
