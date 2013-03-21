# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           forge-parent
Version:        5
Release:        alt1_8jpp7
Summary:        Sonatype Forge Parent Pom

Group:          Development/Java
#Note: The license is confirmed at:
#http://nexus.sonatype.org/mailing-list-dev-archives.html#nabble-ts28522017
License:        ASL 2.0
#svn export http://svn.sonatype.org/forge/tags/forge-parent-5 forge-parent
URL:            http://svn.sonatype.org/forge/tags/forge-parent-5

# tar czf forge-parent-5.tgz forge-parent
Source0:        forge-parent-5.tgz

BuildArch: noarch

BuildRequires: jpackage-utils

Requires: jpackage-utils
Source44: import.info

%description
Sonatype Forge is an open-source community dedicated to the creation of the 
next-generation of development tools and technologies.

%prep
%setup -q -n %{name}

%build
#nothing to do for the pom

%install
rm -rf %{buildroot}/

%add_to_maven_depmap org.sonatype.forge forge-parent %{version} JPP forge-parent

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%files

%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_8jpp7
- fc update

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 5-alt1_7jpp6
- fixed repolib

