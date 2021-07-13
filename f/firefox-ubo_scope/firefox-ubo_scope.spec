# SPEC file for the uBO-Scope Firefox extension

%define rname	ubo_scope
%define cid	uBO-Scope@raymondhill.net

Name:		%firefox_name-%rname
Version:	0.1.12
Release:	alt1

Summary:	uBO-Scope Firefox extension

License:	%gpl3only
Group:		Networking/WWW
URL:		https://github.com/gorhill/uBO-Scope
#URL:		https://addons.mozilla.org/firefox/addon/ubo-scope/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
uBO-Scope Firefox extension is a tool to measure 3rd-party
exposure score for web sites you visit.

uBO-Scope does not alter network traffic, it only observes it.
For every network request, blocked or allowed, it will extract
the base domain name. If the base domain name of the network
request is different from the base domain name extracted from
the URL of the web page, the network request will be deemed
3rd-party and uBO-Scope will store the pair [3rd-party base
domain name, 1st-party base domain name] in its database,
to be used to compute and show your overall 3rd-party
exposure score of web pages you visit in the future.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.1.12-alt1
- Initial build for ALT Linux Sisyphus
