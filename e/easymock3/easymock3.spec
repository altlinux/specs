# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: apache-jar-resource-bundle
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           easymock3
Version:        3.1
Release:        alt2_9jpp7
Summary:        Easy mock objects
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.easymock.org

# svn export https://easymock.svn.sourceforge.net/svnroot/easymock/tags/easymock-3.1 easymock3-3.1
# tar cfJ easymock3-3.1.tar.xz easymock3-3.1
Source0:        %{name}-%{version}.tar.xz

# Fix the artifiact id and object id of cglib, it should be net.sf.cglib:cglib
# instead of cglib:cglib-nodep:
Patch0:         %{name}-fix-cglib-aid-and-gid.patch

# Build the core only (no class extension or OSGi support):
Patch1:         %{name}-build-the-core-only.patch

# Backport upstream fixes for Java 7:
Patch2:         %{name}-backport-of-easymock-101.patch

# Remove tests that fail (please add them again when 3.1.1 is released):
Patch3:         %{name}-remove-failing-tests.patch
Patch4:         %{name}-%{version}-classextension-tests2.patch

BuildArch:      noarch

BuildRequires:  apache-resource-bundles
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  maven
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-timestamp-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  objenesis

Requires:       jpackage-utils
Requires:       objenesis
Source44: import.info


%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch


%description javadoc
Javadoc for %%{name}.


%prep

# Unpack the sources:
%setup -q

# Apply the patches:
%patch0 -p1
# remove some warning caused by unavailable plugin
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin
%pom_xpath_remove pom:profiles easymock-classextension

%pom_disable_module easymock-integration
%patch2 -p1
%patch3 -p1


%build

mvn-rpmbuild \
  -Dmaven.test.failure.ignore \
  -Dproject.build.sourceEncoding=ISO-8859-1 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 easymock/target/easymock-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 easymock-classextension/target/easymockclassextension-%{version}.jar %{buildroot}%{_javadir}/%{name}classextension.jar

# POM files:
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 easymock/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 easymock-classextension/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}classextension.pom

# Javadoc files:
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Dependencies map:
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}classextension.pom %{name}classextension.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc easymock/LICENSE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc easymock/LICENSE.txt


%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_9jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_9jpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_7jpp7
- new fc release

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_6jpp7
- new version

