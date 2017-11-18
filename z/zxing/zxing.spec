Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          zxing
Version:       3.2.1
Release:       alt2_4jpp8
Summary:       Java multi-format 1D/2D bar-code image processing library
License:       ASL 2.0
URL:           https://github.com/zxing/zxing/
# remove unused files (126MB)
# sh zxing-repack.sh <VERSION>
Source0:       %{name}-%{version}.tar.xz
Source1:       zxing-repack.sh

BuildRequires: maven-local
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(junit:junit)

# https://fedorahosted.org/fpc/ticket/574
Provides: bundled(barcode4j)

BuildArch:     noarch
Source44: import.info

%description
ZXing ("zebra crossing") is an open-source,
multi-format 1D/2D bar-code image processing library
implemented in Java, with ports to other languages.

%package javase
Group: Development/Java
Summary:       ZXing Java SE extensions

%description javase
Java SE-specific extensions to core ZXing library.

%package parent
Group: Development/Java
Summary:       ZXing Parent POM

%description parent
This package provides ZXing Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_dep com.google.android:
%pom_remove_dep :android-core
%pom_remove_dep :android-integration

%pom_disable_module android-core
%pom_disable_module android-integration
# use com.google.gwt:gwt-{servlet,user}:2.6.1,org.codehaus.mojo:gwt-maven-plugin
%pom_disable_module zxing.appspot.com
%pom_disable_module zxingorg

# Unwanted/unneeded tasks
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-release-plugin
# Break build
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :apache-rat-plugin
# Unavailble plugin
%pom_remove_plugin -r :clirr-maven-plugin

# Unavailable test resources
rm -r core/src/test/java/com/google/zxing/qrcode/QRCodeWriterTestCase.java \
 core/src/test/java/com/google/zxing/qrcode/QRCodeBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/datamatrix/DataMatrixBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/pdf417/PDF417BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/EAN13BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code39BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/UPCEANExtensionBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/UPCABlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code93BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/UPCEBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code128BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/CodabarBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/ITFBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/negative \
 core/src/test/java/com/google/zxing/oned/EAN8BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/Code39ExtendedBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/RSS14BlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedStackedBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/aztec/AztecBlackBox*TestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedInternalTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedStackedInternalTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedImage2stringTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedImage2binaryTestCase.java \
 core/src/test/java/com/google/zxing/oned/rss/expanded/RSSExpandedImage2resultTestCase.java

sed -i '/DataMatrixBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/Code39BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/EAN13BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/UPCABlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/UPCABlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/UPCEBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/PDF417BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/QRCodeBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/Code128BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/ITFBlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/EAN8BlackBox/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java
sed -i '/Code39ExtendedBlackBox2TestCase/d' core/src/test/java/com/google/zxing/AllPositiveBlackBoxTester.java

sed -i -e /-Werror/d pom.xml

%build

%mvn_build -s  -- -Dmaven.test.skip.exec=true  -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles-core
%doc AUTHORS CHANGES README.md
%doc COPYING NOTICE

%files javase -f .mfiles-javase
%doc COPYING NOTICE

%files parent -f .mfiles-zxing-parent
%doc COPYING NOTICE

%files javadoc -f .mfiles-javadoc
%doc COPYING NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt2_4jpp8
- fixed build

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_4jpp8
- fixed build

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_3jpp8
- new version

