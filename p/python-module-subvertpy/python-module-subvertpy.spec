# $Id: python-module-subvertpy.spec 138 2004-03-26 23:17:36Z cray $
# -*- coding: utf-8 -*-
%define modulename subvertpy
Name: python-module-%modulename
Version: 0.8.9
Release: alt1.1

%setup_python_module subvertpy

Summary: Python bindings for the Subversion version control system that are aimed to be complete, fast and feel native to Python programmers.
License: lgpl2.1
Group: Development/Python

Url: http://www.samba.org/~jelmer/subvertpy/
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar.gz
#Prefix: #_prefix

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Jan 14 2004
BuildRequires: libapr1-devel libaprutil1-devel libsubversion-devel

%description
Python bindings for the Subversion version control system that are
aimed to be complete, fast and feel native to Python programmers.

Bindings are provided for the working copy, client, delta, remote
access and repository APIs. A hookable server side implementation
of the custom Subversion protocol (svn_ra) is also provided.

Subvertpy covers more of the APIs than python-svn. It provides a
more "Pythonic" API than python-subversion, which wraps the Subversion
C API pretty much directly. Neither provide a hookable server-side.

This module is built for python %__python_version

%package -n python-module-%modulename-doc
Summary: %modulename documentation and example programs
Group: Development/Python
Requires: python-module-%modulename = %version
%description -n  python-module-%modulename-doc
Python bindings for the Subversion version control system that are
aimed to be complete, fast and feel native to Python programmers.
Install python-module-%modulename-doc if you need API documentation
and examples for this module

%package -n subvertpy-fast-export
Summary: Generate fastexport stream from a Subversion repository
Group: Development/Python
Requires: python-module-%modulename = %version
%description -n  subvertpy-fast-export
Walk through each revision of a local Subversion repository and export it
in a stream that git-fast-import can consume.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install
install -dm0755 %buildroot%_man1dir
install -m0644 man/* %buildroot%_man1dir


%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%doc NEWS TODO AUTHORS INSTALL

%files -n python-module-%modulename-doc
%doc examples

%files -n subvertpy-fast-export
%_bindir/*
%_man1dir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.9-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Oct 30 2011 Anatoly Kitaikin <cetus@altlinux.org> 0.8.9-alt1
- 0.8.9 release

* Mon Oct 24 2011 Anatoly Kitaykin <cetus@altlinux.org> 0.8.8-alt1
- Initial build
