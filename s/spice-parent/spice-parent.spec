BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           spice-parent
Version:        15
Release:        alt1_5jpp7
Summary:        Sonatype Spice Components

Group:          Development/Java
License:        ASL 2.0
URL:            http://svn.sonatype.org/spice/tags/spice-parent-15
#svn export http://svn.sonatype.org/spice/tags/spice-parent-15 spice-parent-15
#tar zcf spice-parent-15.tar.gz spice-parent-15/
Source0:        %{name}-%{version}.tar.gz
Patch0:        pom.patch

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2

Requires:          jpackage-utils
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2
Source44: import.info

%description
Spice components and libraries are common components 
used throughout the Sonatype Forge.

%prep
%setup -q -n %{name}-%{version}
#Remove plexus-javadoc
%patch0

%build
#nothing to do for the pom

%install

%add_to_maven_depmap org.sonatype.spice spice-parent %{version} JPP spice-parent

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

