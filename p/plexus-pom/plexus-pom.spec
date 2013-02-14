# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          plexus-pom
Version:       3.0.1
Release:       alt2_3jpp7
Summary:       Root Plexus Projects pom
Group:         Development/Java
License:       ASL 2.0
URL:           https://github.com/sonatype/%{name}/
# git clone git://github.com/sonatype/plexus-pom.git
# cd plexus-pom
# git archive --format=tar --prefix=plexus-pom-3.0.1/ plexus-3.0.1 | xz >plexus-pom-3.0.1.tar.xz
Source0:       plexus-pom-%{version}.tar.xz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

# remove
# org.codehaus.mojo taglist-maven-plugin 2.4
# org.apache.maven.wagon wagon-webdav-jackrabbit 1.0
Patch0:        plexus-pom-3.0.1-pom.patch
# remove
# maven-site-plugin which require org.codehaus.plexus:plexus-stylus-skin 1.0
Patch1:        plexus-pom-3.0.1-no-site-plugin.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: spice-parent

BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: modello
BuildRequires: plexus-containers-component-metadata

Requires:      maven
Requires:      spice-parent

Requires:      jpackage-utils >= 0:1.7.5
BuildArch:     noarch
Source44: import.info

%description
The Plexus project provides a full software stack for creating and
executing software projects.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
cp -p %{SOURCE1} LICENSE

%build

mvn-rpmbuild install

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.plexus-plexus.pom
%add_maven_depmap JPP.plexus-plexus.pom

%files
%doc LICENSE
%{_mavenpomdir}/JPP.plexus-plexus.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp7
- new version

