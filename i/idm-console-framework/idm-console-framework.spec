%define major_version 1.1

Name: idm-console-framework
Version: 1.1.7
Release: alt1
Group: Networking/Other
Url: http://port389.org
License: LGPLv2
Summary:  Identity Management Console Framework
BuildArch: noarch
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar.bz2
Patch: %name-alt-classnames.patch
BuildRequires(Pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: ant
BuildRequires: ldapsdk
BuildRequires: jss

Requires: java
Requires: ldapsdk
Requires: jss

Provides: fedora-ds-conosole = %version-%release
Obsoletes: fedora-ds-conosole < %version-%release

Provides: fedora-ds-conosole-framework = %version-%release
Obsoletes: fedora-ds-conosole-framework < %version-%release

%description
A Java Management Console framework used for remote server management.

%prep
%setup -q
%patch -p1

%build
%ant -Dldapjdk.jar.name=ldapsdk.jar -Djss.local.location=%_javadir -Dlib.dir=%_libdir -Dbuilt.dir=`pwd`/built -Dclassdest=%_javadir

%install
install -d %buildroot%_javadir
install -m777 built/release/jars/idm-console-* %buildroot%_javadir

# create symlinks
pushd %buildroot%_javadir
ln -s idm-console-base-%version.jar idm-console-base-%major_version.jar
ln -s idm-console-base-%version.jar idm-console-base.jar
ln -s idm-console-mcc-%version.jar idm-console-mcc-%major_version.jar
ln -s idm-console-mcc-%version.jar idm-console-mcc.jar
ln -s idm-console-mcc-%{version}_en.jar idm-console-mcc-%{major_version}_en.jar
ln -s idm-console-mcc-%{version}_en.jar idm-console-mcc_en.jar
ln -s idm-console-nmclf-%version.jar idm-console-nmclf-%major_version.jar
ln -s idm-console-nmclf-%version.jar idm-console-nmclf.jar
ln -s idm-console-nmclf-%{version}_en.jar idm-console-nmclf-%{major_version}_en.jar
ln -s idm-console-nmclf-%{version}_en.jar idm-console-nmclf_en.jar
popd

%files
%_javadir/idm-console-base-%version.jar
%_javadir/idm-console-base-%major_version.jar
%_javadir/idm-console-base.jar
%_javadir/idm-console-mcc-%version.jar
%_javadir/idm-console-mcc-%major_version.jar
%_javadir/idm-console-mcc.jar
%_javadir/idm-console-mcc-%{version}_en.jar
%_javadir/idm-console-mcc-%{major_version}_en.jar
%_javadir/idm-console-mcc_en.jar
%_javadir/idm-console-nmclf-%version.jar
%_javadir/idm-console-nmclf-%major_version.jar
%_javadir/idm-console-nmclf.jar
%_javadir/idm-console-nmclf-%{version}_en.jar
%_javadir/idm-console-nmclf-%{major_version}_en.jar
%_javadir/idm-console-nmclf_en.jar

%changelog
* Fri Sep 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Mon May 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt2
- rename

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- Updated to 1.1.1

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Fedora-DS 1.1 Final release
- Resolve bug 379211: Removed unused labels, corrected CRL file label, and added help dialog 
- to LoginDialog class.
- Resolve bug 393461: Move documentation home link to theme package.
- Resolve bug 192022: Admin Server fails to bring up Config DS

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030 (version change for console only)

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Fri Jun 29 2007 Nathan Kinder <nkinder@redhat.com 1.1.0-1
- Updated for 1.1.0 release

* Mon Nov 14 2005 Nathan Kinder <nkinder@redhat.com> 1.0-1
- Initial creation
