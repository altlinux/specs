%define modulename emonoda

Name: emonoda
Version: 1.9.13
Release: alt1

Summary: The set of tools to organize and management of your torrents

Group: File tools
License: GPLv3
Url: http://github.com/mdevaev/rtfetch.git

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mdevaev/emonoda.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Provides: rtfetch
Obsoletes: rtfetch

# manually removed:  ruby ruby-stdlibs
# Automatically added by buildreq on Sun Jul 19 2015
# optimized out: python3 python3-base python3-module-greenlet python3-module-pycparser python3-module-setuptools
BuildRequires: libdb4-devel mailcap python3-module-Cython0.18 python3-module-chardet python3-module-nose python3-module-pycairo python3-module-pygobject3 python3-module-zmq pythonium

# do not require by findreq...
Requires: python3-module-yaml

%description
The set of tools to organize and management of your torrents.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/emdiff
%_bindir/emfetch
%_bindir/emfile
%_bindir/emfind
%_bindir/emload
%_bindir/emrm
%_bindir/emhook-manage-trackers

%python3_sitelibdir/%modulename/
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.13-alt1
- initial build for ALT Linux Sisyphus (formely rtfetch)
