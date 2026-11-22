%define _unpackaged_files_terminate_build 1

Name: english-pos-dict
Version: 0.6
Release: alt1

Summary: English part-of-speech and spelling dictionaries
License: LGPL-2.1-or-later
Group: Development/Java
URL: https://github.com/languagetool-org/english-pos-dict
VCS: https://github.com/languagetool-org/english-pos-dict.git

Source0: %url/archive/52b8b63859850f27e63584036fbe857607ede6a3/%name-%version.tar.gz
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: python3
BuildRequires: mvn(org.carrot2:morfologik-fsa)
BuildRequires: mvn(org.carrot2:morfologik-stemming)
BuildRequires: mvn(org.carrot2:morfologik-fsa-builders)
BuildRequires: mvn(org.carrot2:morfologik-tools)
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.carrotsearch:hppc)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

BuildArch: noarch

%description
English part-of-speech, synthesis and six regional spelling dictionaries
in Morfologik format for LanguageTool.

%prep
%setup
%patch0 -p1
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%mvn_package :english-pos-dict english-pos-dict
%mvn_package :::sources: __noinstall
# Avoid the LanguageTool standalone -> English -> this dictionary cycle.
# This reference is the literal upstream JLanguageTool constant, not core API.
sed -i '/^import org.languagetool.JLanguageTool;/d; s/JLanguageTool.DICTIONARY_FILENAME_EXTENSION/".dict"/' bootstrap/languagetool-6.6/DictionaryBuilder.java

%build
mkdir -p bootstrap/classes
helper_cp=$(build-classpath \
    morfologik-stemming/morfologik-stemming \
    morfologik-stemming/morfologik-fsa \
    morfologik-stemming/morfologik-fsa-builders \
    morfologik-stemming/morfologik-tools commons-cli \
    jetbrains-annotations/annotations beust-jcommander/jcommander hppc/hppc)
javac -encoding UTF-8 -cp "$helper_cp" -d bootstrap/classes bootstrap/languagetool-6.6/*.java
export LT_DICT_CLASSPATH="$PWD/bootstrap/classes:$helper_cp"
# All eight product dictionaries are generated from tracked text inputs.
bash ./build-dicts-from-src.sh
%mvn_build -s -j -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles-english-pos-dict
%doc bootstrap/languagetool-6.6/COPYING.txt
%doc spell-data/hunspell/README_*.txt
%doc original-files-december-2023/pos-readme.txt

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 0.6-alt1
- Initial build for ALT.
