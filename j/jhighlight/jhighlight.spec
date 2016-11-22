Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jhighlight
Version:        1.0.1
Release:        alt1_5jpp8
Summary:        An embeddable pure Java syntax highlighting library

Group:          Development/Other
License:        LGPLv2+ or CDDL
URL:            http://svn.rifers.org/jhighlight

Source0:        https://github.com/codelibs/jhighlight/archive/jhighlight-%{version}.tar.gz
Patch0:         servlet31.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
JHighlight is an embeddable pure Java syntax highlighting library that supports
Java, Groovy, C++, HTML, XHTML, XML and LZX languages and outputs to XHTML. It
also supports RIFE (http://rifers.org) templates tags and highlights them
clearly so that you can easily identify the difference between your RIFE markup
and the actual marked up source.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%mvn_alias : com.uwyn:

%build
%mvn_build 

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc COPYING
%doc LICENSE_LGPL.txt LICENSE_CDDL.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE_LGPL.txt LICENSE_CDDL.txt
%doc COPYING

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

