%setup_python_subpackage mod_python
Name: mod_python%__python_package_version
Version: 2.7.11
Release: alt6.2.1.1

Summary: Python module for Apache
Group: System/Servers
License: Free
Url: http://www.modpython.org
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %modulename-%version.tgz
Patch: mod_python-dynamic.patch
Patch1: mod_python-alt-python_bin.patch

BuildRequires(pre): rpm-build-python >= 0.21-alt1 apache-devel python-dev >= 2.4

Requires: apache >= %apache_version
PreReq: python >= %__python_version
Requires: python = %__python_version

Provides: mod_python%__python_version

Conflicts: apache2-mod_python

%add_python_req_skip _apache

%define apache_ctl %_sbindir/apachectl

%define apache_libdir %(%apache_apxs -q LIBEXECDIR)
%define apache_modconfdir %apache_confdir/addon-modules
%define apache_moddocdir  %apache_htdocsdir/addon-modules
%define apache_addonconfdir_d %apache_addonconfdir.d
%define python_bindir %apache_htdocsdir/python

%description
mod_python is an Apache module that embeds the Python interpreter within the server.
With mod_python you can write web-based applications in Python that will run many
times faster than traditional CGI and will have access to advanced features such as
ability to retain database connections and other data between hits and access to
Apache internals.

%prep
%setup -q -n %modulename-%version
%patch
%patch1 -p1

%build
%__autoconf
%configure --with-apxs=%apache_apxs --prefix=%prefix --with-python-bin=%__python
%make OPT="-fPIC $RPM_OPT_FLAGS -DEAPI" dso

%install
%__mkdir_p %buildroot{%_libdir/apache,%apache_moduledir,%apache_moddocdir,%apache_addonconfdir_d,\
%python_sitelibdir/%modulename,%_docdir/%modulename-%version/icons,%python_bindir}

%__install -c src/mod_python.so %buildroot%_libdir/apache/

for i in `ls lib/python/mod_python/*.py`; do
  %__install -m 0644 $i %buildroot%python_sitelibdir/%modulename;
done

# docs
for i in `ls doc-html/*.html doc-html/*.css`; do
  %__install -m 0644 $i %buildroot%_docdir/%modulename-%version;
done
for i in `ls doc-html/icons/*.gif`; do
  %__install -m 0644 $i %buildroot%_docdir/%modulename-%version/icons;
done

%__ln_s %_docdir/%modulename-%version %buildroot%apache_moddocdir/%modulename

### Creating %modulename.conf
%__cat <<EOF >%modulename.conf
### %modulename.conf - configuration directives for the Python Apache module.
### See %apache_moddocdir/%modulename/docs/index.html for details.

## To configure Apache to handle files with the specified extension(s)
## as Python applications:

# LoadModule python_module      modules/mod_python.so
# AddHandler python-program .py

# Sample configuration for Python directory

<IfModule mod_python.c>
    <Directory "%python_bindir">
	AddHandler python-program .py .pyc .pyo
	PythonHandler mptest
	PythonDebug on
    </Directory>
</IfModule>
EOF

### Creating mptest.py
%__cat <<EOF >mptest.py
from mod_python import apache

def handler(req):
    req.send_http_header()
    req.write("Hello World!")
    return apache.OK
EOF

%__install -m 0644 %modulename.conf %buildroot%apache_addonconfdir_d
%__install -m 0644 mptest.py %buildroot%python_bindir

%post
[ -x %apache_ctl ] && %apache_ctl update ||:

%postun
[ -x %apache_ctl ] && %apache_ctl update ||:

%files
%python_sitelibdir/%modulename/*
%_libdir/apache/%modulename.so
%dir %attr(0775,root,%apache_webmaster) %python_bindir
%attr(0664,root,%apache_webmaster) %python_bindir/mptest.py*
%config(noreplace) %apache_addonconfdir_d/%modulename.conf
%apache_moddocdir/*
%doc %_docdir/%modulename-%version

%changelog
* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.11-alt6.2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.11-alt6.2.1
- Rebuilt with python 2.6

* Tue May 13 2008 Alexey Morsov <swi@altlinux.ru> 2.7.11-alt6.2
- remove XFree86 from req

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 2.7.11-alt6.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Alexey Morsov <swi@altlinux.ru> 2.7.11-alt6
- fix package (own doc dir.)

* Wed Jan 10 2007 Alexey Morsov <swi@altlinux.ru> 2.7.11-alt5
- add Conflicts to apache2-mod_python

* Fri Dec 08 2006 Alexey Morsov <swi@altlinux.ru> 2.7.11-alt4
- Change Packager to "Alexey Morsov <swi@altlinux.ru>

* Thu Nov 23 2006 Alexey Morsov <swi@altlinux.ru> 2.7.11-alt3
- changed spec for policy compliance
- remove apacheversion macro

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 2.7.11-alt2
- rebuild with python 2.4

* Sun Feb 20 2005 Ivan Fedorov <ns@altlinux.ru> 2.7.11-alt1
- 2.7.11
- changed spec for apache policy compliance

* Sat Feb 12 2005 Alexey Morozov <morozov@altlinux.org> 2.7.10-alt5
- changed spec for policy compliance

* Mon Nov 22 2004 Ivan Fedorov <ns@altlinux.ru> 2.7.10-alt4
- Dynamic linking with python.

* Thu Oct 14 2004 Ivan Fedorov <ns@altlinux.ru> 2.7.10-alt3
- Rebuild with -DEAPI switch for support Apache Extended API.

* Mon Jun 28 2004 Ivan Fedorov <ns@altlinux.ru> 2.7.10-alt2
- Rebuild with new rpm/python macros.

* Sat May 15 2004 Ivan Fedorov <ns@altlinux.ru> 2.7.10-alt1
- First build for Sisyphus.
