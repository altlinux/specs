Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sablecc
Version:        3.2
Release:        alt3_4jpp7
Summary:        A parser generator written in Java
Group:          Development/Java
License:        LGPLv2+
URL:            http://sablecc.org
Source0:        http://downloads.sourceforge.net/sablecc/sablecc-3.2.zip
Patch0:         sablecc-fsf-addr.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  jpackage-utils
Requires:       jpackage-utils
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
find . -regex '.*\(class\|jar\)' -type f -exec rm -f {} \;
rm %{name}-anttask-1.0.1.tar.gz

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
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -m 0644 lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 0755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%doc LICENSE README.html ChangeLog AUTHORS COPYING-LESSER THANKS
%doc doc/*

%changelog
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

