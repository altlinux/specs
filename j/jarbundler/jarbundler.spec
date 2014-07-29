# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: jarbundler	
Version: 2.2.0
Release: alt1_4jpp7
Summary: A feature-rich Ant task which will create a Mac OS X application bundle

Group:	Development/Java
License: ASL 2.0
URL:	http://informagen.com/JarBundler/
Source0: http://informagen.com/JarBundler/dist/jarbundler.tar.gz

BuildRequires:	ant
BuildRequires: jpackage-utils

Requires: ant
Requires: jpackage-utils

BuildArch: noarch
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
Summary: Javadocs for %{name}
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}


find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;



%build
export CLASSPATH=
CLASSPATH=build/lib/%{name}-%{version}.jar:$CLASSPATH
echo $ANT_HOME
export OPT_JAR_LIST=:"ant/%{name}-%{version}"
ant jar javadocs

%install

# jars
install -Dpm 644 %{_builddir}/%{name}-%{version}/build/%{name}-%{version}.jar \
 %{buildroot}/%{_javadir}/ant/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar  %{buildroot}/%{_javadir}/ant/%{name}.jar

mkdir -p %{buildroot}%{_javadir}
cp -a build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p  %{buildroot}/%{_javadocdir}/%{name}
cp -rp %{_builddir}/%{name}-%{version}/javadoc \
 %{buildroot}/%{_javadocdir}/%{name}

mkdir -p  %{buildroot}/%{_sysconfdir}/ant.d
echo "jarbundler" >  %{buildroot}/%{_sysconfdir}/ant.d/jarbundler

%files
%{_javadir}/*
%{_sysconfdir}/ant.d/jarbundler
%doc LICENSE.TXT

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_4jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_3jpp7
- new version

