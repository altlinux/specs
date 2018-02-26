%_python_set_noarch

Name: charm
Summary: A LiveJournal, Atom, and MetaWeb API client for Python
Version: 1.9.1
Release: alt2.1
License: GPLv2
Group: Networking/Other
Url: http://ljcharm.sourceforge.net/

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar

# Automatically added by buildreq on Fri Apr 08 2011 (-bb)
# optimized out: python-base python-modules
BuildRequires: python-devel

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/charm
%python_sitelibdir/charm-1.9.1-*.egg-info
%python_sitelibdir/ljcharm.py
%python_sitelibdir/ljcharm.pyc
%python_sitelibdir/ljcharm.pyo
%_docdir/charm
%_man1dir/charm.1.*
%_man5dir/charmrc.5.*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.1-alt2.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Denis Smirnov <mithraen@altlinux.ru> 1.9.1-alt2
- Use hashlib instead of deprecated md5 and sha modules
  patch by binarymutant (at) gmail.com

* Fri Apr 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.9.1-alt1
- initial build for ALT Linux Sisyphus
