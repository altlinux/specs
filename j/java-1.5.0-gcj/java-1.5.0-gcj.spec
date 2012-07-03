Packager: Igor Vlasenko <viy@altlinux.ru>
%def_without src
%def_without devel
%define gccrpmsuffix    4.4
%define _with_bootstrap 1
%define _bootstrap 1
BuildRequires(pre): rpm-build-java
BuildRequires: /proc
%define version 1.5.0.0
%define name java-1.5.0-gcj
# python support for aot-compile
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

# convert an absolute path to a relative path.  each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%define abs2rel %{__perl} -e 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'

# resolve circular dependency between sinjdoc and java-1.5.0-gcj.
# define to 1 if sinjdoc has not been built yet.
%define bootstrap 1

# the plugin subpackage is disabled because libgcj's security
# infrastructure isn't ready to run untrusted applets.
%define enable_plugin 0

# the naming suffix for the gcc rpms we require (e.g., gcc4, libgcj4)
%define gccsuffix       -4.4

# the version-release string for the gcj rpms we require
%define gccver          4.4-alt2

# the version string for the java-gcj-compat release we require
%define jgcver          1.0.79

# hard-code libdir on 64-bit architectures to make the 64-bit JDK
# simply be another alternative
%ifarch ppc64 s390x x86_64 sparc64
%define syslibdir        %{_prefix}/lib64
%define _libdir          %{_prefix}/lib
%else
%define syslibdir        %{_libdir}
%endif

# standard JPackage naming and versioning defines
%define origin          gcj
%define priority        1500
%define javaver         1.5.0
%define buildver        0
%define name            java-%{javaver}-%{origin}

# standard JPackage directories and symbolic links
# make 64-bit JDKs just another alternative on 64-bit architectures
%define sdklnk          java-%{javaver}-%{origin}
%define jrelnk          jre-%{javaver}-%{origin}
%define sdkdir          %{name}-%{version}
%define jredir          %{sdkdir}/jre
%define sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%define jrebindir       %{_jvmdir}/%{jrelnk}/bin
%define jvmjardir       %{_jvmjardir}/%{name}-%{version}

%if %{enable_plugin}
%define plugindir       %{_libdir}/mozilla/plugins
%endif

%define debug_package %{nil}

Name:    %{name}
Version: %{javaver}.%{buildver}
Release: alt2_28jpp5.1.1
Summary: JPackage runtime compatibility layer for GCJ
Group:   System/Internationalization
# The LICENSE file has the classpath exception, but nothing in this package
# seems to use or even need it.
License: GPLv2+
URL:     http://sources.redhat.com/rhug/java-gcj-compat.html
Source0: ftp://sources.redhat.com/pub/rhug/java-gcj-compat-%{jgcver}.tar.gz
Source1: javadoc-workaround.patch


# required to calculate gcj binary's path to encode in aotcompile.py
# and rebuild-gcj-db
BuildRequires: gcc%{gccrpmsuffix}-java >= %{gccver}
BuildRequires: libgcj%{gccrpmsuffix}-src >= %{gccver}
# required for cacerts generation
%ifnarch %{ix86}
BuildRequires: ca-certificates
%else
# work around bug #500314
BuildRequires: ca-certificates
%endif
BuildRequires: python-devel
%if ! %{bootstrap}
# required for javadoc
BuildRequires: java-1.6.0-openjdk-devel
%endif
BuildRequires: unzip

