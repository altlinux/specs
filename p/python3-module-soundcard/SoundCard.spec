%define nameD soundcard

Name: python3-module-%nameD
Version: 0.4.6
Release: alt1

Summary: A Pure-Python Real-Time Audio Library
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/SoundCard
Vcs: https://github.com/bastibe/SoundCard

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

Patch: pulseaudio-0.4.4-alt-fixes.patch

%description
SoundCard is a library for playing and recording audio without resorting to a 
CPython extension. Instead, it is implemented using the wonderful CFFI and 
the native audio libraries of Linux, Windows and macOS.

%prep
%setup

%patch -p0

%build
%pyproject_build

%install
%pyproject_install


%files
%doc LICENSE README.rst
%python3_sitelibdir/%nameD/
%python3_sitelibdir/%{pyproject_distinfo %nameD}/

%changelog
* Thu Apr 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.4.6-alt1
- 0.4.5 -> 0.4.6

* Tue Sep 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.5-alt1
- 0.4.4 -> 0.4.5

* Thu Jul 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4-alt2
- fixed import error (ALT #55035)

* Wed Jun 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4-alt1
- 0.4.3 -> 0.4.4

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.4.3-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sat Feb 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt2
- rebuild with removed %%add_python3_path

* Fri Jan 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus
