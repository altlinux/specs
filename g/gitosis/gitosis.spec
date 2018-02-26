Name: gitosis
Version: 0.2
Release: alt1.1.1
BuildArch: noarch

Summary: a tool for hosting git repositories
License: GPLv2
Group: System/Servers
Url: git://eagain.net/gitosis.git
Packager: Alexander Myltsev <avm@altlinux.ru>

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

%description
gitosis aims to make hosting git repos easier and safer. It
manages multiple repositories under one user account, using SSH keys
to identify users. End users do not need shell accounts on the server,
they will talk to one shared account that will not let them run
arbitrary commands.


%prep
%setup

%install
%__python setup.py install --root=%buildroot

%files
%_bindir/%name-init
%_bindir/%name-run-hook
%_bindir/%name-serve
%python_sitelibdir/%name
%python_sitelibdir/%name-%version-*.egg-info

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.1
- Rebuilt with python 2.6

* Wed Jun 18 2008 Alexander Myltsev <avm@altlinux.ru> 0.2-alt1
- Initial build for Sisyphus.

