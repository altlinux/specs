# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:             guessencoding
Version:          1.4
Release:          alt2_12jpp8
Summary:          Guess encoding of files and return configured reader
Group:            Development/Other
License:          ASL 2.0
URL:              http://docs.codehaus.org/display/GUESSENC/
# svn export http://svn.codehaus.org/guessencoding/tags/guessencoding-1.4/
# tar caf guessencoding-1.4.tar.gz guessencoding-1.4
Source0:          %{name}-%{version}.tar.gz
# Comment out wagon-webdav extension as it is not needed in Fedora
Patch0:           guessencoding-webdav.patch
BuildArch:        noarch

BuildRequires:    maven-local

%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
%endif
Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
The purpose of this library is to "guess" the encoding of files, and retrieve
a reader that is properly configured to use the right encoding as guessed.
The library is able to recognize the various Unicode encoding variants:

    * UTF-8
    * UTF-16LE - Low Endian
    * UTF-16BE - Big Endian
    * UTF-32

If a Unicode encoding isn't recognized, it's an 8-bit encoding. If the 8-bit
encoding is not US-ASCII, the default platform 8-bit encoding is assumed
whatever it is. However, the library cannot guess between different 8-bit
encodings. Only statistical analysis, n-grams and similar techniques specific
to each language used in those files can help guessing the encoding, but this
is not supported by the library.


%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1 -b .webdav


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version

