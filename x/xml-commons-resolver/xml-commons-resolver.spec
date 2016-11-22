# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
%if %{?fedora} > 19 || 0%{?rhel} > 6
%global headless -headless
%endif

Name:           xml-commons-resolver
Version:        1.2
Release:        alt1_19jpp8
Epoch:          0
Summary:        Resolver subproject of xml-commons
License:        ASL 2.0
URL:            http://xerces.apache.org/xml-commons/components/resolver/
Source0:        http://www.apache.org/dist/xerces/xml-commons/%{name}-%{version}.tar.gz
Source5:        %{name}-pom.xml
Source6:        %{name}-resolver.1
Source7:        %{name}-xparse.1
Source8:        %{name}-xread.1
Patch0:         %{name}-1.2-crosslink.patch
Patch1:         %{name}-1.2-osgi.patch

Requires:       java%{?headless} >= 1.6.0
Requires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires: javapackages-tools rpm-build-java
Group:          Development/Other
BuildArch:      noarch
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
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildRequires:  java-javadoc
Requires:       java-javadoc
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

%build
%ant -f resolver.xml jar javadocs

%install
# Jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/xml-resolver.jar

# Javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/apidocs/resolver/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

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

# Pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf

%files -f .mfiles
%doc KEYS LICENSE.resolver.txt NOTICE-resolver.txt
%{_mavenpomdir}/*
%{_javadir}/*
%{_mandir}/man1/*
%{_bindir}/xml-*
%config(noreplace,missingok) /etc/java/%name.conf

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.resolver.txt NOTICE-resolver.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_19jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_18jpp8
- new version

* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_14jpp7
- xml-commons replacement

