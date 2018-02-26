Name:		webobjects
Version:	5.4.3
Release:	alt2

Summary:	WebObjects runtime environment scripts
Summary(ru_RU.UTF-8): Среда исполнения web-приложений WebObjects

License:	Distributable
Group:		System/Servers
URL:		http://developer.apple.com/tools/webobjects/
BuildArch: 	noarch
Packager:	Gennady Kushnir <baywind@altlinux.org>

Source:		%{name}-%{version}.tar

Requires:	helloWO = 5.4.3
Requires:	woadaptor >= 5.4
Provides:	wotaskd womonitor

BuildRequires:	rpm-macros-webobjects

%description
This package provides init.d scripts and initial configuration for WebObjects runtime environment.
Environment files itself should be installed by required packages.

WebObjects is a set java frameworks for building complex web-applications.
It gives developers a comprehensive suite of tools and frameworks for quickly 
developing standards-based web services and Java server applications. 
A powerful rapid application development environment, backed by web service,
data access, and page generation capabilities, extends the reach of developers
and reduces the cost of ownership by ensuring flexible, maintainable design.
WebObjects is the ideal way to develop, deploy, and extend powerful web services.

%description -l ru_RU.UTF-8
В этом пакте содержатся скрипты init.d и первоначальная конфигурация среды исполения WebObjects.
Необходимые файлы среды исполнения должны быть установлены с требуемыми пакетами.

%prep
%setup

subst "s,/opt/apple/Local/Library/WebObjects/Logs,%wo_logdir,g" SiteConfig.xml
subst "s,/opt/apple/Local/Library/WebObjects/Configuration,%wo_configdir,g" SiteConfig.xml
subst "s,/opt/apple,%wo_next_root,g" SiteConfig.xml
subst "s,/opt/apple,%wo_next_root,g" wotaskd
subst "s,/opt/apple,%wo_next_root,g" womonitor
subst "s,\$WO_CONFIGDIR,%wo_configdir,g" wotaskd
subst "s,\$WO_CONFIGDIR,%wo_configdir,g" womonitor


%install
install -m755 -pD wotaskd %buildroot%_initdir/wotaskd
install -m755 -pD womonitor %buildroot%_initdir/womonitor
install -m640 -pD SiteConfig.xml %buildroot%wo_configdir/SiteConfig.xml

%post
%post_service wotaskd
%post_service womonitor

%preun
%preun_service wotaskd
%preun_service womonitor

%files
%attr(0640,%wo_user,%wo_group) %config(noreplace) %wo_configdir/SiteConfig.xml
%_initdir/wotaskd
%_initdir/womonitor

%changelog
* Thu Oct 07 2010 Gennady Kushnir <baywind@altlinux.org> 5.4.3-alt2
- removed Vendor tag
* Mon Sep 13 2010 Gennady Kushnir <baywind@altlinux.org> 5.4.3-alt1
- initial build for ALT Linux Sisyphus

