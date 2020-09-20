%define oname pybugz
%define bash_completion /etc/bash_completion.d/

Name: python3-module-%oname
Version: 0.13
Release: alt1

Summary: PyBugz - Python Interface to Bugzilla

License: GPL
Group: System/Libraries
Url: https://github.com/williamh/pybugz

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: https://github.com/williamh/pybugz/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3

Conflicts: python-module-%oname

%description
PyBugz is a python and command line interface to Bugzilla.

Bugzilla has a very inefficient user interface, so I've written a
command line utility to interact with it. This is mainly done to help
me with closing bugs on Gentoo Bugzilla by grabbing patches, ebuilds
and so on.

%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%bash_completion/
install -m644 contrib/bash-completion %buildroot%bash_completion/

%files
%doc README
%_bindir/bugz
%_man1dir/*
%_man5dir/*
%_datadir/pybugz.d/
%bash_completion/*
%python3_sitelibdir/bugz/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- new version (0.13) with rpmgs script
- build from release tarball
- add conflicts to python-module-pybugz (ALT bug 36918)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.11.1-alt1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt1
- initial build python3 version 0.11.1 (ALT bug #31355)
