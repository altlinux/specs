%define oname pybugz
%define bash_completion /etc/bash_completion.d/

Name: python-module-%oname
Version: 0.9.0
Release: alt1.rc1.1

Summary: PyBugz - Python Interface to Bugzilla

License: GPL
Group: System/Libraries
Url: http://www.liquidx.net/pybugz/
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar

# Automatically added by buildreq on Wed Jan 13 2010
BuildRequires: python-devel python-module-PyXML python-module-Reportlab python-modules-email

BuildPreReq: rpm-build-python

%setup_python_module pybugz

%description
PyBugz is a python and command line interface to Bugzilla.

It was conceived as a tool to speed up the workflow for Gentoo Linux
developers and contributors when dealing with bugs using Bugzilla. By
avoiding the clunky web interface, the user quickly search, isolate
and contribute to the project very quickly. Developers alike can easily
extract attachments and close bugs all from the comfort of the command
line.

%prep
%setup

%build
%python_build

%install
%python_install
mkdir -p %buildroot%bash_completion/
install -m644 contrib/bash-completion %buildroot%bash_completion/

%files
%doc README
%_bindir/bugz
%bash_completion/*
%python_sitelibdir/bugz/
%python_sitelibdir/*.egg-info

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.rc1.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.rc1
- Version 0.9.0_rc1 (ALT #26158)

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- initial build for ALT Linux Sisyphus