# required for tools and libgcj.jar
Requires: libgcj%{gccrpmsuffix} >= %{gccver}
# required for directory structures
Requires: jpackage-utils >= 1.7.3
# required for java.security symlink.  also ensures that the proper
# libgcj is installed on multilib systems.
Requires: %{syslibdir}/security/classpath.security
%if ! %{bootstrap}
# required for javadoc symlink
Requires: sinjdoc
%endif
# post requires alternatives to install tool alternatives
Requires(post): alternatives >= 0:0.4
# post requires gij to retrieve gcc version
Requires(post): %{_bindir}/gij%{gccsuffix}
# post rebuilds the gcj database
Requires(post): %{_bindir}/rebuild-gcj-db
# rebuild-gcj-db requires gcj-dbtool
Requires(post): %{_bindir}/gcj-dbtool%{gccsuffix}
# rebuild-gcj-db requires findutils
Requires(post): findutils
# postun requires alternatives to uninstall tool alternatives
Requires(postun): alternatives >= 0:0.4
# postun requires gij to retrieve gcc version
Requires(postun): %{_bindir}/gij%{gccsuffix}
# postun rebuilds the gcj database
Requires(postun): %{_bindir}/rebuild-gcj-db
# rebuild-gcj-db requires gcj-dbtool
Requires(postun): %{_bindir}/gcj-dbtool%{gccsuffix}
# rebuild-gcj-db requires findutils
Requires(postun): findutils
# triggerin requires alternatives to install tool alternatives
Requires(triggerin): alternatives >= 0:0.4
# triggerin requires gij to retrieve gcc version
Requires(triggerin): %{_bindir}/gij%{gccsuffix}
# triggerin requires perl for abs2rel
Requires(triggerin): perl

# standard JPackage base provides
Provides: jre-%{javaver}-%{origin} = %{version}-%{release}
Provides: jre-%{origin} = %{version}-%{release}
Provides: jre-%{javaver} = %{version}-%{release}
Provides: java-%{javaver} = %{version}-%{release}
Provides: jre = %{javaver}
Provides: java-%{origin} = %{version}-%{release}
Provides: java = %{javaver}
# libgcj provides, translated to JPackage provides
Provides: jaas = %{version}-%{release}
Provides: jce = %{version}-%{release}
Provides: jdbc-stdext = %{version}-%{release}
Provides: jdbc-stdext = 3.0
Provides: jndi = %{version}-%{release}
Provides: jndi-cos = %{version}-%{release}
Provides: jndi-dns = %{version}-%{release}
Provides: jndi-ldap = %{version}-%{release}
Provides: jndi-rmi = %{version}-%{release}
Provides: jsse = %{version}-%{release}
Provides: java-sasl = %{version}-%{release}
Provides: jaxp_parser_impl = %{version}-%{release}
# java-gcj-compat base provides
Provides: java-gcj-compat = %{jgcver}
Provides: java-1.4.2-gcj-compat > 1.4.2.0-40jpp.111

Obsoletes: java-1.4.2-gcj-compat <= 1.4.2.0-40jpp.111
Obsoletes: gnu-crypto <= 2.1.0-2jpp.1
Obsoletes: gnu-crypto-sasl-jdk1.4 <= 2.1.0-2jpp.1
Obsoletes: jessie <= 1.0.1-7

%description
This package installs directory structures, shell scripts and symbolic
links to simulate a JPackage-compatible runtime environment with GCJ.

%if_with devel
%package devel
Summary: JPackage development compatibility layer for GCJ
Group:   Development/Java

# FIXME: require libgcj-src for tools.jar symlink
Requires: libgcj%{gccrpmsuffix}-src >= %{gccver}
# require base package
Requires: %{name} = %{version}-%{release}
# require eclipse-ecj for ecj binary
Requires: eclipse-ecj >= 3.2.1
# require python for aot-compile
Requires: python
# require gcc-java for gjavah binary
Requires: gcc%{gccrpmsuffix}-java >= %{gccver}
# post requires alternatives to install tool alternatives
Requires(post): alternatives >= 0:0.4
# post requires gcj to retrieve gcj header file locations
Requires(post): %{_bindir}/gcj%{gccsuffix}
# postun requires alternatives to uninstall tool alternatives
Requires(postun): alternatives >= 0:0.4
# triggerin requires gij to retrieve gcc version
Requires(triggerin): %{_bindir}/gij%{gccsuffix}
# triggerin requires gcj to retrieve gcj header file locations
Requires(triggerin): %{_bindir}/gcj%{gccsuffix}
# triggerin requires perl for abs2rel
Requires(triggerin): perl

# standard JPackage devel provides
Provides: java-sdk-%{javaver}-%{origin} = %{version}
Provides: java-sdk-%{javaver} = %{version}
Provides: java-sdk-%{origin} = %{version}
Provides: java-sdk = %{javaver}
Provides: java-%{javaver}-devel = %{version}
Provides: java-devel-%{origin} = %{version}
Provides: java-devel = %{javaver}
# java-gcj-compat devel provides
Provides: java-gcj-compat-devel = %{jgcver}
Provides: java-1.4.2-gcj-compat-devel > 1.4.2.0-40jpp.111

