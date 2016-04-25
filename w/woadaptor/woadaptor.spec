Name:		woadaptor
Version:	6.1.4
Release:	alt1

Summary:	WebObjects adaptor for Apache 2.4
Summary(ru_RU.UTF-8): WebObjects-адаптор для Apache 2.4

License:	APPLE PUBLIC SOURCE LICENSE
Group:		System/Servers

URL:		https://github.com/projectwonder/wonder/tree/master/Utilities/Adaptors
#URL:		http://wonder.svn.sourceforge.net/viewvc/wonder/trunk/Wonder/Utilities/Adaptors/
Packager:	Gennady Kushnir <baywind@altlinux.org>

Source0:	%{name}-%{version}.tar
Patch1:		%{name}-%{version}-alt-config.patch

Requires:	%apache2_name-base >= 2.4.7-alt1
Requires:	%apache2_name-mmn = %apache2_mmn
Requires:	%apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires:	%apache2_libapr_name >= %apache2_libapr_evr
Provides:	mod_WebObjects.so

BuildRequires(pre): apache2-devel >= 2.4.7-alt1
BuildRequires:	rpm-macros-webobjects

%description
Apache 2.4 extension module that interacts with WebObjects web-applications and configuration files for one

%description -l ru_RU.UTF-8
Модуль расширения для Apache 2.4 , который позволяет работать с web-приложениями WebObjects

%prep
%setup -a 0
%patch1 -p2

%build
%make

subst "s,LOCAL_LIBRARY_DIR,%wo_localroot/Library,g" Apache2.4/apache.conf
subst "s,modules/,%apache2_moduledir/,g" Apache2.4/apache.conf


%install
install -D -m 644 Apache2.4/mod_WebObjects.so %buildroot%apache2_moduledir/mod_WebObjects.so
install -D -m 644 Apache2.4/apache.conf %buildroot%apache2_extra_available/webobjects.conf
install -d  %buildroot%apache2_extra_start
echo "webobjects=yes" > %buildroot%apache2_extra_start/030-webobjects.conf

# activate module %%ghost config
mkdir -p %buildroot%apache2_extra_enabled
touch %buildroot%apache2_extra_enabled/webobjects.conf


%files
%apache2_moduledir/mod_WebObjects.so
%config(noreplace) %apache2_extra_available/webobjects.conf
%config %apache2_extra_start/030-webobjects.conf
%ghost %apache2_extra_enabled/webobjects.conf

%changelog
* Sat Apr 02 2016 Sergey Alembekov <rt@altlinux.ru> 6.1.4-alt1
- new version
- build with apache2.4

* Sat Feb 09 2013 Aleksey Avdeev <solo@altlinux.ru> 5.4-alt3.1
- rebuild with apache2-2.2.22-alt16 (fix unmets)
- add %%ghost for %%apache2_extra_enabled/*.{load,conf}

* Thu Aug 04 2011 Gennady Kushnir <baywind@altlinux.org> 5.4-alt3
- upstream update 5dfcf454...
- http traffic compression setup in configuration file

* Thu Oct 07 2010 Gennady Kushnir <baywind@altlinux.org> 5.4-alt2
- file %%apache2_extra_start/030-webobjects.conf is written using echo instead of installing source file

* Mon Sep 13 2010 Gennady Kushnir <baywind@altlinux.org> 5.4-alt1
- initial build for ALT Linux Sisyphus

