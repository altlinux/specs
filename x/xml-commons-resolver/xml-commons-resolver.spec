Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xml-commons-resolver
Epoch:          0
Version:        1.2
Release:        alt1_23jpp8
Summary:        Resolver subproject of xml-commons
License:        ASL 2.0
URL:            http://xerces.apache.org/xml-commons/components/resolver/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/xerces/xml-commons/%{name}-%{version}.tar.gz
Source5:        %{name}-pom.xml
Source6:        %{name}-resolver.1
Source7:        %{name}-xparse.1
Source8:        %{name}-xread.1

Patch0:         %{name}-1.2-crosslink.patch
Patch1:         %{name}-1.2-osgi.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  apache-parent
Source44: import.info
# jpackage deprecations
Conflicts: xml-commons-resolver10 < 0:1.3.05
Conflicts: xml-commons-resolver11 < 0:1.3.05
Conflicts: xml-commons-resolver12 < 0:1.3.05
Obsoletes: xml-commons-resolver10 < 0:1.3.05
Obsoletes: xml-commons-resolver11 < 0:1.3.05
Obsoletes: xml-commons-resolver12 < 0:1.3.05


%description
Resolver subproject of xml-commons.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf docs
sed -i 's/\r//' KEYS LICENSE.resolver.txt NOTICE-resolver.txt

%mvn_file : xml-commons-resolver xml-resolver

%build
%ant -f resolver.xml jar javadocs
%mvn_artifact %{SOURCE5} build/resolver.jar

%install
%mvn_install -J build/apidocs/resolver

# Scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%jpackage_script org.apache.xml.resolver.apps.resolver "" "" %{name} xml-resolver true
%jpackage_script org.apache.xml.resolver.apps.xread "" "" %{name} xml-xread true
%jpackage_script org.apache.xml.resolver.apps.xparse "" "" %{name} xml-xparse true

# Man pages
install -d -m 755 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m 644 %{SOURCE6} ${RPM_BUILD_ROOT}%{_mandir}/man1/xml-resolver.1
install -p -m 644 %{SOURCE7} ${RPM_BUILD_ROOT}%{_mandir}/man1/xml-xparse.1
install -p -m 644 %{SOURCE8} ${RPM_BUILD_ROOT}%{_mandir}/man1/xml-xread.1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf

%files -f .mfiles
%doc KEYS LICENSE.resolver.txt NOTICE-resolver.txt
%{_mandir}/man1/*
%{_bindir}/xml-*
%config(noreplace,missingok) /etc/java/%name.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE.resolver.txt NOTICE-resolver.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_23jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_22jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_19jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_18jpp8
- new version

* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_14jpp7
- xml-commons replacement

