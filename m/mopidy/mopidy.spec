%define _unpackaged_files_terminate_build 1
%define pypi_name Mopidy
%def_with check 

Name: mopidy
Version: 3.4.2
Release: alt1

Summary: Mopidy is an extensible music server written in Python
License: Apache-2.0
Group: Sound
Url: https://mopidy.com/
VCS: https://github.com/mopidy/mopidy
Source: %name-%version.tar
Patch1: alt-fix-user-via-su.patch
Patch2: alt-fix-path-config.patch

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: gstreamer1.0-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pygobject3
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-requests
BuildRequires: python3-module-responses
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pykka
BuildRequires: python3-module-pytest-cov
BuildRequires: gst-plugins-base1.0
BuildRequires: gst-plugins-good1.0
BuildRequires: gst-plugins-ugly1.0
%endif

Requires: python3-module-dbus
Requires: python3-module-pygobject3

%description
Mopidy plays music from local disk, Spotify, SoundCloud, Google Play Music, and
more. You edit the playlist from any phone, tablet, or computer using a variety
of MPD and web clients.

Out of the box, Mopidy is an HTTP server. If you install the Mopidy-MPD
extension, it becomes an MPD server too. Many additional frontends for
controlling Mopidy are available as extensions.

%description -l ru_RU.UTF-8
Mopidy воспроизводит музыку с локального диска, Spotify, SoundCloud, Google Play
Music и т.д. У вас есть возможность редактировать плейлист с любого телефона,
планшета или компьютера, используя различные MPD и веб-клиентов.

По умолчанию Mopidy представляет собой HTTP-сервер. Если установить Mopidy-MPD,
он также становится сервером MPD. Множество дополнительных интерфейсов для
управление Mopidy доступны в виде расширений.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%pyproject_build

%install
%pyproject_install
install -d %buildroot{%_sysconfdir,%_sharedstatedir/%name,%_logdir/%name}
install -D -p -m 644 mopidy/config/default.conf %buildroot%_sysconfdir/%name.conf
install -D -p -m 644 extra/systemd/mopidy.service %buildroot%_unitdir/%name.service
install -D -p -m 755 extra/mopidyctl/mopidyctl %buildroot%_bindir/mopidyctl
install -D -m 644 extra/mopidyctl/mopidyctl.8 %buildroot%_man8dir/mopidyctl.8

%check
# After updating python3-module-setuptools (04/17/2024), test_help.py stopped working. 
# Should be fixed in Mopidy 4.0 - https://docs.mopidy.com/latest/changelog/#v4-0-0-unreleased.
rm -rf tests/test_help.py
%tox_check_pyproject

%pre
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -g %name -G audio -s /dev/null  \
		-d %_sharedstatedir/%name %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_bindir/mopidyctl
%_man8dir/mopidyctl.8.*
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name.conf
%attr(-,%name,%name) %dir %_sharedstatedir/%name
%attr(-,%name,%name) %dir %_logdir/%name
%attr(-,%name,%name) %_sysconfdir/%name.conf

%doc LICENSE README.rst docs/changelog.rst

%python3_sitelibdir/%name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Wed Feb 07 2024 Anastasia Osmolovskaya <lola@altlinux.org> 3.4.2-alt1
- Initial build for ALT.
