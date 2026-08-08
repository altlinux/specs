%define pypi_name miniaudio

Name:    python3-module-%pypi_name
Version: 1.71
Release: alt1

Summary: Python bindings for the miniaudio library and its decoders
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/miniaudio/
VCS:     https://github.com/irmen/pyminiaudio

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-module-setuptools python3-module-cffi

Source: %name-%version.tar

%description
Python bindings for the miniaudio library and its decoders
(mp3, flac, ogg vorbis, wav).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%_bindir/miniaudio-documentation

%files
%doc LICENSE README.md
%python3_sitelibdir/%{pypi_name}.py
%python3_sitelibdir/__pycache__/%{pypi_name}.*
%python3_sitelibdir/_%{pypi_name}*.so
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Sat Aug 08 2026 Sergey Palcheh <minergenon@altlinux.org> 1.71-alt1
- Initial build for Sisyphus
