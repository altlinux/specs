%define oname pypubsub

Name: python3-module-pypubsub
Version: 4.0.3
Release: alt1

Summary: Python Publish-Subscribe Package

License: BSD-like
Group: Development/Python3
Url: https://github.com/schollii/pypubsub

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: %__pypi_url %oname
# Source-url: https://github.com/schollii/pypubsub/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
Provides a publish-subscribe API to facilitate event-based or
message-based architecture in a single-process application.
It is pure Python and works on Python 3.3+.
It is centered on the notion of a topic;
senders publish messages of a given topic,
and listeners subscribe to messages of a given topic,
all inside the same process.
The package also supports a variety of advanced features
that facilitate debugging and maintaining topics and messages
in larger desktop- or server-based applications.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst README_WxPython.txt
%python3_sitelibdir/*

%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- initial build for ALT Sisyphus