Obsoletes: java-1.4.2-gcj-compat-devel <= 1.4.2.0-40jpp.111
Requires: %name-aot-compile = %version-%release
%endif #devel

%if_with devel
%description devel
This package installs directory structures, shell scripts and symbolic
links to simulate a JPackage-compatible development environment with
GCJ.
%endif #devel

%if_with src
%package src
Summary: Source files for libgcj
Group:   Development/Java

Requires: %{name} = %{version}-%{release}
Requires: libgcj%{gccrpmsuffix}-src >= %{gccver}
# post requires gij to retrieve gcc version
Requires(post): %{_bindir}/gij%{gccsuffix}
# triggerin requires gij to retrieve gcc version
Requires(triggerin): %{_bindir}/gij%{gccsuffix}
# triggerin requires perl for abs2rel
Requires(triggerin): perl

# java-gcj-compat src provides
Provides: java-1.4.2-gcj-compat-src > 1.4.2.0-40jpp.111

Obsoletes: java-1.4.2-gcj-compat-src <= 1.4.2.0-40jpp.111
%endif #src

%if_with src
%description src
This package installs a src.zip symbolic link that points to a
specific version of the libgcj sources.
%endif #src

%if ! %{bootstrap}
%package javadoc
Summary: API documentation for libgcj
Group:   Development/Java

# require base package
Requires: %{name} = %{version}-%{release}

# standard JPackage javadoc provides
Provides: java-javadoc = %{version}-%{release}
Provides: java-%{javaver}-javadoc = %{version}-%{release}
# java-gcj-compat javadoc provides
Provides: java-1.4.2-gcj-compat-javadoc > 1.4.2.0-40jpp.111

Obsoletes: java-1.4.2-gcj-compat-javadoc <= 1.4.2.0-40jpp.111
Obsoletes: gnu-crypto-javadoc <= 2.1.0-2jpp.1

%description javadoc
This package installs Javadoc API documentation for libgcj.
%endif

%if %{enable_plugin}
%package plugin
Summary: Web browser plugin that handles applets
Group:   Development/Java

# require base package
Requires: %{name} = %{version}-%{release}
# require libgcj for plugin shared object
Requires: libgcj%{gccsuffix} >= %{gccver}
# require Mozilla plugin directory
Requires: %{plugindir}
# post requires gij to retrieve gcc version
Requires(post): %{_bindir}/gij%{gccsuffix}
# post requires alternatives to install plugin alternative
Requires(post): alternatives >= 0:0.4
# post requires Mozilla plugin directory
Requires(post): %{plugindir}
# postun requires gij to retrieve gcc version
Requires(postun): %{_bindir}/gij%{gccsuffix}
# postun requires alternatives to uninstall plugin alternative
Requires(postun): alternatives >= 0:0.4
# triggerin requires gij to retrieve gcc version
Requires(triggerin): %{_bindir}/gij%{gccsuffix}
# triggerin requires alternatives to install plugin alternative
Requires(triggerin): alternatives >= 0:0.4

# standard JPackage plugin provides
Provides: java-plugin = %{javaver}
Provides: java-%{javaver}-plugin = %{version}
# java-gcj-compat plugin provides
Provides: java-1.4.2-gcj-compat-plugin > 1.4.2.0-40jpp.111

Obsoletes: java-1.4.2-gcj-compat-plugin <= 1.4.2.0-40jpp.111

%description plugin
This package installs a symbolic link to gcjwebplugin, a Mozilla
plugin for applets.
%endif


%package aot-compile

Summary: java jcj ahead-of-time compile scripts
Group: Development/Java
BuildArch: noarch

%description aot-compile
java jcj ahead-of-time compile scripts

%prep
%setup -q -n java-gcj-compat-%{jgcver}
%__subst s,/etc/pki/tls/cert.pem,/usr/share/ca-certificates/ca-bundle.crt, generate-cacerts.pl
# hack: gcc4.1 seems to have no gjavah
for i in Makefile*; do 
%__subst s,gjavah,gjnih, $i
# bootstrap hack; sinjdoc not built yet
%if %{bootstrap}
%__subst s,sinjdoc,gij, $i
%endif
done

for i in Makefile.am Makefile.in; do
    subst 's,python setup.py install --prefix=\$\(DESTDIR\)\$\(prefix\),%__python setup.py install --root=%buildroot  --optimize=2 --record=INSTALLED_FILES,' $i
done

%build
# Print kernel version in logs.
uname -a
%configure --disable-symlinks --with-arch-directory=%{_arch} \
  --with-os-directory=linux \
  --with-security-directory=%{_sysconfdir}/java/security/security.d
make

# the python compiler encodes the source file's timestamp in the .pyc
# and .pyo headers.  since aotcompile.py is generated by configure,
# its timestamp will differ from build to build.  this causes multilib
# conflicts.  we work around this by setting aotcompile.py's timestamp
# to equal aotcompile.py.in's timestamp. (205216)
touch --reference=aotcompile.py.in aotcompile.py

%install

make DESTDIR=$RPM_BUILD_ROOT install

# extensions handling
install -dm 755 $RPM_BUILD_ROOT%{jvmjardir}
pushd $RPM_BUILD_ROOT%{jvmjardir}
  RELATIVE=$(%{abs2rel} %{_jvmdir}/%{jredir}/lib %{jvmjardir})
  for jarname in jaas jce jdbc-stdext jndi jndi-cos jndi-dns \
    jndi-ldap jndi-rmi jsse sasl
  do
    ln -s $RELATIVE/$jarname.jar $jarname-%{version}.jar
  done
  for jar in *-%{version}.jar
  do
    ln -sf ${jar} $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
    ln -sf ${jar} $(echo $jar | sed "s|-%{version}.jar|.jar|g")
  done
popd

# security directory and provider list
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
  RELATIVE=$(%{abs2rel} %{syslibdir}/security \
    %{_jvmdir}/%{jredir}/lib/security)
  ln -sf $RELATIVE/classpath.security java.security
popd
# default security providers, provided by libgcj
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d
for provider in \
  1000-gnu.java.security.provider.Gnu \
  1001-gnu.javax.crypto.jce.GnuCrypto \
  1002-gnu.javax.crypto.jce.GnuSasl \
  1003-gnu.javax.net.ssl.provider.Jessie \
  1004-gnu.javax.security.auth.callback.GnuCallbacks
do
  cat > $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d/$provider << EOF
# This file's contents are ignored.  Its name, of the form
# <priority>-<provider name>, is used by post and postun scripts to
# rebuild the list of security providers in libgcj's
# classpath.security file.
EOF
done
# cacerts
%{__perl} generate-cacerts.pl
install -m 644 cacerts $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security

# versionless symbolic links
pushd $RPM_BUILD_ROOT%{_jvmdir}
   ln -s %{jredir} %{jrelnk}
   ln -s %{sdkdir} %{sdklnk}
popd
pushd $RPM_BUILD_ROOT%{_jvmjardir}
   ln -s %{sdkdir} %{jrelnk}
   ln -s %{sdkdir} %{sdklnk}
popd

# classmap database directory
install -dm 755 $RPM_BUILD_ROOT%{syslibdir}/gcj

%if ! %{bootstrap}
# build and install API documentation
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
pushd $RPM_BUILD_ROOT%{_javadocdir}
  ln -s %{name} java
popd
mkdir docsbuild
pushd docsbuild
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')
  echo ==== CHECK ZIP ====
  unzip -tq /usr/share/java/src-$GIJ_VERSION.zip || :
  echo ==== END CHECK ZIP ====
  if unzip -tq /usr/share/java/src-$GIJ_VERSION.zip
  then
    fastjar xvf /usr/share/java/src-$GIJ_VERSION.zip
    rm -rf gnu
    patch -p0 < %{SOURCE1}
    find ./ -name \*.java | xargs -n 1 dirname | sort | uniq \
      | sed -e "s/\.\///" | sed -e "s/\//\./" \
      | sed -e "s/\//\./" | sed -e "s/\//\./" \
      | sed -e "s/\//\./" | sed -e "s/\//\./" \
      | xargs javadoc -quiet \
      -d $RPM_BUILD_ROOT%{_javadocdir}/%{name} \
      -encoding UTF-8 -breakiterator \
      -linksource -splitindex -doctitle "GNU libgcj $GIJ_VERSION" \
      -windowtitle "GNU libgcj $GIJ_VERSION Documentation"
  else
    # Work around https://bugzilla.redhat.com/show_bug.cgi?id=404981
    touch $RPM_BUILD_ROOT%{_javadocdir}/%{name}/package-list
  fi
