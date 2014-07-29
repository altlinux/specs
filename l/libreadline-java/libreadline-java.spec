Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global editline_ver    2.9
%global src_dirs        org test

Name:    libreadline-java
Version: 0.8.0
Release: alt2_31jpp7
Summary: Java wrapper for the EditLine library
Group:   Development/Java

License: LGPLv2+
URL:     http://java-readline.sf.net/
Source0: http://download.sf.net/java-readline/%{name}-%{version}-src.tar.gz
Patch0:  %{name}-ncurses.patch
Patch1:  %{name}-libdir.patch

BuildRequires: jpackage-utils >= 1.5
BuildRequires: libedit-devel >= %{editline_ver}
BuildRequires: ncurses-devel

Requires:         libedit >= %{editline_ver}
Source44: import.info

%description
libreadline-java provides Java bindings for libedit though a JNI
wrapper.

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1
sed -i 's|@LIBDIR@|%{_libdir}|' src/org/gnu/readline/Readline.java
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

# install jar file and JNI library under %{_libdir}/%{name}
# FIXME: fix jpackage-utils to handle multilib correctly
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m 644 %{name}.jar \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}.jar
install -m 755 libJavaEditline.so $RPM_BUILD_ROOT%{_libdir}/%{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog NEWS README README.1st VERSION COPYING.LIB
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
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

