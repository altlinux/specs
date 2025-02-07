%define pypname shazamio

Name: python3-module-shazamio
Version: 0.8.0
Release: alt1.1

Summary: Is a free asynchronous library from reverse engineered Shazam API written in Python 3.8+ with asyncio and aiohttp.
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/shazamio/
Vcs: https://github.com/shazamio/ShazamIO

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre):  rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-poetry
BuildRequires: python3-module-dataclass-factory

%description
Is a FREE asynchronous library from reverse engineered Shazam API written in Python 3.8+ with asyncio and aiohttp. 
Includes all the methods that Shazam has, including searching for a song by file. 

%prep
%setup

subst "s|from shazamio_core import Recognizer, Signature|from shazamio_core.shazamio_core import Recognizer, Signature|" shazamio/api.py

%build
%pyproject_build

%install
%pyproject_install

%files 
%doc LICENSE.txt *.md
%python3_sitelibdir/%pypname/
%python3_sitelibdir/%{pyproject_distinfo %pypname}

%changelog
* Fri Feb 07 2025 Daniel Zagaynov <kotopesutility@altlinux.org> 0.8.0-alt1.1
- NMU: remove useless %%add_python3_path.

* Wed Feb 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.8.0-alt1
- Update to version 0.8.0

* Tue Feb 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt2
- fixed for new shazamio core v1.1.1

* Thu Jan 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
