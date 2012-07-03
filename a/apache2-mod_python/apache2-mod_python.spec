%setup_python_subpackage apache2_mod_python
%define modname mod_python
%define module_name python

%ifarch %ix86
%define parch i686
%else
%define parch %_arch
%endif

%define a2_version 2.2.9-alt10

%define python_bindir %apache2_htdocsdir/%module_name
Name: apache2-mod_python%__python_package_version
Version: 3.3.1
Release: alt2.5.2.1.1

Summary: Python module for Apache2
Group: System/Servers
License: Free
Url: http://www.modpython.org
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %modname-%version.tgz
Source1: python.load
Source2: python.conf
Source3: python.start

BuildPreReq: rpm-build-apache2 >= %a2_version
BuildRequires: flex python-dev python-modules-encodings
BuildRequires: apache2-devel >= %a2_version
BuildRequires: rpm-build-python >= 0.21-alt1
BuildRequires: python-base >= 2.4.4

Requires: python = %__python_version
Requires: apache2 >= %a2_version

Conflicts: mod_python
Provides: mod_python%__python_version

%add_python_req_skip _apache
%add_python_req_skip _psp


%description
mod_python is an Apache2 module that embeds the Python interpreter within the server.
With mod_python you can write web-based applications in Python that will run many
times faster than traditional CGI and will have access to advanced features such as
ability to retain database connections and other data between hits and access to
Apache internals.

%prep
%setup -q -n %modname-%version
sed -i "s/!(b == APR_BRIGADE_SENTINEL(b) ||/!(b == APR_BRIGADE_SENTINEL(bb) ||/g" src/connobject.c

%build
%configure --with-apxs=%apache2_apxs --prefix=%prefix --with-python-bin=%__python
%make OPT="-fPIC $RPM_OPT_FLAGS -DEAPI" dso

%install
install -d -m 755 -- $RPM_BUILD_ROOT%apache2_mods_available
install -d -m 755 -- $RPM_BUILD_ROOT%apache2_mods_start
install -d -m 755 -- $RPM_BUILD_ROOT%apache2_libexecdir
install -d -m 755 -- $RPM_BUILD_ROOT%apache2_htdocsaddondir/%modname

install -p -m 644 -- %SOURCE1 $RPM_BUILD_ROOT%apache2_mods_available/%module_name.load
install -p -m 644 -- %SOURCE2 $RPM_BUILD_ROOT%apache2_mods_available/%module_name.conf
subst 's,@a_libexecdir@,%apache2_libexecdir,g' $RPM_BUILD_ROOT%apache2_mods_available/%module_name.load
subst 's,@python_bindir@,%python_bindir,g' $RPM_BUILD_ROOT%apache2_mods_available/%module_name.conf
install -p -m 644 -- %SOURCE3 $RPM_BUILD_ROOT%apache2_mods_start/100-%module_name.conf

mkdir -p %buildroot{%python_sitelibdir/%modname,%_docdir/%modname-%version/icons,%python_bindir,\
%apache2_cgibindir}

install -c src/%modname.so %buildroot%apache2_libexecdir
install -c dist/build/lib.%{_os}-%{parch}-%{__python_version}/%modname/*.so %buildroot%python_sitelibdir/%modname

for i in `ls lib/python/%modname/*.py`; do
  install -m 0644 $i %buildroot%python_sitelibdir/%modname;
done

# docs
for i in `ls doc-html/*.html doc-html/*.css`; do
  install -m 0644 $i %buildroot%_docdir/%modname-%version;
done
for i in `ls doc-html/icons/*.gif`; do
  install -m 0644 $i %buildroot%_docdir/%modname-%version/icons;
done

ln -s %_docdir/%modname-%version %buildroot%apache2_htdocsaddondir/%modname

### Creating mptest.py
%__cat <<EOF >mptest.py
from mod_python import apache

def handler(req):
    req.send_http_header()
    req.write("Hello World!")
    return apache.OK
EOF

install -m 0644 mptest.py %buildroot%python_bindir/

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To use %modname check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %modname module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi



%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To complete %module_name uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi



%files
%python_sitelibdir/%modname/*
%apache2_libexecdir/%modname.so
%dir %attr(0775,root,%apache2_webmaster) %python_bindir
%attr(0664,root,%apache2_webmaster) %python_bindir/mptest.py*
%config(noreplace) %apache2_mods_available/%module_name.conf
%config            %apache2_mods_available/%module_name.load
%config            %apache2_mods_start/100-%module_name.conf
%apache2_htdocsaddondir/*
%_docdir/%modname-%version

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.1-alt2.5.2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt2.5.2.1
- Rebuilt with python 2.6

* Tue Feb 10 2009 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2.5.2
- put _psp.so into package
- clean spec

* Thu Oct 30 2008 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2.5.1
- fix comments in .load file 

* Wed Oct 29 2008 Alexey Morsov <swi@altlinux.org> 3.3.1-alt2.5
- fix build
  + fix macros
  + apply tip from gentoo (http://bugs.gentoo.org/show_bug.cgi?id=230211)

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 3.3.1-alt2.4.1
- Rebuilt with python-2.5.

* Mon Jan 21 2008 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2.4
- fix package: now own _docdir/modname-version

* Mon Apr 09 2007 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2.3
- fix version requires for apache2

* Wed Apr 04 2007 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2.2
- fix build requires for new python policy

* Mon Apr 02 2007 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2.1
- fix uninstall, config 

* Mon Apr 02 2007 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt2
- Switch to the new Apache2 configuration scheme
- Spec file cleanup

* Tue Mar 06 2007 Alexey Morsov <swi@altlinux.ru> 3.3.1-alt1
- new version (bugfixed, improvements, new features)

* Wed Jan 10 2007 Alexey Morsov <swi@altlinux.ru> 3.2.10-alt2
- make this mod_python conflicts with mod_python for apache1.3
  otherwise not possible to start any apps without patching them
	for s/mod_python/apache2_mod_python/

* Wed Dec 20 2006 Alexey Morsov <swi@altlinux.ru> 3.2.10-alt1.1
- fix spec

* Thu Dec 07 2006 Alexey Morsov <swi@altlinux.ru> 3.2.10-alt1
- Initial build for Sisyphus
- patch for separate apache2-mod_python from mod_python for apache1

