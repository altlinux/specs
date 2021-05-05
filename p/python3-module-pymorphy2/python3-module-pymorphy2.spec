%define  modulename pymorphy2

Name:    python3-module-%modulename
Version: 0.9.1
Release: alt1

Summary: Morphological analyzer/inflection engine for Russian and Ukrainian languages
License: MIT
Group:   Development/Python3
URL:     https://github.com/kmike/pymorphy2

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Morphological analyzer (POS tagger + inflection engine) for Russian and
Ukrainian languages.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/pymorphy
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 05 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus.
