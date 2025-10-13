%define  modulename pydub

Name:    python3-module-%modulename
Version: 0.25.1
Release: alt3

Summary: Manipulate audio with a simple and easy high level interface

License: MIT
Group:   Development/Python3
URL:     https://github.com/jiaaro/pydub

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar
Patch: 0d6034778f3a8488ec1b0b40c4f5af131fa9c1c9.patch

%description
%summary

%prep
%setup
%patch -p1

# Hotfix for python3.12
sed -i 's/re\.match(/re\.match(r/g' pydub/utils.py

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Oct 13 2025 Grigory Ustinov <grenka@altlinux.org> 0.25.1-alt3
- Use relative import for pyaudioop fallback (Closes: #56358).

* Sat Jan 25 2025 Grigory Ustinov <grenka@altlinux.org> 0.25.1-alt2
- Fixed regular expressions for python3.12 (Closes: #52814).

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 0.25.1-alt1
- Automatically updated to 0.25.1.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 0.24.1-alt1
- Initial build for Sisyphus.
