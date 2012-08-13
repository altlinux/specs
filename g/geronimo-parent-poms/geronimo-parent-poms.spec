BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		geronimo-parent-poms
Version:	1.6
Release:	alt1_7jpp7
Summary:	Parent POM files for geronimo-specs

Group:		Development/Java
License:	ASL 2.0
URL:		http://geronimo.apache.org/

# Following the parent chain all the way up ...
Source0:	http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml

# Remove dependencies from POMs that aren't yet in Fedora
Patch0:		%{name}-parent.patch

BuildRequires:	jpackage-utils

BuildArch:	noarch

# Dependencies and plugins from the POM files
Requires:	maven-compiler-plugin
Requires:	maven-idea-plugin
Requires:	maven-jar-plugin
Requires:	maven-pmd-plugin
Requires:	maven-plugin-bundle

Provides:       geronimo-specs = %{version}-%{release}
Source44: import.info
Conflicts: geronimo-specs < 0:1.2-alt9_16jpp6

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T
cp %SOURCE0 .
%patch0

%build
# Nothing to do ...

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -pm 644 pom.xml \
	$RPM_BUILD_ROOT%{_mavenpomdir}/JPP-geronimo-specs.pom
%add_maven_depmap JPP-geronimo-specs.pom -a 'org.apache.geronimo.specs:specs'

%files
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-geronimo-specs.pom


%changelog
* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

