# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           plexus-cipher
Version:        1.5
Release:        alt1_11jpp7
Summary:        Plexus Cipher: encryption/decryption Component

Group:          Development/Java
License:        ASL 2.0
URL:            http://spice.sonatype.org
#svn export http://svn.sonatype.org/spice/tags/plexus-cipher-1.5
#tar zcf plexus-cipher-1.5.tar.gz plexus-cipher-1.5
Source0:        %{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-migration-to-component-metadata.patch
Patch1:         0001-Improve-randomness-of-PBECipher-salt.patch

BuildArch: noarch

BuildRequires: maven1
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: plexus-container-default
BuildRequires: forge-parent
BuildRequires: spice-parent
BuildRequires: plexus-containers-component-metadata
BuildRequires: junit
BuildRequires: maven-shared-reporting-impl
BuildRequires: plexus-digest

Requires: plexus-containers
Requires: jpackage-utils
Source44: import.info


%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %%{name}.


%prep
%setup -q

%patch0 -p1
%patch1 -p1

cp %{SOURCE1} .

%build
mvn-rpmbuild -Dmaven.test.failure.ignore=true \
             install javadoc:aggregate

%install
# jars
install -Dm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/plexus/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.plexus-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/plexus/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/plexus/%{name}/

%add_maven_depmap JPP.plexus-%{name}.pom plexus/%{name}.jar

%files
%doc LICENSE-2.0.txt NOTICE.txt
%{_javadir}/plexus/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE-2.0.txt NOTICE.txt
%{_javadocdir}/plexus/%{name}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_8jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