popd
%endif

# amd64 compatibility link
%ifarch x86_64
pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib
  ln -s %{_arch} amd64
popd
%endif

# install operating system include directory
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/include/linux

# install libjvm.so directories
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/client
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/server

# install tools.jar directory
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib

touch $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/include/jawt.h
touch $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/include/jni.h
touch $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/include/linux/jawt_md.h
touch $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/include/linux/jni_md.h
touch $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/tools.jar
touch $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/libjawt.so
touch $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/client/libjvm.so
touch $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/server/libjvm.so
touch $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/rt.jar
touch $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/src.zip

pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/jre/lib
  for jarname in jaas jce jdbc-stdext jndi jndi-cos jndi-dns \
    jndi-ldap jndi-rmi jsse sasl
  do
    ln -s rt.jar $jarname.jar
  done
popd
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/java_%{name}<<EOF
%{_bindir}/java	%{jrebindir}/java	%{priority}
%{_jvmdir}/jre	%{_jvmdir}/%{jrelnk}	%{jrebindir}/java
%{_jvmjardir}/jre	%{_jvmjardir}/%{jrelnk}	%{jrebindir}/java
%{_bindir}/keytool	%{jrebindir}/keytool	%{jrebindir}/java
%{_bindir}/rmiregistry	%{jrebindir}/rmiregistry	%{jrebindir}/java
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jre_%{origin}_%{name}<<EOF
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jrelnk}	%{priority}
%{_jvmjardir}/jre-%{origin}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jrelnk}
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jre_%{javaver}_%{name}<<EOF
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jrelnk}	%{priority}
%{_jvmjardir}/jre-%{javaver}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jrelnk}
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_parser_impl_%{name}<<EOF
%{_javadir}/jaxp_parser_impl.jar	%{_javadir}/libgcj-$GIJ_VERSION.jar	20
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javac_%{name}-devel<<EOF
%{_bindir}/javac	%{sdkbindir}/javac	%{priority}
%{_jvmdir}/java	%{_jvmdir}/%{sdklnk}	%{sdkbindir}/javac
%{_jvmjardir}/java	%{_jvmjardir}/%{sdklnk}	%{sdkbindir}/javac
%{_bindir}/javadoc	%{sdkbindir}/javadoc	%{sdkbindir}/javac
%{_bindir}/javah	%{sdkbindir}/javah	%{sdkbindir}/javac
%{_bindir}/jar	%{sdkbindir}/jar	%{sdkbindir}/javac
%{_bindir}/jarsigner	%{sdkbindir}/jarsigner	%{sdkbindir}/javac
%{_bindir}/appletviewer	%{sdkbindir}/appletviewer	%{sdkbindir}/javac
%{_bindir}/rmic	%{sdkbindir}/rmic	%{sdkbindir}/javac
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/java_sdk_%{origin}_%{name}-devel<<EOF
%{_jvmdir}/java-%{origin}	%{_jvmdir}/%{sdklnk}	%{priority}
%{_jvmjardir}/java-%{origin}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdklnk}
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/java_sdk_%{javaver}_%{name}-devel<<EOF
%{_jvmdir}/java-%{javaver}	%{_jvmdir}/%{sdklnk}	%{priority}
%{_jvmjardir}/java-%{javaver}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdklnk}
EOF
install -d -m755 %buildroot/usr/lib/jvm-exports/%{sdkdir}

%post



GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
  | awk '{ print $5 }')

# jaxp_parser_impl
:

