Epoch: 1
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name commons-launcher

Name:          apache-%{short_name}
Version:       1.1
Release:       alt3_18.20100521svn936225jpp8
Summary:       A cross platform Java application launcher
License:       ASL 2.0
URL:           http://commons.apache.org/launcher/

# The last release of this package was many years ago and in that time there
# have only been two extremely minor changes to the source code, [1] and [2].
# It seems a new release is unlikely to be forthcoming in the near future.
# 
# [1] - http://svn.apache.org/viewvc/commons/proper/launcher/trunk/src/java/org/apache/commons/launcher/ChildMain.java?r1=138801&r2=138803
# [2] - http://svn.apache.org/viewvc/commons/proper/launcher/trunk/src/java/org/apache/commons/launcher/Launcher.java?r1=138801&r2=138802
# 
# During that time however, support for the maven 2 build system has been
# added. So in order to make my life easier as a maintainer, with regard to
# supporting OSGi manifests and installing poms, etc, I have elected to package
# a maven2 supporting snapshot instead of maintaining patches in our SRPM. As
# an added bonus, the snapshot also has more accurate javadocs.
# 
# How to generate source tarball from source control:
#  $ svn export -r 936225 http://svn.apache.org/repos/asf/commons/proper/launcher/trunk/ commons-launcher-1.1-src
#  $ tar -zcf commons-launcher-1.1-src.tar.gz commons-launcher-1.1-src
Source0:       %{short_name}-%{version}-src.tar.gz

# remove unnecessary build dependency on ant-optional (ant no longer ships this jar)
Patch0:        %{short_name}-pom.patch

BuildArch:     noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
Source44: import.info

%description
Commons-launcher eliminates the need for a batch or shell script to launch a 
Java class. Some situations where elimination of a batch or shell script may 
be desirable are:

* You want to avoid having to determining where certain application paths are
e.g. your application's home directory, etc. Determining this dynamically in 
a Windows batch scripts is very tricky on some versions of Windows or when 
soft links are used on Unix platforms.

* You want to avoid having to handle native file and path separators or native
path quoting issues.

* You need to enforce certain system properties.

* You want to allow users to pass in custom JVM arguments or system properties
without having to parse and reorder arguments in your script. This can be 
tricky and/or messy in batch and shell scripts.

* You want to bootstrap system properties from a configuration file instead 
hard-coding them in your batch and shell scripts.

* You want to provide localized error messages which is very tricky to do in
batch and shell scripts.

%package javadoc
Group: Development/Java
Summary:       API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# apply patches
%patch0 -p0 -b .orig

sed -i 's/\r//' README.txt LICENSE.txt NOTICE.txt
sed -i "s|\<groupId\>ant\<\/groupId\>|<groupId>org.apache.ant</groupId>|g" build.xml

# This class is for working around PATH problems on Windows platforms only but
# prevents building here because OSGi does not permit classes in the default
# package. Remove for now, to appease newer maven-bundle-plugin versions.
rm src/java/LauncherBootstrap.java

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-launcher %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%doc README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt3_18.20100521svn936225jpp8
- unbootstrap build

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_14.20100521svn936225jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_12.20100521svn936225jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_10.20100521svn936225jpp7
- fc update

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.r832060.5jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_4jpp5
- new jpackage release

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_3jpp1.7
- converted from JPackage by jppimport script

* Mon Mar 21 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt3
- rpm-build-java macroces
- cvs 20050321

* Sun Oct 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt2
- 1.1-dev (cvs 20041024)

* Sat Sep 11 2004 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- 1.1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Fri Jan  9 2004 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:0.9-1jpp
- First build for JPackage

* Wed Dec 17 2003 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:0.9-0.2
- Fixed description
- Enabled javadocs

* Thu Dec  4 2003 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:0.9-0.1
- Rebuilt w/o javadocs

