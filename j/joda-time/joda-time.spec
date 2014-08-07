BuildRequires: maven-antrun-plugin
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global tzversion tzdata2011f

Name:             joda-time
Version:          1.6.2
Release:          alt4_8.tzdata2011fjpp7
Summary:          Java date and time API

Group:            Development/Java
License:          ASL 2.0
URL:              http://joda-time.sourceforge.net
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Source1:          ftp://elsie.nci.nih.gov/pub/%{tzversion}.tar.gz
# Remove maven toolchanins from pom.xml (not present in fedora yet)
Patch0:           joda-time-remove-toolchains-from-pom.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local

Requires:         jpackage-utils
Source44: import.info

%description
Joda-Time provides a quality replacement for the Java date and time classes. The
design allows for multiple calendar systems, while still providing a simple API.
The 'default' calendar is the ISO8601 standard which is used by XML. The 
Gregorian, Julian, Buddhist, Coptic, Ethiopic and Islamic systems are also 
included, and we welcome further additions. Supporting classes include time 
zone, duration, format and parsing. 


%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' ToDo.txt
%patch0 -p0

# all java binaries must be removed from the sources
find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

# replace internal tzdata
rm -f src/main/java/org/joda/time/tz/src/*
tar -xzf %{SOURCE1} -C src/main/java/org/joda/time/tz/src/


%build
mvn-rpmbuild \
        -e \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc


%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE.txt RELEASE-NOTES.txt ToDo.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_8.tzdata2011fjpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt3_8.tzdata2011fjpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_8.tzdata2011fjpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_8.tzdata2011fjpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt4_2jpp6
- fixed build with moved maven1

* Sun Dec 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_2jpp6
- jpp 6.0 build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_1jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

