# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sonatype-oss-parent
Version:        7
Release:        alt1_2jpp7
Summary:        Sonatype OSS Parent

Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/sonatype/oss-parents
# git clone git://github.com/sonatype/oss-parents.git
# (cd ./oss-parents; git archive --prefix %{name}-%{version}/ oss-parent-%{version}) | gzip >%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2

Requires:       jpackage-utils
Requires:       maven-release-plugin
Source44: import.info

%description
Sonatype OSS parent pom used by other sonatype packages

%prep
%setup -q
cp -p %{SOURCE1} LICENSE
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%build
#nothing to do for the pom

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%files
%doc LICENSE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 7-alt1_2jpp7
- fc update

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 7-alt1_1jpp7
- new release

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 6-alt1_3jpp7
- new version

