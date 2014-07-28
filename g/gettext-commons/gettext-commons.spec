# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           gettext-commons
Version:        0.9.6
Release:        alt1_8jpp7
Summary:        Java internationalization (i18n) library

Group:          Development/Java
License:        LGPLv2+
URL:            http://code.google.com/p/gettext-commons/
Source0:        http://gettext-commons.googlecode.com/files/%{name}-%{version}-src.tar.gz
# This patch is from Debian
Patch0:         %{name}-0.9.6-buildxml.patch
# Fix some javadoc warnings
# http://code.google.com/p/gettext-commons/issues/detail?id=36
Patch1:         %{name}-0.9.6-javadoc.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  ant
Requires:       jpackage-utils
Source44: import.info


%description
The Gettext Commons project provides Java classes for internationalization 
(i18n) through GNU gettext.

The lightweight library combines the power of the unix-style gettext tools 
with the widely used Java ResourceBundles. This makes it possible to use the 
original text instead of arbitrary property keys, which is less cumbersome 
and makes programs easier to read.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;


%build
ant


%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p Releases/%{name}-0.9.jar   \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# JAR alias
pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar %{name}.jar
popd

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rp api/*  \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

#javadoc alias
pushd $RPM_BUILD_ROOT%{_javadocdir}
ln -sf %{name}-%{version} %{name}
popd



%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%doc ChangeLog LICENSE.txt README


%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_7jpp7
- new version

