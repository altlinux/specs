%define  modulename transliterate

Name:    python3-module-%modulename
Version: 1.10.2
Release: alt1

Summary: Bi-directional transliterator for Python
License: GPL-2.0-only or LGPL-2.1-or-later
Group:   Development/Python3
URL:     https://github.com/barseghyanartur/transliterate

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Bi-directional transliterator for Python. Transliterates (unicode) strings
according to the rules specified in the language packs (source script <->
target script).

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Nov 30 2021 Andrey Cherepanov <cas@altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus.
