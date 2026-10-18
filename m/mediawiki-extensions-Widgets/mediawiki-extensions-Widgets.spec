%define oname Widgets
%define mwversion 1.46
%define webappdir %webserver_webappsdir/mediawiki
%define commit e67d0bd
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.7.0
Release: alt2

Summary: Widgets extension allows adding widgets to wiki by just creating pages in Widget namespace

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7
BuildRequires(pre): rpm-build-webserver-common

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Widgets extension allows adding widgets
to wiki by just creating pages in Widget namespace.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json,composer.lock,vendor/smarty/smarty/run-tests*.sh}
subst "4i\$wgGroupPermissions['sysop']['editwidgets'] = true;" %buildroot%_mediawiki_settings_dir/50-%oname.php
# the extension directory is read-only for the web server: compile templates in the writable cache
rm -rv %buildroot%mediawiki_ext_dir/compiled_templates
subst "4i\$wgWidgetsCompileDir = '%webappdir/cache/widgets/';" %buildroot%_mediawiki_settings_dir/50-%oname.php
mkdir -p %buildroot%webappdir/cache/widgets

%files -f %oname.files
%attr(2770,root,%webserver_group) %dir %webappdir/cache/widgets/

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt2
- fix "unable to write file" in compiled_templates: set $wgWidgetsCompileDir to the web server writable cache directory, do not ship compiled_templates in the read-only extension directory
- added BuildRequires: rpm-build-webserver-common (webserver_webappsdir and webserver_group macros)
- 1.7.0 fixes the Title class error on MediaWiki 1.46 (closes: #58402)

* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- update to REL1_46 snapshot e67d0bd (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- vendor (smarty 4.5) comes with the snapshot: dropped the predownloaded Source1
- removed vendor smarty test scripts
- dropped BuildRequires: rpm-build-intro (no %%remove_repo_info: the snapshot has no repo info)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sun Jun 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1git
- new version (1.3.0) with rpmgs script
- CVE-2020-9382, CVE-2020-35625

* Sun Oct 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- incorporate smarty

* Sun Oct 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus
