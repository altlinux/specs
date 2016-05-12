%define major_version 1.1
%define minor_version 16

Name:    389-console
Version: %major_version.%minor_version
Release: alt1
Summary: Fedora Management Console

Group:   Networking/Other
License: LGPL
Url:     http://port389.org
# VCS:	 https://git.fedorahosted.org/git/389/console.git
BuildArch: noarch
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-%release.tar
Requires: idm-console-framework

BuildRequires(Pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: ant
BuildRequires: ldapsdk
BuildRequires: jss
BuildRequires: idm-console-framework

Requires: which

Provides: fedora-idm-console = %version-%release
Obsoletes: fedora-idm-console < %version-%release

%description
A Java based remote management console used for Managing Fedora
Administration Server and Fedora Directory Server.

%prep
%setup -q

%build
%ant -Dlib.dir=%_libdir -Dbuilt.dir=`pwd`/built -Dldapjdk.jar.name=ldapsdk.jar \
     -Djss.local.location=%_javadir -Dman.dir=`pwd`/built%_mandir

%install
install -d %buildroot%_javadir
install -m644 built/*.jar %buildroot%_javadir
install -d %buildroot%_bindir
install -m755 built/%name %buildroot%_bindir
install -d %buildroot%_man8dir
install -m644 built/%_man8dir/* %buildroot%_man8dir

# create symlinks
pushd %buildroot%_javadir
ln -s %{name}_en.jar %name-%{version}_en.jar
ln -s %{name}_en.jar %name-%{major_version}_en.jar
popd

%files
%_javadir/%name-%{version}_en.jar
%_javadir/%name-%{major_version}_en.jar
%_javadir/%{name}_en.jar
%_bindir/%name
%_man8dir/*

%changelog
* Thu May 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.16-alt1
- New version

* Tue Nov 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.15-alt1
- New version

* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt1
- merge upstream 1.1.7

* Tue Jul 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.6-alt1
- merge upstream 1.1.6

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt4
- merge upstream 1.1.3

* Mon Jun 01 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt3
- fix dependencies

* Mon May 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt2
- rename to 389

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- Updated to 1.1.1

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Fedora-DS 1.1 Final release
- Resolve bug 393461: Move documentation home link to theme package.

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030
- Resolves bug 183962: Remove -ms and -mx options from console start script.

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Mon Aug 06 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20070806
- Initial for Sisyphus, separated from Fedora-DS-Console

* Wed Aug  1 2007 Nathan Kinder <nkinder@redhat.com> 1.1.0-3
- Separated theme package.

* Fri Jul 27 2007 Nathan Kinder <nkinder@redhat.com> 1.1.0-2
- Modified package name to be less generic.

* Mon Jul 26 2007 Nathan Kinder <nkinder@redhat.com> 1.1.0-1
- Initial creation
