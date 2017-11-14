Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global tzversion tzdata2016c

Name:             joda-time
Version:          2.9.3
Release:          alt1_4.tzdata2016cjpp8
Summary:          Java date and time API

License:          ASL 2.0
URL:              http://www.joda.org/joda-time/
Source0:          https://github.com/JodaOrg/%{name}/archive/v%{version}.tar.gz
Source1:          ftp://ftp.iana.org/tz/releases/%{tzversion}.tar.gz
BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.joda:joda-convert)
Source44: import.info


%description
Joda-Time provides a quality replacement for the Java date and time classes. The
design allows for multiple calendar systems, while still providing a simple API.
The 'default' calendar is the ISO8601 standard which is used by XML. The
Gregorian, Julian, Buddhist, Coptic, Ethiopic and Islamic systems are also
included, and we welcome further additions. Supporting classes include time
zone, duration, format and parsing.


%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt
sed -i 's/\r//' RELEASE-NOTES.txt

# all java binaries must be removed from the sources
find . -name '*.jar' -exec rm -f '{}' \;

# replace internal tzdata
rm -f src/main/java/org/joda/time/tz/src/*
tar -xzf %{SOURCE1} -C src/main/java/org/joda/time/tz/src/

# compat filename
%mvn_file : %{name}

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_4.tzdata2016cjpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_3.tzdata2016cjpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_2.tzdata2016cjpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9.2-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_1.tzdata2015ejpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1.tzdata2013gjpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1.tzdata2013cjpp7
- new release

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

