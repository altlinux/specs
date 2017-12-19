%setup_python_subpackage apache2_mod_wsgi
%define modname mod_wsgi
%define module_name wsgi

%define a2_version 2.2.4-alt15

%define python_bindir %apache2_htdocsdir/%module_name
Name: apache2-mod_wsgi
Version: 4.5.24
Release: alt1

Summary: Python WSGI module for Apache2
Group: System/Servers
License: Free
Url: http://www.modwsgi.org
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %modname-%version.tar
Source1: wsgi.load
Source3: wsgi.start

BuildRequires: flex python-devel python-modules-encodings
BuildRequires: apache2-devel >= %a2_version
BuildRequires: rpm-build-python >= 0.21-alt1
BuildRequires: python-base >= 2.4.4

Requires: python >= %__python_version
Requires: apache2 >= %a2_version

Provides: mod_wsgi%__python_version

%add_python_req_skip _apache
%add_python_req_skip _psp


%description
mod_wsgi implement a simple to use Apache module which can host any 
Python application which supports the Python WSGI interface. The module 
would be suitable for use in hosting high performance production web 
sites.

%prep
%setup -q -n %modname-%version

%build
%configure --with-apxs=%apache2_apxs --with-python-bin=%__python
%make OPT="-fPIC $RPM_OPT_FLAGS -DEAPI" 

%install
%makeinstall_std
install -d -m 755 $RPM_BUILD_ROOT{%apache2_mods_available,%apache2_mods_start}
install -p -m 644 -- %SOURCE1 $RPM_BUILD_ROOT%apache2_mods_available/%module_name.load
subst 's,@a_libexecdir@,%apache2_libexecdir,g' $RPM_BUILD_ROOT%apache2_mods_available/%module_name.load
install -p -m 644 -- %SOURCE3 $RPM_BUILD_ROOT%apache2_mods_start/100-%module_name.conf


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
%doc *.rst LICENSE
%apache2_libexecdir/%modname.so
%config            %apache2_mods_available/%module_name.load
%config            %apache2_mods_start/100-%module_name.conf

%changelog
* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.24-alt1
- New version.

* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.23-alt1
- New version.

* Sun Nov 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.22-alt1
- New version.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.21-alt1
- New version.

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.20-alt1
- New version

* Sun Oct 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.19-alt1
- New version

* Thu Aug 31 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.18-alt1
- New version

* Sun Jul 09 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.17-alt1
- New version

* Tue Mar 14 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.15-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.14-alt1
- new version 4.5.14

* Fri Jan 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.5.13-alt1
- new version 4.5.13

* Mon Dec 19 2016 Andrey Cherepanov <cas@altlinux.org> 4.5.11-alt1
- new version 4.5.11

* Wed Apr 06 2016 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt1
- New version

* Tue Apr 05 2016 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1.2
- Rebuild with new apache2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3-alt1.1
- Rebuild with Python-2.7

* Fri Nov 26 2010 Michael A. Kangin <prividen@altlinux.org> 3.3-alt1
- new version

* Sun Dec 20 2009 Alexey Morsov <swi@altlinux.ru> 3.1-alt1
- new version

* Sat Nov 28 2009 Alexey Morsov <swi@altlinux.ru> 2.8-alt1
- new version

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Wed Sep 09 2009 Alexey Morsov <swi@altlinux.ru> 2.5-alt1
- new version

* Thu Sep 04 2008 Alexey Morsov <swi@altlinux.ru> 2.3-alt1
- initial build



