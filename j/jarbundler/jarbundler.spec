BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: java-1.8.0-openjdk-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jarbundler	
Version:       2.2.0
Release:       alt5_12jpp8
Summary:       A feature-rich Ant task which will create a Mac OS X application bundle
License:       ASL 2.0
URL:           http://informagen.com/JarBundler/
Source0:       http://informagen.com/JarBundler/dist/%{name}.tar.gz
Source1:       %{name}-template-pom.xml
BuildRequires: ant
BuildRequires: jpackage-utils

Requires:      ant

BuildArch:     noarch
Source44: import.info

%description
How many times has this happened to you? You've written a little 
Java utility, or maybe even a more complex application, and you 
want to create Mac OS X application bundle for easy distribution.

You'd like to be able to do it automatically from your build 
process, but you're forced to go run the Apple Jar Bundler and 
tweak all the settings manually every time you build.

Well no more! JarBundler is a feature-rich Ant task which will 
create a Mac OS X application bundle from a list of Jar files and 
a main class name. You can add an Icon resource, set various Mac 
OS X native look-and-feel bells and whistles, and maintain your 
application bundles as part of your normal build and release 
cycle. It is free software licensed under the GNU General Public 
License.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}


find -name '*.class' -delete
find -name '*.jar' -delete

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

sed -i 's|source="1.4"|source="1.6" target="1.6"|' build.xml
sed -i 's|/Developer/Java/Ant/lib/ant.jar|%{_javadir}/ant.jar|' build.xml
sed -i 's|<javadoc destdir="javadoc" classpath="${ant.jar}">|<javadoc destdir="javadoc" classpath="${ant.jar}:build/${jarbundler.jar}">|' build.xml

# install in _javadir
%mvn_file net.sourceforge.%{name}:%{name} %{name}

%build
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
ant jar javadocs

export JAVA_HOME=/usr/lib/jvm/java
%mvn_artifact pom.xml build/%{name}-%{version}.jar

%install
%mvn_install -J javadoc

# jars
mkdir -p %{buildroot}%{_javadir}/ant
ln -s ../%{name}.jar  %{buildroot}/%{_javadir}/ant/%{name}.jar

mkdir -p  %{buildroot}/%{_sysconfdir}/ant.d
echo "%{name}" >  %{buildroot}/%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%{_javadir}/ant/%{name}.jar
%doc LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%doc LICENSE.TXT

%changelog
* Tue Jun 14 2022 Igor Vlasenko <viy@altlinux.org> 2.2.0-alt5_12jpp8
- xmvn4 support

* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 2.2.0-alt4_12jpp8
- migrated to %%mvn_artifact

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3_12jpp8
- fixed build with new java

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_12jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_4jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_3jpp7
- new version

