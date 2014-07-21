# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           tycho-extras
Version:        0.16.0
Release:        alt1_3jpp7
Summary:        Additional plugins for Tycho

Group:          Development/Java
License:        EPL
URL:            http://eclipse.org/tycho/
Source0:        http://git.eclipse.org/c/tycho/org.eclipse.tycho.extras.git/snapshot/tycho-extras-0.16.x.tar.bz2
# maven-properties-plugin is only needed for tests
Patch0:         %{name}-no-maven-properties-plugin.patch
Patch1:         %{name}-remove-core.patch
Patch2:         %{name}-393686.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  jgit
BuildRequires:  tycho

Requires:       jpackage-utils
Requires:       jgit
Requires:       tycho
Source44: import.info


%description
A small set of plugins that work with Tycho to provide additional functionality
when building projects of an OSGi nature.


%package javadoc
Summary:        Java docs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n tycho-extras-0.16.x
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# To run tests, we need :
# maven-properties-plugin (unclear licensing)
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-main.pom
%add_maven_depmap JPP.%{name}-main.pom -a "org.eclipse.tycho:tycho-extras,org.sonatype.tycho:tycho-extras"

for mod in tycho-{custom-bundle,eclipserun,source-feature,version-bump}-plugin \
           tycho-{buildtimestamp,sourceref}-jgit tycho-p2-extras-plugin \
           pack200/tycho-pack200{{a,b}-plugin,-impl} \
           target-platform-validation-plugin ; do
   echo $mod
   aid=`basename $mod`
   install -pm 644 $mod/pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-$aid.pom
   install -m 644 $mod/target/$aid-%{version}.jar %{buildroot}%{_javadir}/%{name}/$aid.jar
   %add_maven_depmap JPP.%{name}-$aid.pom %{name}/$aid.jar -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"
done

for pommod in pack200; do
   echo $pommod
   aid=`basename $pommod`
   install -pm 644 $pommod/pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-$aid.pom
   %add_maven_depmap JPP.%{name}-$aid.pom -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"
done

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3jpp7
- update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

