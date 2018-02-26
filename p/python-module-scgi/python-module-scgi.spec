%define modulename scgi

Name: python-module-%modulename
Version: 1.13
Release: alt2.1.1

Summary: Python implementation of the server side of the SCGI protocol
License: CNRI OPEN SOURCE LICENSE
Group: Development/Python

Url: http://www.python.ca/scgi

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-apache rpm-macros-apache2
# Automatically added by buildreq on Tue Mar 31 2009
BuildRequires: apache-devel apache2-devel apache2-httpd-worker python-devel

%setup_python_module %modulename
%add_findreq_skiplist %python_sitelibdir/%modulename/quixote_handler.py

%description
The SCGI protocol is a replacement for the Common Gateway Interface
(CGI) protocol. It is a standard for applications to interface with
HTTP servers. It is similar to FastCGI but is designed to be easier to
implement.

%package -n apache-mod_%modulename
Summary: An Apache 1.3 module that implements the client side of the SCGI protocol
Group: System/Servers
Requires: apache

%description -n apache-mod_%modulename
%summary

%package -n apache2-mod_%modulename
Summary: An Apache 2.0 module that implements the client side of the SCGI protocol
Group: System/Servers
Requires: apache2

%description -n apache2-mod_%modulename
%summary

%prep
%setup

%build
%python_build

# build module for apache1
pushd apache1
%apache_apxs -c mod_scgi.c
popd

# build module for apache2
pushd apache2
%apache2_apxs -c mod_scgi.c
popd

%install
%python_install

# install apache modules
install -pD apache1/mod_scgi.so %buildroot%apache_moduledir/mod_scgi.so
install -pD apache2/.libs/mod_scgi.so %buildroot%apache2_moduledir/mod_scgi.so

# apache configs
install -pDm0644 apache.conf %buildroot%apache_modconfdir/mod_scgi.conf
install -pDm0644 apache.conf %buildroot%apache2_mods_available/scgi.load

%post -n apache-mod_%modulename
%_initdir/httpd condrestart >/dev/null

%postun -n apache-mod_%modulename
%_initdir/httpd condrestart >/dev/null

%post -n apache2-mod_%modulename
if [ $1 -eq 1 ]; then
	a2enmod scgi >/dev/null
fi
%_initdir/httpd2 condreload >/dev/null

%postun -n apache2-mod_%modulename
if [ $1 -eq 0 ]; then
	a2dismod scgi
	%_initdir/httpd2 condreload >/dev/null
fi

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%doc doc README.txt LICENSE.txt

%files -n apache-mod_%modulename
%apache_moduledir/*
%config(noreplace) %apache_modconfdir/mod_scgi.conf
%doc apache1/README.txt

%files -n apache2-mod_%modulename
%apache2_moduledir/*
%config(noreplace) %apache2_mods_available/scgi.load
%doc apache2/README.txt

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.13-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.13-alt2.1
- Rebuild with Python-2.7

* Thu May 06 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.13-alt2
- Skip findreq for uixote_handler.py (Closes: #23441)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1.1
- Rebuilt with python 2.6

* Tue Mar 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.13-alt1
- Initial build for Sisyphus

