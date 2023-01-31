# SPEC file for the WebScrapBook Firefox extension

%define rname	webscrapbook
%define cid	webscrapbook@danny0838.addons.mozilla.org

Name:		%firefox_name-%rname
Version:	1.6.0
Release:	alt1

Summary:	WebScrapBook Firefox extension

License:	%mpl 2.0
Group:		Networking/WWW
URL:		https://github.com/danny0838/webscrapbook
#URL:		https://addons.mozilla.org/firefox/addon/webscrapbook/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
WebScrapBook is a Firefox extension that captures the web page
faithfully with various archive formats and customizable
configurations, for future retrieval, organization, annotation,
and editing. This project inherits from legacy Firefox add-on
ScrapBook X.


# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.6.0-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.2.0-alt1
- New version

* Sun Nov 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.143.0-alt1
- New version

* Wed Nov 17 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.142.0-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.130.1-alt1
- New version

* Tue Jul 20 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.125.1-alt1
- New version

* Mon Jul 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.124.0-alt1
- New version

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.121.1-alt1
- Initial build for ALT Linux Sisyphus