{
  # Rebuild the list of security providers in classpath.security.
  # This used to be a standalone script, rebuild-security-providers,
  # provided by the Fedora version of jpackage-utils.  Now it is
  # inlined here and removed from Fedora's jpackage-utils for
  # compatibility with jpackage.org's jpackage-utils.  See:
  # https://bugzilla.redhat.com/show_bug.cgi?id=260161
  suffix=security/classpath.security
  secfiles="/usr/lib/$suffix /usr/lib64/$suffix"

  for secfile in $secfiles
  do
    # check if this classpath.security file exists
    [ -f "$secfile" ] || continue

    sed -i '/^security\.provider\./d' "$secfile"

    count=0
    for provider in $(ls /etc/java/security/security.d)
    do
      count=$((count + 1))
      echo "security.provider.${count}=${provider#*-}" >> "$secfile"
    done
  done
} || :


%triggerin -- libgcj%{gccrpmsuffix} >= %{gccver}
{
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')

  # jaxp_parser_impl
  alternatives --install %{_javadir}/jaxp_parser_impl.jar \
    jaxp_parser_impl \
    %{_javadir}/libgcj-$GIJ_VERSION.jar 20

  # rt.jar
  RELATIVE=$(%{abs2rel} %{_javadir} %{_jvmdir}/%{sdkdir}/jre/lib)
  ln -sf \
    $RELATIVE/libgcj-$GIJ_VERSION.jar \
    %{_jvmdir}/%{sdkdir}/jre/lib/rt.jar

  # libjawt.so
  RELATIVE=$(%{abs2rel} %{syslibdir}/gcj-$GIJ_VERSION \
    %{_jvmdir}/%{jredir}/lib/%{_arch})
  ln -sf $RELATIVE/libjawt.so \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/libjawt.so

  # libjvm.so
  RELATIVE=$(%{abs2rel} %{syslibdir}/gcj-$GIJ_VERSION \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/client)
  ln -sf $RELATIVE/libjvm.so \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/client/libjvm.so
  RELATIVE=$(%{abs2rel} %{syslibdir}/gcj-$GIJ_VERSION \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/server)
  ln -sf $RELATIVE/libjvm.so \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/server/libjvm.so
} || :

%postun
if [ $1 -eq 0 ]
then
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')
  :
fi

{
  # Rebuild the list of security providers in classpath.security
  suffix=security/classpath.security
  secfiles="/usr/lib/$suffix /usr/lib64/$suffix"

  for secfile in $secfiles
  do
    # check if this classpath.security file exists
    [ -f "$secfile" ] || continue

    sed -i '/^security\.provider\./d' "$secfile"

    count=0
    for provider in $(ls /etc/java/security/security.d)
    do
      count=$((count + 1))
      echo "security.provider.${count}=${provider#*-}" >> "$secfile"
    done
  done
} || :


%if_with devel
%triggerin devel -- gcc%{gccrpmsuffix}-java >= %{gccver}
{
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')

  # tools.jar
  RELATIVE=$(%{abs2rel} %{_javadir} %{_jvmdir}/%{sdkdir}/lib)
  ln -sf \
    $RELATIVE/libgcj-tools-$GIJ_VERSION.jar \
    %{_jvmdir}/%{sdkdir}/lib/tools.jar

  # create symbolic links to headers in gcj's versioned directory
  for headername in jawt jni
  do
    DIRECTORY=$(dirname $(gcj%{gccsuffix} \
      -print-file-name=include/$headername.h))
    RELATIVE=$(%{abs2rel} $DIRECTORY %{_jvmdir}/%{sdkdir}/include)
    ln -sf $RELATIVE/$headername.h \
      %{_jvmdir}/%{sdkdir}/include/$headername.h
  done
  for headername in jawt_md jni_md
  do
    DIRECTORY=$(dirname $(gcj%{gccsuffix} \
      -print-file-name=include/$headername.h))
    RELATIVE=$(%{abs2rel} $DIRECTORY %{_jvmdir}/%{sdkdir}/include/linux)
    ln -sf $RELATIVE/$headername.h \
      %{_jvmdir}/%{sdkdir}/include/linux/$headername.h
  done
} || :
%endif #devel

%if_with devel
%postun devel
if [ $1 -eq 0 ]
then
  :
fi
%endif #devel

%if_with src
%triggerin src -- libgcj%{gccrpmsuffix}-src >= %{gccver}
{
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')
  RELATIVE=$(%{abs2rel} %{_javadir} %{_jvmdir}/%{sdkdir})
  ln -sf \
    $RELATIVE/src-$GIJ_VERSION.zip \
    %{_jvmdir}/%{sdkdir}/src.zip
} || :
%endif #src

