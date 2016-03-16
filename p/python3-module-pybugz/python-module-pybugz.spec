%define oname pybugz
%define bash_completion /etc/bash_completion.d/

Name: python3-module-%oname
Version: 0.11.1
Release: alt1.1

Summary: PyBugz - Python Interface to Bugzilla

License: GPL
Group: System/Libraries
Url: https://github.com/williamh/pybugz

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-git: https://github.com/williamh/pybugz
Source: %name-%version.tar

# manually removed: python3-module-zope ruby ruby-stdlibs
# Automatically added by buildreq on Tue Oct 13 2015
# optimized out: python3-base
BuildRequires: python3

BuildPreReq: rpm-build-python3

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
%bash_completion/*
%python3_sitelibdir/bugz/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt1
- initial build python3 version 0.11.1 (ALT bug #31355)
