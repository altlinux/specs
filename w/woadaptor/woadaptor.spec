Name:		woadaptor
Version:	5.4
Release:	alt3

Summary:	WebObjects adaptor for Apache 2.2
Summary(ru_RU.UTF-8): WebObjects-адаптор для Apache 2.2

License:	APPLE PUBLIC SOURCE LICENSE
Group:		System/Servers

URL:		https://github.com/projectwonder/wonder/tree/master/Utilities/Adaptors
#URL:		http://wonder.svn.sourceforge.net/viewvc/wonder/trunk/Wonder/Utilities/Adaptors/
Packager:	Gennady Kushnir <baywind@altlinux.org>

Source0:	%{name}-%{version}.tar
Patch1:		%{name}-%{version}-alt-config.patch

Requires:	apache2-common >= 2.2.0
Requires(post):	apache2-common
Provides:	mod_WebObjects.so

BuildRequires:	apache2-devel rpm-macros-webobjects

%description
Apache 2.2 extension module that interacts with WebObjects web-applications and configuration files for one

%description -l ru_RU.UTF-8
Модуль расширения для Apache 2.2 , который позволяет работать с web-приложениями WebObjects

%prep
%setup -a 0
%patch1 -p2

%build
%make_build

subst "s,LOCAL_LIBRARY_DIR,%wo_localroot/Library,g" Apache2.2/apache.conf
subst "s,modules/,%apache2_moduledir/,g" Apache2.2/apache.conf


%install
install -D -m 644 Apache2.2/mod_WebObjects.so %buildroot%apache2_moduledir/mod_WebObjects.so
install -D -m 644 Apache2.2/apache.conf %buildroot%apache2_extra_available/webobjects.conf
install -d  %buildroot%apache2_extra_start
echo "webobjects=yes" > %buildroot%apache2_extra_start/030-webobjects.conf
#activate module config
#mkdir -p %buildroot%apache2_extra_enabled
#ln -sf ../extra-available/webobjects.conf %buildroot%apache2_extra_enabled/webobjects.conf


%post
%_sbindir/a2chkconfig >/dev/null
/sbin/service %apache2_dname condreload ||:

%postun
%_sbindir/a2chkconfig >/dev/null
/sbin/service %apache2_dname condreload ||:

%files
%apache2_moduledir/mod_WebObjects.so
%config(noreplace) %apache2_extra_available/webobjects.conf
%config %apache2_extra_start/030-webobjects.conf
#%config(noreplace,missingok) %apache2_extra_enabled/webobjects.conf

%changelog
* Thu Aug 04 2011 Gennady Kushnir <baywind@altlinux.org> 5.4-alt3
- upstream update 5dfcf454...
- http traffic compression setup in configuration file
* Thu Oct 07 2010 Gennady Kushnir <baywind@altlinux.org> 5.4-alt2
- file %%apache2_extra_start/030-webobjects.conf is written using echo instead of installing source file
* Mon Sep 13 2010 Gennady Kushnir <baywind@altlinux.org> 5.4-alt1
- initial build for ALT Linux Sisyphus

