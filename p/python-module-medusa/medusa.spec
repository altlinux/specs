%define version 0.5.4
%define release alt1

%define oname medusa

%setup_python_module medusa

Name: %packagename
Version: %version
Release: %release.1.1.1

Summary: Medusa is a framework for writing asynchronous socket-based servers
License: Python (see LICENSE.txt)
Group: Development/Python
Url: http://www.amk.ca/python/code/medusa.html

Source0: http://www.amk.ca/files/python/%oname-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2007 (-bi)
BuildRequires: python-devel python-modules-compiler

%description
Medusa is a framework for writing asynchronous socket-based servers.

%prep
%setup -q -n %oname-%version

%build
%__python setup.py build

%install
CFLAGS="%optflags" %__python setup.py \
	install --optimize=2 \
	--root=%buildroot \
	--install-data=%_datadir \
	--record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CHANGES.txt INSTALL.txt LICENSE.txt README.txt TODO.txt
%doc demo docs test

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt1.1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.5.4-alt1.1
- Rebuilt with python-2.5.

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 0.5.4-alt1
- build for Sisyphus

