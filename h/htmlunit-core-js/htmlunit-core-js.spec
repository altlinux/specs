Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           htmlunit-core-js
Version:        2.9
Release:        alt2_3jpp7
Summary:        Rhino fork for htmlunit

Group:          Development/Java
License:        MPLv1.1
URL:            http://htmlunit.sourceforge.net/
# svn export http://htmlunit.svn.sourceforge.net/svnroot/htmlunit/tags/core-js-2.9 htmlunit-core-js-2.9
# tar caf ~/rpmbuild/htmlunit-core-js-2.9.tar.xz htmlunit-core-js-2.9
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-%{version}-build-fix.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  junit4
BuildRequires:  ant

Requires:       jpackage-utils
Source44: import.info

%description
This is a fork of Rhino to support HtmlUnit.
Everyone hopes it will go away someday.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p0
find . -regex '.*\.\(class\|jar\|zip\)' -exec rm -f '{}' \;

%build
ant -DupdateRhinoOriginal.skip=true jar-all

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar
%doc LICENSE.txt README.txt release.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt1_3jpp7
- new release

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_3jpp6
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_2jpp6
- new version

