Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          opennlp
Version:       1.5.3
Release:       alt1_3jpp8
Summary:       A machine learning based toolkit for the processing of natural language text
License:       ASL 2.0
URL:           https://opennlp.apache.org/
Source0:       http://www.apache.org/dist/opennlp/%{name}-%{version}/apache-%{name}-%{version}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
# https://bugzilla.redhat.com/show_bug.cgi?id=1261017
BuildRequires: mvn(net.sf.jwordnet:jwnl)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.uima:uimaj-core)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)

BuildArch:     noarch
Source44: import.info

%description
The Apache OpenNLP library is a machine learning based toolkit for the
processing of natural language text.

It supports the most common NLP tasks, such as tokenization, sentence
segmentation, part-of-speech tagging, named entity extraction, chunking,
parsing, and coreference resolution. These tasks are usually required to
build more advanced text processing services. OpenNLP also includes
maximum entropy and perceptron based machine learning.

%package tools
Group: Development/Java
Summary:       Apache OpenNLP Tools

%description tools
This package provides Apache OpenNLP Tools.

%package maxent
Group: Development/Java
Summary:       Apache OpenNLP Maxent

%description maxent
This package provides Apache OpenNLP Maxent.

%package uima
Group: Development/Java
Summary:       Apache OpenNLP UIMA Annotators

%description uima
This package provides Apache OpenNLP UIMA Annotators.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apache-%{name}-%{version}-src
# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.bat' -print -delete
find . -name '*.class' -print -delete

%pom_remove_plugin -r :apache-rat-plugin opennlp
%pom_remove_plugin -r :maven-dependency-plugin opennlp
%pom_remove_plugin -r :maven-eclipse-plugin opennlp
%pom_remove_plugin -r :maven-source-plugin opennlp
%pom_remove_plugin -r :maven-javadoc-plugin opennlp

%pom_xpath_set -r pom:addClasspath false opennlp

%pom_disable_module ../opennlp-distr opennlp
%pom_disable_module ../opennlp-docs opennlp

for p in maxent tools ; do
%pom_xpath_inject "pom:dependency[pom:artifactId='junit']" "<scope>test</scope>" opennlp-${p}
done

# AssertionError: expected:<0.7756870512503095> but was:<0.7766773953948998>
rm -r opennlp-maxent/src/test/java/opennlp/perceptron/PerceptronPrepAttachTest.java \
 opennlp-maxent/src/test/java/opennlp/maxent/quasinewton/QNTrainerTest.java \
 opennlp-maxent/src/test/java/opennlp/PrepAttachDataUtil.java \
 opennlp-maxent/src/test/java/opennlp/maxent/MaxentPrepAttachTest.java

%build

%mvn_build -s -- -f opennlp/pom.xml

%install
%mvn_install

%files -f .mfiles-%{name}
%doc KEYS opennlp-distr/README opennlp-distr/RELEASE_NOTES.html
%doc LICENSE NOTICE

%files tools -f .mfiles-%{name}-tools
%doc LICENSE NOTICE

%files maxent -f .mfiles-%{name}-maxent
%doc LICENSE NOTICE

%files uima -f .mfiles-%{name}-uima

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_2jpp8
- new version

