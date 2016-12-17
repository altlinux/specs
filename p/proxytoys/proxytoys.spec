Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash 6f4d22725ef28f09bfd5422939b83e1865b5daef
Name:          proxytoys
Version:       1.0
Release:       alt1_8jpp8
Summary:       An implementation neutral API for creation of dynamic proxies
License:       BSD
Url:           http://proxytoys.github.io/
# svn export http://svn.codehaus.org/proxytoys/tags/1.0/ proxytoys-1.0
# tar cJf proxytoys-1.0.tar.xz proxytoys-1.0
Source0:       https://github.com/proxytoys/proxytoys/archive/%{githash}/%{name}-%{githash}.tar.gz
# initializationError
# java.lang.Exception:
# The class com.thoughtworks.proxy.AllTests$StandardSuite is not public.
# The class com.thoughtworks.proxy.AllTests$CglibSuite is not public.
Patch0:        proxytoys-1.0-tests.patch

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jvnet.hudson:xstream)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(xpp3:xpp3)

BuildArch:     noarch
Source44: import.info

%description
ProxyToys provides a collection of toys acting as factories for
creating "special" proxies such as:

* Decorators - for simple AOP-like chained method interception
* Delegates - for method invocation on a delegate object,
  that might have different type
* Dispatcher proxy - single proxy instance dispatching method
  calls to different object with separate types
* Echo proxy - for tracing method calls
* Failover objects - fails over to a next object in case of
  exception
* Hot swapping proxy - allows implementation hiding that
  can be swapped, and mutual dependencies
* Multicasting objects - for multicasting a method invocation
  to multiple objects
* Null objects - for default implementations of classes that
  do nothing at all
* Pool - for a pool implementation with proxied objects that
  return automatically to the pool

%package example-code
Group: Development/Java
Summary:       ProxyToys Example Code

%description example-code
This package contains ProxyToys example code.

%package parent
Group: Development/Java
Summary:       ProxyToys parent POM

%description parent
ProxyToys parent POM.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
find -name '*.class' -delete
find -name '*.jar' -print -delete
%patch0 -p0

# require xsite-maven-plugin
%pom_disable_module website

# remove wagon-webdav-jackrabbit
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin :xsite-maven-plugin
# Unwanted source jar
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-source-plugin example-code
%pom_remove_plugin :maven-source-plugin %{name}
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin %{name}
# Unwanted javadoc jar. required only for build website module
%pom_remove_plugin :maven-javadoc-plugin %{name}

%pom_remove_plugin :findbugs-maven-plugin %{name}
%pom_remove_plugin :javancss-maven-plugin %{name}
%pom_remove_plugin :jdepend-maven-plugin %{name}
%pom_remove_plugin :jxr-maven-plugin %{name}
%pom_remove_plugin :maven-pmd-plugin %{name}

%pom_xpath_remove "pom:dependency[pom:classifier='javadoc']"

%pom_change_dep cglib: :cglib
%pom_change_dep cglib: :cglib %{name}
# cglib is not an optional dep
%pom_xpath_set "pom:dependency[pom:groupId='cglib']/pom:optional" false %{name}

# Fix test deps
# see https://issues.jenkins-ci.org/browse/JENKINS-4752
# solved in https://kenai.com/projects/hudson/sources/xstream/revision/23
# com.thoughtworks.xstream.converters.ConversionException:
# java.lang.Class cannot be cast to java.lang.ref.WeakReference
%pom_change_dep :xstream org.jvnet.hudson:
%pom_change_dep :xstream org.jvnet.hudson: %{name}
# NoClassDefFoundError: org/xmlpull/v1/XmlPullParserFactory
%pom_add_dep xpp3:xpp3:1.1.4c:test %{name}

%mvn_file :%{name} %{name}
%mvn_file :%{name}-example-code %{name}-example-code
%mvn_alias :%{name} "proxytoys:proxytoys"

%build
# Disable test suite incompatibility with newer cglib
%mvn_build -sf -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE.txt

%files example-code -f .mfiles-%{name}-example-code
%doc LICENSE.txt

%files parent -f .mfiles-%{name}-parent
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_8jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_6jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp8
- new version

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt3_2jpp5
- explicitly use junit3

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt2_2jpp5
- use jmock1

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_2jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_1jpp5
- fixed repocop warnings

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

