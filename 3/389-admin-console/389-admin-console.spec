%define major_version 1.1
%define minor_version 5

%define shortname 389-admin
%define pkgname fedora-ds

Name: 389-admin-console
Version: 1.1.7
Release: alt1
Group: Networking/Other
Url: http://port389.org
License: GPLv2
Summary: 389 Admin Server Management Console
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-%release.tar

BuildRequires(Pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: ant
BuildRequires: ldapsdk
BuildRequires: idm-console-framework
BuildRequires: jss

Requires: 389-admin

BuildArch: noarch

%description
A Java based remote management console used for Managing 389
Admin Server.  Requires the 389 Console to load and run the
jar files.

%package doc
Summary: Web docs for 389 Admin Server Management Console
Group: Documentation
Requires: %name = %version-%release

%description doc
Web docs for 389 Admin Server Management Console

%prep
%setup -q

%build
%ant -Dconsole.location=%_datadir/java -Dldapjdk.jar.name=ldapsdk.jar -Dconsole.location=%_javadir -Dbuilt.dir=`pwd`/built

%install
install -d %buildroot%_datadir/%pkgname/html/java
install -m777 built/package/%{shortname}* %buildroot%_datadir/%pkgname/html/java
install -d %buildroot%_datadir/%pkgname/manual/en/admin/help
install -m644 help/en/*.html %buildroot%_datadir/%pkgname/manual/en/admin
install -m644 help/en/tokens.map %buildroot%_datadir/%pkgname/manual/en/admin
install -m644 help/en/help/*.html %buildroot%_datadir/%pkgname/manual/en/admin/help

# create symlinks
pushd %buildroot%_datadir/%pkgname/html/java
ln -s %shortname-%version.jar %shortname-%major_version.jar
ln -s %shortname-%version.jar %shortname.jar
ln -s %shortname-%{version}_en.jar %shortname-%{major_version}_en.jar
ln -s %shortname-%{version}_en.jar %{shortname}_en.jar
ln -s %shortname-%version.jar fedora-admin-1.1.jar
ln -s %shortname-%{version}_en.jar fedora-admin-1.1_en.jar
popd

%files
%doc LICENSE
%_datadir/%pkgname/html/java/%shortname-%version.jar
%_datadir/%pkgname/html/java/%shortname-%major_version.jar
%_datadir/%pkgname/html/java/%shortname.jar
%_datadir/%pkgname/html/java/%shortname-%{version}_en.jar
%_datadir/%pkgname/html/java/%shortname-%{major_version}_en.jar
%_datadir/%pkgname/html/java/%{shortname}_en.jar
%_datadir/%pkgname/html/java/fedora-admin-1.1.jar
%_datadir/%pkgname/html/java/fedora-admin-1.1_en.jar

%files doc
%dir %_datadir/%pkgname/manual/en/admin
%dir %_datadir/%pkgname/manual/en/admin/help
%doc %_datadir/%pkgname/manual/en/admin/tokens.map
%doc %_datadir/%pkgname/manual/en/admin/*.html
%doc %_datadir/%pkgname/manual/en/admin/help/*.html

%changelog
* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Tue Jul 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1
- 1.1.4
- subpackage with docs

* Mon May 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt2
- rename to 389-admin-console

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- Updated to 1.1.1

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Fedora-DS 1.1 Final release
- Resolve bug 379211: Online help corrections.
- Resolve bug 400361: can't perform admin tasks after changing password
- Resolve bug 416311: change admin user text field to label
- Resolve bug 400341: unable to reset admin user password

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030 (version change for directoryconsole only)

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Wed May 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt0
- Initial for Sisyphus based on fedora-ds-directoryconsole spec
