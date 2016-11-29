Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           metadata-extractor
Version:        2.3.1
Release:        alt1_13jpp8
Summary:        JPEG metadata extraction framework

# Read upstream homepage for license information
License:        Public Domain
URL:            http://www.drewnoakes.com/code/exif/
Source0:        http://www.drewnoakes.com/code/exif/releases/%{name}-%{version}-src.jar
# Patch provided by Gabriel Ebner to remove all references to the 
# com.sun classes. Package builds with a free java implementation now.
Patch0:         %{name}-2.3.1-nosun.patch
# Patch from upstream svn r16
# Fix encoding errors
Patch1:         %{name}-2.3.1-encoding.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  ant-junit
Source44: import.info


%description
Java based metadata extraction library for JPEG images with support for Exif 
and Iptc metadata segments, including manufacturer specific metadata of 
several digital camera models.


%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

# Use system junit
build-jar-repository -s -p Libraries junit

# Fix end-of-line encoding
sed -i 's/\r//' ChangeLog.txt

# Delete test directories
find . -type d -name test -print | xargs rm -rf

# Disable junit tests
sed -i 's/depends="clean, compile, test"/depends="clean, compile"/' build.xml


%build
ant dist-binaries
ant javadoc ||:


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p Releases/%{name}-%{version}.jar   \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rp javadoc/*  \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

#javadoc alias
pushd $RPM_BUILD_ROOT%{_javadocdir}
ln -sf %{name}-%{version} %{name}
popd


%files
%{_javadir}/%{name}.jar
%doc ChangeLog.txt


%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}


%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_13jpp8
- new fc release

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_11jpp8
- fixed build with java8

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_10jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_9jpp7
- new version

