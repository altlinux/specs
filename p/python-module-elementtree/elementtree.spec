%define rver 20050316
%define version 1.2.6
%define release alt0.%rver.1
%setup_python_module elementtree
Summary: ElementTree - a light-weight XML object model for Python.
Name: %packagename
Version: %version
Release: %release.1.1.1
URL: http://effbot.org/zone/element-index.htm
Source: %modulename-%version-%rver.tar.gz
Patch1: %modulename-TidyHTMLTreeBuilder-fix.patch
Copyright: Python (MIT style)
Group: Development/Python
BuildArch: noarch
Packager: Konstantin Klimchev <koka@altlinux.ru>

%description
The Element type is a flexible container object, designed to store
hierarchical data structures in memory.  Element structures can be
converted to and from XML.

%prep
%setup -q -n %modulename-%version-%rver
%patch1 -p1
%build
env CFLAGS="$RPM_OPT_FLAGS" %__python setup.py build

%install
%__python setup.py install \
        --root=%buildroot \
        --optimize=2 \
        --record=INSTALLED_FILES
%clean

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs samples CHANGES README benchmark.py selftest.py

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt0.20050316.1.1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt0.20050316.1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.2.6-alt0.20050316.1.1
- Rebuilt with python-2.5.

* Fri May  6 2005 Konstantin Klimchev <koka@altlinux.ru> 1.2.6-alt0.20050316.1
- new 1.2.6-20050316
- python2.4

* Wed Dec 22 2004 Konstantin Klimchev <koka@altlinux.ru> 1.2.3-alt0.20041205.1
- initial build for Sisyphus
