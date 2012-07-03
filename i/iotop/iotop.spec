Name: iotop
Version: 0.4.4
Release: alt1

Summary: Top like utility for I/O
License: GPLv2
Group: Monitoring

Url: http://guichaz.free.fr/iotop/
Source: http://guichaz.free.fr/iotop/files/iotop-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Tue Mar 29 2011
BuildRequires: python-devel

%description
iotop is a Python program with a top like UI used to show of behalf of which
process is the I/O going on.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/iotop
%python_sitelibdir/*
%_man1dir/*

%changelog
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
