%define major_version 1.2
%define minor_version 3
%define shortname 389-ds
%define pkgname   fedora-ds

Name: 389-ds-console
Version: 1.2.6
Release: alt1
Group: Networking/Other
Url: http://port389.org
License: GPLv2
Summary: 389 Directory Server Management Console
BuildArch: noarch
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-%release.tar

BuildRequires(Pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: ant
BuildRequires: ldapsdk
BuildRequires: idm-console-framework
BuildRequires: jss

Provides: fedora-ds-directoryconsole = %version-%release
Obsoletes: fedora-ds-directoryconsole < %version-%release

%description
A Java based remote management console used for managing 389
Directory Server.  The 389 Console is required to load and
run these jar files.

%package          doc
Summary:          Web docs for 389 Directory Server Management Console
Group:            Documentation
Requires:         %name = %version-%release

%description      doc
Web docs for 389 Directory Server Management Console

%prep
%setup -q

%build
%ant -Dconsole.location=%_datadir/java -Dldapjdk.jar.name=ldapsdk.jar -Dconsole.location=%_javadir -Dbuilt.dir=`pwd`/built

%install
install -d %buildroot%_datadir/%pkgname/html/java/
install -m777 built/package/%{shortname}* %buildroot%_datadir/%pkgname/html/java
install -d %buildroot%_datadir/%pkgname/manual/en/slapd/help
install -m644 help/en/*.html %buildroot%_datadir/%pkgname/manual/en/slapd
install -m644 help/en/tokens.map %buildroot%_datadir/%pkgname/manual/en/slapd
install -m644 help/en/help/*.html %buildroot%_datadir/%pkgname/manual/en/slapd/help

# create symlinks
pushd %buildroot%_datadir/%pkgname/html/java
ln -s %shortname-%version.jar %shortname-%major_version.jar
ln -s %shortname-%version.jar %shortname.jar
ln -s %shortname-%{version}_en.jar %shortname-%{major_version}_en.jar
ln -s %shortname-%{version}_en.jar %{shortname}_en.jar
popd

%files
%_datadir/%pkgname/html/java/%shortname-%version.jar
%_datadir/%pkgname/html/java/%shortname-%major_version.jar
%_datadir/%pkgname/html/java/%shortname.jar
%_datadir/%pkgname/html/java/%shortname-%{version}_en.jar
%_datadir/%pkgname/html/java/%shortname-%{major_version}_en.jar
%_datadir/%pkgname/html/java/%{shortname}_en.jar

%files doc
%dir %_datadir/%pkgname/manual/en/slapd
%dir %_datadir/%pkgname/manual/en/slapd/help
%doc %_datadir/%pkgname/manual/en/slapd/tokens.map
%doc %_datadir/%pkgname/manual/en/slapd/*.html
%doc %_datadir/%pkgname/manual/en/slapd/help/*.html

%changelog
* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt1
- merge upstream 1.2.6

* Tue Jul 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt1
- merge upstream 1.2.3

* Sun Oct 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt5
- fix build (buildprereq rpm-build-java)

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt4
- merge upstream 1.2.0
- subpackage with docs

* Thu Jul 02 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt3
- fix wrong major version

* Mon May 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt2
- rename to 389-ds-console

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- Updated to 1.1.1

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Fedora-DS 1.1 Final release
- Resolve bug 379191: Online help: Directory Console (ds-console)
- Resolve bug 386041: "Select control OID(s) to add" dialog shows redundant OIDs at the end

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030
- Resolves bug 308221: Don't try to verify plugin path validity.
- Resolves bug 333171: Deal with illegal input for port field when setting up sync agreement.
- Resolves bug 178247: Removed disabled cachesize field from Database Settings tab.

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Mon Nov 14 2005 Nathan Kinder <nkinder@redhat.com> 1.1.0-1
- Initial creation
