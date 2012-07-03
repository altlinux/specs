Version: 1.1
Release: alt2.1
Summary: Simplified object-oriented Python extension module for libpcap
Url: http://code.google.com/p/pypcap/
License: BSD
Group: Development/Python
Packager: Fr. Br. George <george@altlinux.ru>
%setup_python_module pypcap
Name: %packagename
Source: http://pypcap.googlecode.com/files/%modulename-%version.tar.gz

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: libpcap-devel

%description
PyPcapi is simplified object-oriented Python extension module for libpcap - the current tcpdump.org version, the legacy version shipping with some of the BSD operating systems

%prep
%setup -q -n %modulename-%version
sed -i 's/dylib/so/' setup.py
%ifarch x86_64
sed -i "s/'lib'/'lib64'/g" setup.py
%endif

sed -i "s/'include', *//" setup.py

%build
python setup.py config
python setup.py build

%install
python setup.py install --prefix=%prefix --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CHANGES LICENSE README test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Fr. Br. George <george@altlinux.ru> 1.1-alt2
- Fix build

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Sat Jan 10 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from scratch

