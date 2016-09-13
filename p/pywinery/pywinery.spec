Name: pywinery
Version: 0.3.2
Release: alt1

Summary: PyWinery is a graphical, easy and simple wine-prefix manager
License: GPLv3
Group: Emulators

Url: https://github.com/ergoithz/pywinery.git
Source: %name-%version.tar
Packager: Konstantin Artyushkin <akv@altlinux.org>

BuildRequires: rpm-build-python python-dev python-module-pygobject3-devel
BuildArch:noarch

%description
PyWinery is a graphical, easy and simple wine-prefix manager which allows
you to launch apps, explore and manage configuration of separate prefixes,
graphically and faster than setting variables on linux shell.

%prep
%setup

%build
pushd branches/0.3
%python_build
popd

%install
pushd branches/0.3
%python_install
popd

%files
%_bindir/%name
%python_sitelibdir/%name-*.egg-info
%python_sitelibdir/%name/*
%_desktopdir/%name.desktop
%_datadir/%name/*

%changelog
* Tue Sep 13 2016 Konstantin Artyushkin <akv@altlinux.org> 0.3.2-alt1
- new version

