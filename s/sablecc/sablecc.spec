Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           sablecc
Version:        3.7
Release:        alt1_3jpp8
Summary:        A parser generator written in Java
License:        LGPLv2+
URL:            http://sablecc.org
# https://github.com/SableCC/sablecc
Source0:        http://downloads.sourceforge.net/sablecc/sablecc-3.7.zip
#Source1:        http://repo1.maven.org/maven2/sablecc/sablecc/3.2/sablecc-3.2.pom
Patch0:         sablecc-fsf-addr.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  javapackages-local
Source44: import.info

%description
SableCC is a parser generator which generates object-oriented frameworks for
building compilers, interpreters and other text parsers. SableCC keeps a clean
separation between machine and user code which leads to a shorter development 
cycle.

%prep
%setup -q 
%patch0 -p1
# The ant task has to be unpacked and sanitized prior to the main build. 
tar xzf %{name}-anttask-1.0.1.tar.gz
find -name "*.jar" -delete
find -name "*.class" -delete
rm %{name}-anttask-1.0.1.tar.gz

sed -i "s|lib/%{name}.jar|%{_javadir}/%{name}.jar|" bin/%{name}

%mvn_file %{name}:%{name} %{name}

%build
# Build the ant task and copy *only* that class into the main
# classes directory.  Don't copy everything, because there's a 
# namespace collision that will break the build.
pushd %{name}-anttask-1.0.1
ant 
mkdir -p ../classes/org/sablecc/ant/taskdef/
cp classes/org/sablecc/ant/taskdef/Sablecc.class ../classes/org/sablecc/ant/taskdef/
popd

# the define here prevents ant from redownloading the deleted tarball
ant -Dsablecc-anttask_available=true jar

%install
%mvn_artifact %{name}:%{name}:%{version} lib/%{name}.jar
%mvn_install

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files -f .mfiles
%{_bindir}/%{name}
%doc README.html ChangeLog AUTHORS THANKS
%doc LICENSE COPYING-LESSER
%doc doc/*

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_4jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_3jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_2jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_1jpp5
- converted from JPackage by jppimport script