%if %{enable_plugin}
%triggerin plugin -- libgcj%{gccrpmsuffix} >= %{gccver}
{
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')
  alternatives --install %{plugindir}/libjavaplugin.so \
    libjavaplugin.so %{syslibdir}/gcj-$GIJ_VERSION/libgcjwebplugin.so \
    %{priority}
} || :

%postun plugin
if [ $1 -eq 0 ]
then
  GIJ_VERSION=$(gij%{gccsuffix} --version | head -n 2 | tail -n 1 \
    | awk '{ print $5 }')
  :
fi
%endif

%if_with main_package
%files
%_altdir/jaxp_parser_impl_%{name}
%_altdir/jre_%{javaver}_%{name}
%_altdir/jre_%{origin}_%{name}
%_altdir/java_%{name}
%doc AUTHORS ChangeLog COPYING LICENSE README
%dir %{_jvmdir}/%{sdkdir}
%dir %{_jvmdir}/%{jredir}
%dir %{_jvmdir}/%{jredir}/bin
%dir %{_jvmdir}/%{jredir}/lib
%dir %{_jvmdir}/%{jredir}/lib/%{_arch}
%dir %{_jvmdir}/%{jredir}/lib/%{_arch}/client
%dir %{_jvmdir}/%{jredir}/lib/%{_arch}/server
%dir %{_jvmdir}/%{jredir}/lib/security
%dir %{jvmjardir}
%dir %{syslibdir}/gcj
%{_bindir}/rebuild-gcj-db
%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/%{jredir}/bin/keytool
%{_jvmdir}/%{jredir}/bin/rmiregistry
%{_jvmdir}/%{jredir}/lib/security/cacerts
%{_jvmdir}/%{jredir}/lib/security/java.security
%{_jvmdir}/%{jredir}/lib/jaas.jar
%{_jvmdir}/%{jredir}/lib/jce.jar
%{_jvmdir}/%{jredir}/lib/jdbc-stdext.jar
%{_jvmdir}/%{jredir}/lib/jndi-cos.jar
%{_jvmdir}/%{jredir}/lib/jndi-dns.jar
%{_jvmdir}/%{jredir}/lib/jndi-ldap.jar
%{_jvmdir}/%{jredir}/lib/jndi-rmi.jar
%{_jvmdir}/%{jredir}/lib/jndi.jar
%{_jvmdir}/%{jredir}/lib/jsse.jar
%{_jvmdir}/%{jredir}/lib/sasl.jar
%ifarch x86_64
%{_jvmdir}/%{jredir}/lib/amd64
%endif
%{_jvmdir}/%{jrelnk}
%{jvmjardir}/jaas.jar
%{jvmjardir}/jaas-%{javaver}.jar
%{jvmjardir}/jaas-%{version}.jar
%{jvmjardir}/jce.jar
%{jvmjardir}/jce-%{javaver}.jar
%{jvmjardir}/jce-%{version}.jar
%{jvmjardir}/jdbc-stdext.jar
%{jvmjardir}/jdbc-stdext-%{javaver}.jar
%{jvmjardir}/jdbc-stdext-%{version}.jar
%{jvmjardir}/jndi.jar
%{jvmjardir}/jndi-%{javaver}.jar
%{jvmjardir}/jndi-%{version}.jar
%{jvmjardir}/jndi-cos.jar
%{jvmjardir}/jndi-cos-%{javaver}.jar
%{jvmjardir}/jndi-cos-%{version}.jar
%{jvmjardir}/jndi-dns.jar
%{jvmjardir}/jndi-dns-%{javaver}.jar
%{jvmjardir}/jndi-dns-%{version}.jar
%{jvmjardir}/jndi-ldap.jar
%{jvmjardir}/jndi-ldap-%{javaver}.jar
%{jvmjardir}/jndi-ldap-%{version}.jar
%{jvmjardir}/jndi-rmi.jar
%{jvmjardir}/jndi-rmi-%{javaver}.jar
%{jvmjardir}/jndi-rmi-%{version}.jar
%{jvmjardir}/jsse.jar
%{jvmjardir}/jsse-%{javaver}.jar
%{jvmjardir}/jsse-%{version}.jar
%{jvmjardir}/sasl.jar
%{jvmjardir}/sasl-%{javaver}.jar
%{jvmjardir}/sasl-%{version}.jar
%{_jvmjardir}/%{jrelnk}
%ghost %{_jvmdir}/%{sdkdir}/jre/lib/rt.jar
%ghost %{_jvmdir}/%{jredir}/lib/%{_arch}/libjawt.so
%ghost %{_jvmdir}/%{jredir}/lib/%{_arch}/client/libjvm.so
%ghost %{_jvmdir}/%{jredir}/lib/%{_arch}/server/libjvm.so
# These must not be marked %config(noreplace).  Their file names are
# used in post and postun.  Their contents are ignored, so replacing
# them doesn't matter.  .rpmnew files are harmful since they're
# interpreted by post and postun as classnames ending in rpmnew.
%{_sysconfdir}/java/security/security.d/1000-gnu.java.security.provider.Gnu
%{_sysconfdir}/java/security/security.d/1001-gnu.javax.crypto.jce.GnuCrypto
%{_sysconfdir}/java/security/security.d/1002-gnu.javax.crypto.jce.GnuSasl
%{_sysconfdir}/java/security/security.d/1003-gnu.javax.net.ssl.provider.Jessie
%{_sysconfdir}/java/security/security.d/1004-gnu.javax.security.auth.callback.GnuCallbacks
%dir /usr/lib/jvm-exports/%{sdkdir}
%endif #main_package

