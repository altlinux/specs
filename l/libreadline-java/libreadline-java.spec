Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global editline_ver    2.9
%global src_dirs        org test

Name:          libreadline-java
Version:       0.8.0
Release:       alt3_42jpp8
Summary:       Java wrapper for the EditLine library
License:       LGPLv2+
URL:           http://java-readline.sf.net/
Source0:       http://download.sf.net/java-readline/%{name}-%{version}-src.tar.gz
Source1:       %{name}-%{version}-pom.xml
Patch0:        %{name}-ncurses.patch
Patch1:        %{name}-libdir.patch

BuildRequires: javapackages-local
BuildRequires: libedit-devel >= %{editline_ver}
BuildRequires: libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel

Requires:      libedit >= %{editline_ver}
Source44: import.info

%description
libreadline-java provides Java bindings for libedit though a JNI
wrapper.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1
sed -i 's|@LIBDIR@|%{_libdir}|' src/org/gnu/readline/Readline.java

sed -i 's|javadoc |javadoc -Xdoclint:none |' Makefile

%mvn_file net.sourceforge:%{name} %{name}
%__subst s,termcap,tinfo, src/native/Makefile

%build
export JAVA_HOME=%{java_home}
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
make CFLAGS="$RPM_OPT_FLAGS -fPIC -DPOSIX" T_LIBS=JavaEditline
make apidoc

# fix debuginfo package
rm -f %{src_dirs}
for dir in %{src_dirs}
do
  ln -s src/$dir
done

%install

# install jar file and JNI library under %%{_libdir}/%%{name}
# FIXME: fix jpackage-utils to handle multilib correctly
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 libJavaEditline.so %{buildroot}%{_libdir}/%{name}
%mvn_artifact %{SOURCE1} %{name}.jar
ln -sf %{_jnidir}/%{name}.jar %{buildroot}%{_libdir}/%{name}/%{name}.jar
%mvn_install -J api

%files -f .mfiles
%doc ChangeLog NEWS README README.1st VERSION
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%doc COPYING.LIB

%files javadoc -f .mfiles-javadoc
%doc COPYING.LIB

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt3_42jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt3_40jpp8
- %%_jnidir set to /usr/lib/java

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_40jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_33jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_31jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_30jpp7
- fc update

* Sun Feb 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_12jpp6
- build with new jnidir

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_12jpp5
- fixed repocop warnings

* Mon May 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_11jpp1.7
- fixed requires

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt1_11jpp1.7
- converted from JPackage by jppimport script

