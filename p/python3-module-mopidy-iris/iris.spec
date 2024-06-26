%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-mopidy-iris
Version: 3.69.3
Release: alt1

Summary: Fully-featured Mopidy frontend client
License: Apache-2.0
Group: Sound
Url: https://mopidy.com/ext/iris/
VCS: https://github.com/jaedb/iris
Source: %name-%version.tar
Source1: node_modules.tar
Patch1: alt-fix-removing-spotify-from-handlers-test.patch

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: npm

%if_with check
BuildRequires: mopidy
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pytest-asyncio
%endif

Requires: mopidy

%description
Iris is an web-extension for the Mopidy music server. With support for Spotify,
LastFM, Genius, Snapcast and many other extensions, Iris brings all your music
into one user-friendly and unified web-based interface that works beautifully,
no matter your device.

%description -l ru_RU.UTF-8
Iris — это веб-расширение для музыкального сервера Mopidy. Благодаря поддержке
Spotify, LastFM, Snapcast и других расширений, Iris переносит всю вашу музыку
в один удобный и унифицированный веб-интерфейс, который прекрасно работает,
независимо от вашего устройства.

%prep
# prepare web
# npm install --openssl-legacy-provider
# git add -f node_modules
# git commit -m "Updated node modules"
%setup -a 1
%patch1 -p1

%build
npm run prod
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest __tests__

%files
%python3_sitelibdir/mopidy_iris
%python3_sitelibdir/Mopidy_Iris-%version.dist-info

%doc README.rst LICENSE

%changelog
* Mon Apr 01 2024 Anastasia Osmolovskaya <lola@altlinux.org> 3.69.3-alt1
- Initial build for ALT.
