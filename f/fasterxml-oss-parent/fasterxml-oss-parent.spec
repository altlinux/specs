# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          fasterxml-oss-parent
Version:       4
Release:       alt2_1jpp7
Summary:       FasterXML parent pom
Group:         Development/Java
License:       ASL 2.0
URL:           http://fasterxml.com/
# git clone git://github.com/FasterXML/oss-parent.git fasterxml-oss-parent-4
# (cd fasterxml-oss-parent-4/ && git archive --format=tar --prefix=fasterxml-oss-parent-4/ oss-parent-4 | xz > ../fasterxml-oss-parent-4-src-git.tar.xz)
Source0:       %{name}-%{version}-src-git.tar.xz

# remove unavailable extension org.kathrynhuxtable.maven.wagon wagon-gitsite 0.3.1
# fix javadoc configration, remove unavailable com.google.doclava doclava 1.0.3
Patch0:        fasterxml-oss-parent-3-pom.patch

BuildRequires: jpackage-utils

BuildRequires: maven
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin

%build
# nothing to do
%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%check
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE README.creole

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 4-alt2_1jpp7
- fixed maven1 dependency

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt1_1jpp7
- use /var/lock/serial

