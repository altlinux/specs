Name: iotop
Version: 0.6
Release: alt3

Summary: Top like utility for I/O
License: GPLv2
Group: Monitoring

Url: http://guichaz.free.fr/iotop/
Source: http://guichaz.free.fr/iotop/files/iotop-%version.tar.bz2

# rhbz#1035503
Patch0: iotop-0.6-noendcurses.patch
Patch1: iotop-0.6-python3.patch

# Fix build error with Python 3 caused by itervalues() in setup.py
# http://repo.or.cz/iotop.git/commit/99c8d7cedce81f17b851954d94bfa73787300599
Patch2:	iotop-python3build.patch

# sent upstream, iotop <= 0.6, rhbz#1285088
Patch3: iotop-0.3.2-batchprintutf8.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description
iotop is a Python program with a top like UI used to show of behalf of which
process is the I/O going on.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%python3_build

%install
%python3_install --install-scripts %_sbindir

%files
%_sbindir/iotop
%python3_sitelibdir/*
%_man8dir/*

%changelog
* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 0.6-alt3
- Fixed FTBFS (setuptools 60+).

* Sun Nov 10 2019 Anton Midyukov <antohami@altlinux.org> 0.6-alt2
- rebuild with python3

* Fri Feb 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 0.4.4-alt1
- 0.4.4

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.3-alt1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 0.4.3-alt1
- 0.4.3

* Fri Dec 17 2010 Victor Forsiuk <force@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Jul 01 2010 Victor Forsiuk <force@altlinux.org> 0.4.1-alt1
- 0.4.1

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 0.4-alt1
- 0.4

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.1
- Rebuilt with python 2.6

* Thu Sep 24 2009 Victor Forsyuk <force@altlinux.org> 0.3.2-alt1
- 0.3.2

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.3.1-alt1
- 0.3.1

* Wed Jul 30 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt1
- 0.2.1

* Fri Feb 22 2008 Victor Forsyuk <force@altlinux.org> 0.1-alt1
- Initial build.
