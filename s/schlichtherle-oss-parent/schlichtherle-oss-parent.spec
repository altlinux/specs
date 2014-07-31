Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		schlichtherle-oss-parent
Version:	9
Release:	alt1_6jpp7
Summary:	Parent Pom for OSS Projects

License:	ASL 2.0
URL:		http://schlichtherle.de

Source0:	http://central.maven.org/maven2/de/schlichtherle/oss-parent/%{version}/oss-parent-%{version}.pom

# set fedora versions, comment out unavailable deps
Patch0:		%{name}-versions.patch

BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	maven-local
BuildRequires:	maven-enforcer-plugin
BuildRequires:	sonatype-oss-parent

Requires:	jpackage-utils
Requires:	maven
Source44: import.info


%description
A parent Project Object Model (POM) for Open
Source Software (OSS) projects, such as truezip.


%prep
cp %{SOURCE0} pom.xml
%patch0


%build
mvn-rpmbuild package


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 9-alt1_6jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 9-alt1_4jpp7
- new version

