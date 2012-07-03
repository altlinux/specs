# -*- coding: utf-8 -*-
Name: python-module-qbzr
Version: 0.22.2
Release: alt1

%setup_python_module qbzr

Summary: A simple Qt cross-platform frontend for some of Bazaar commands
License: gpl2
Group: Development/Python

Url: https://launchpad.net/qbzr
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: rpm-build-licenses

%description
The purpose of this plugin is to provide a graphical user
interface for those Bazaar commands where it can simplify the usage.
Highlighting of differences between files, "browsable" log view, commit
only some files without listing them all on the command line, etc.

QBzr provides a GUI frontend for many core bzr commands and several
universal dialogs and helper commands.  The qbzr equivalents for core
bzr commands have the same names as the CLI commands but with a 'q'
prefix.  See home page for more details.

This module is built for python %__python_version

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/qbzr
%python_sitelibdir/*.egg-info
%doc AUTHORS.txt NEWS.txt README.txt

%changelog
* Thu Apr 19 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.22.2-alt1
- Qt frontend for bazaar 

