%define pypname shazamio

Name: python3-module-shazamio
Version: 0.7.0
Release: alt1

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

%add_python3_path %python3_sitelibdir/%pypname/

%description
Is a FREE asynchronous library from reverse engineered Shazam API written in Python 3.8+ with asyncio and aiohttp. 
Includes all the methods that Shazam has, including searching for a song by file. 

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files 
%doc LICENSE.txt *.md
%python3_sitelibdir/%pypname/
%python3_sitelibdir/%{pyproject_distinfo %pypname}

%changelog
* Thu Jan 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