%if_with devel
%files devel
%_altdir/java_sdk_%{javaver}_%{name}-devel
%_altdir/java_sdk_%{origin}_%{name}-devel
%_altdir/javac_%{name}-devel
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/include/linux
%dir %{_jvmdir}/%{sdkdir}/lib
%{_bindir}/aot-compile
%{_bindir}/aot-compile-rpm
#%{python_sitelib}/aotcompile.py*
#%{python_sitelib}/classfile.py*
#%{python_sitelib}/java_gcj_compat-%{jgcver}-py?.?.egg-info
%{_jvmdir}/%{sdkdir}/bin/appletviewer
%{_jvmdir}/%{sdkdir}/bin/jar
%{_jvmdir}/%{sdkdir}/bin/jarsigner
%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/%{sdkdir}/bin/javadoc
%{_jvmdir}/%{sdkdir}/bin/javah
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/rmic
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%ghost %{_jvmdir}/%{sdkdir}/include/jawt.h
%ghost %{_jvmdir}/%{sdkdir}/include/jni.h
%ghost %{_jvmdir}/%{sdkdir}/include/linux/jawt_md.h
%ghost %{_jvmdir}/%{sdkdir}/include/linux/jni_md.h
%ghost %{_jvmdir}/%{sdkdir}/lib/tools.jar
%dir /usr/lib/jvm-exports/%{sdkdir}
%exclude %_bindir/aot-compile*
%endif #devel

%if_with src
%files src
#%ghost %{_jvmdir}/%{sdkdir}/src.zip
%endif #src

%if ! %{bootstrap}
%files javadoc
%doc %{_javadocdir}/%{name}
# A JPackage that "provides" this directory will, in its %post script,
# remove the existing directory and install a new symbolic link to its
# versioned directory.  For Fedora we want clear file ownership so we
# make java-1.5.0-gcj-javadoc own this file.  Installing the
# corresponding JPackage over java-1.5.0-gcj-javadoc will work but
# will invalidate this file.
%doc %{_javadocdir}/java
%endif

%if %{enable_plugin}
%files plugin
%endif

%files aot-compile
%_bindir/aot-compile*
/usr/lib/python*/site-packages/*


%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0.0-alt2_28jpp5.1.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.0-alt2_28jpp5.1
- Rebuilt with python 2.6

* Tue Oct 27 2009 Igor Vlasenko <viy@altlinux.ru> 1.5.0.0-alt2_28jpp5
- fixed bug (BuildRequires on jpackage-1.6-compat) thanks to kirill@shutemov.

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 1.5.0.0-alt1_28jpp6
- first build

