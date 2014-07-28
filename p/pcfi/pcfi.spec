# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit bd245c9

Name:		pcfi
Version:	2010.08.09
Release:	alt2_6.20111103gitbd245c9jpp7
Summary:	PDF Core Font Information

Group:		Publishing
License:	BSD
URL:		https://github.com/jukka/pcfi
Source0:	https://github.com/jukka/pcfi/tarball/%{commit}/jukka-pcfi-%{commit}.tar.gz
Source1:	http://opensource.adobe.com/wiki/display/cmap/License
BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	maven-surefire-provider-junit
Requires:	jpackage-utils
Source44: import.info


%description
Collection of PDF core font information files downloaded from Adobe's
Developer Center and elsewhere. This collection contains font metrics for the
14 PDF core fonts, CMaps for the PDF CJK fonts and the Adobe Glyph List.   The
files are stored inside the com/adobe/pdf/pcfi directory. See the individual
files for exact licensing information.


%prep
%setup -q -n jukka-pcfi-%{commit}
sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp %SOURCE1 .


%build
mvn-rpmbuild install


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc README.txt src/main/resources/META-INF/LICENSE.txt License
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_6.20111103gitbd245c9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_4.20111103gitbd245c9jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt1_4.20111103gitbd245c9jpp7
- new release

