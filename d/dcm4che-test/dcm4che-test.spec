Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# use dcm4che-test as name, no use carrying the version in the name
%global svn_rev 15516

Name:           dcm4che-test
Version:        2.6
Release:        alt3_0.5.20110530svn15516jpp7
Summary:        Test images for dcm4che2

License:        MPLv1.1 or GPLv2 or LGPLv2
URL:            http://www.dcm4che.org/confluence/display/proj/The+Project
BuildArch:      noarch

# Generated from an svn checkout: TODO: use svn export next time
# svn export https://dcm4che.svn.sourceforge.net/svnroot/dcm4che/dcm4che2-test/tags/dcm4che2-test-2.6
# tar -cvzf dcm4che2-test-2.6.tar.gz dcm4che2-test-2.6/
Source0:        dcm4che2-test-%{version}.tar.gz

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin

Requires:       jpackage-utils

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Source44: import.info

%description
DCM4CHE Test Data and Libraries

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n dcm4che2-test-2.6

%build
mvn-rpmbuild -X install javadoc:aggregate 

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p  %{name}-image/target/%{name}-image-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-image.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

install -pm 644 %{name}-image/pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-image.pom

# note that the artifact id is %%{name}-image, not dcm4che2-test-image
%add_to_maven_depmap org.dcm4che.test %{name}-image %{version} JPP %{name}-image

# Check on this: there is no jar for the -test pom, do we need a add_to_maven_depmap here?
%add_to_maven_depmap org.dcm4che.test dcm4che2-test %{version} JPP %{name}

find $RPM_BUILD_ROOT%{_javadocdir}/%{name} -name "javadoc.sh" -exec chmod a-x '{}' \;

%files
%{_mavenpomdir}/*.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}-image.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.5.20110530svn15516jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.3.20110530svn15516jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_0.3.20110530svn15516jpp7
- new fc release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_0.3.20110530svn15516jpp7
- new version

