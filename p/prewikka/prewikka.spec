Name: prewikka
Version: 1.2.6
Release: alt1.rc2.git20140923
Summary: Graphical front-end analysis console for the Prelude Hybrid IDS Framework
Group: Security/Networking
License: GPLv2+
Url: http://www.prelude-ids.org
# https://prelude-ids.org/git/prewikka.git
Source0: %name-%version.tar.gz
Source1: %name.apache_mod_python
Source2: %name.apache_cgi
Source3: %name.init

BuildArch: noarch

#Requires: python-module-twisted-names python-module-twisted-core

# Automatically added by buildreq on Tue Jan 13 2009
BuildRequires: python-devel python-module-cheetah python-modules-email

%description
Prewikka is a graphical front-end analysis console for the Prelude
Hybrid IDS Framework. Providing numerous features, Prewikka facilitates
the work of users and analysts. It provides alert aggregation and sensor
and hearbeat views, and has user management and configurable filters. It
has access to external tools such as whois and traceroute.

%package standalone
Summary: %name standalone web server
Group: Security/Networking
Requires: %name = %version

%description standalone
This package contains standalone %name web server

%package mod_python
Summary: %name mod_python web frontend
Group: Security/Networking
Requires: %name = %version

%description mod_python
This package contains %name mod_python web frontend

%package cgi
Summary: %name CGI web frontend
Group: Security/Networking
Requires: %name = %version

%description cgi
This package contains %name CGI web frontend

%prep
%setup

find -type f -exec sed -i 's|preludedbold|preludedb|g' '{}' +
find -type f -exec sed -i 's|preludeold|prelude|g' '{}' +

%build
python setup.py config
%python_build -e %_bindir/python%_python_version

%install
%python_install || (PYTHONPATH=$PWD/prewikka python -c "import siteconfig";
	install -m644 prewikka/siteconfig.py* \
		%buildroot%python_sitelibdir/prewikka/)
%python_install

#install -d %buildroot%python_sitelibdir/prewikka
#install -p -m644 build/lib/prewikka/siteconfig.py \
#	%buildroot%python_sitelibdir/prewikka/
mkdir -p %buildroot%_defaultdocdir/%name-%version
mkdir -p %buildroot%_sbindir/
chmod 0644 %buildroot/%_datadir/%name/htdocs/css/style.css
mv %buildroot/%_bindir/%name-httpd %buildroot/%_sbindir/%name-httpd
mkdir -p %buildroot%_sysconfdir/httpd2/conf/addon.d
%__install -m 755 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name-mod_python.conf
%__install -m 755 %SOURCE2 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name-cgi.conf


%__mkdir_p %buildroot%_initdir
%__install -m 755 %SOURCE3 %buildroot%_initdir/%name
%__mkdir_p %buildroot%_sysconfdir/sysconfig
%__cat > %buildroot%_sysconfdir/sysconfig/%name <<EOF
# Additional command line parameters for %name:
#
PORT="8000"
ADDRESS="0.0.0.0"
EOF

%find_lang %name

%files -f %name.lang
%doc AUTHORS README NEWS HACKING.README
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/%name.conf-dist
%_datadir/%name
%python_sitelibdir/%name/
%python_sitelibdir/%{name}*.egg-info

%exclude %_datadir/%name/cgi-bin
%exclude %python_sitelibdir/%name/ModPythonHandler.*

%files cgi
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name-cgi.conf
%_datadir/%name/cgi-bin

%files mod_python
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name-mod_python.conf
%python_sitelibdir/%name/ModPythonHandler.*

%files standalone
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_initdir/%name
%_sbindir/%name-httpd


%changelog
* Thu Sep 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.rc2.git20140923
- Version 1.2.6rc2

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.14-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.1
- Rebuilt with python 2.6

* Mon Jun 30 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.14-alt1
- Build for ALT
