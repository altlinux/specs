# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           xml-commons-resolver
Version:        1.2
Release:        alt1_14jpp7
Epoch:          0
Summary:        Resolver subproject of xml-commons
License:        ASL 2.0
URL:            http://xml.apache.org/commons/
Source0:        http://www.apache.org/dist/xml/commons/xml-commons-resolver-%{version}.tar.gz
Source1:        xml-commons-resolver-resolver.sh
Source2:        xml-commons-resolver-xread.sh
Source3:        xml-commons-resolver-xparse.sh
Source4:        %{name}-MANIFEST.MF
Source5:        %{name}-pom.xml
Source6:        %{name}-resolver.1
Source7:        %{name}-xparse.1
Source8:        %{name}-xread.1

Requires:       xml-commons-apis
Requires:       jpackage-utils
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildRequires:  zip
Group:          Development/Java
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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf docs
sed -i 's/\r//' KEYS LICENSE.resolver.txt

%build
sed -i -e 's|call Resolver|call resolver|g' resolver.xml
sed -i -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' resolver.xml
sed -i -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver

ant -f resolver.xml jar javadocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE4} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/resolver.jar META-INF/MANIFEST.MF

# Jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/xml-resolver.jar

# Javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/apidocs/resolver/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/xml-resolver
cp %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/xml-xread
cp %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/xml-xparse

# Man pages
install -d -m 755 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m 644 %{SOURCE6} ${RPM_BUILD_ROOT}%{_mandir}/man1/xml-resolver.1
install -p -m 644 %{SOURCE7} ${RPM_BUILD_ROOT}%{_mandir}/man1/xml-xparse.1
install -p -m 644 %{SOURCE8} ${RPM_BUILD_ROOT}%{_mandir}/man1/xml-xread.1

# Pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc KEYS LICENSE.resolver.txt
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%{_javadir}/*
%{_mandir}/man1/*
%attr(0755,root,root) %{_bindir}/*

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.resolver.txt

%changelog
* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_14jpp7
- xml-commons replacement

