%def_disable plugin

%ifarch %arm ppc ppc64
# not yet ported
%def_without sinjdoc
%else
%def_with sinjdoc
%endif

# note: at sync with fedora rel.28

Name: jdkgcj
Version: 0.5.9
Release: alt2

Summary: A free Java SDK
License: GPL
Group: Development/Java
Url: http://www.arklinux.org/projects/jdkgcj

# temporary: should be version
%define javafullver 1.5.0.0
# the version string for the java-gcj-compat release we require
%define jgcver          1.0.70

# standard JPackage naming and versioning defines
%define origin          gcj
%define priority        1490
#define priority        1500
%define javaver         1.5.0
%define buildver        0

%define jppname            java-%{javaver}-%{origin}

%define sdkdir          %{jppname}-%__gcc_version_base-%{javafullver}
%define java_home   %_jvmdir/%sdkdir
%define jredir      %sdkdir/jre
%define sdkbindir   %java_home/bin
%define jrebindir   %java_home/jre/bin
%define jvmjardir   %{_jvmjardir}/%sdkdir
%define sdklnk          java-%{javaver}-%{origin}
%define jrelnk          jre-%{javaver}-%{origin}

%if_enabled plugin
%define plugindir       %{_libdir}/mozilla/plugins
%endif


# a must for java-1.5.0-gcj-devel
Requires: libgcj%__gcc_version_base-jar	= %__gcc_version
Requires: libgcj%__gcc_version_base-plugins	= %__gcc_version
BuildRequires(pre): alternatives >= 0:0.4
BuildRequires(pre): rpm-build-java

Source: %name-%version.tar
Source1: altgcj-%version.tar
Source2: %name-refentry.xml

%set_compress_method gzip

BuildRequires: gcc%__gcc_version_base-java xmlto

Requires: java-1.5.0-gcj = %version-%release
#Requires: java-1.5.0-gcj-devel = %version-%release

#%package -n %jppname-devel
#Group: Development/Java
#Summary: JPackage development compatibility layer for GCJ
# java-x.x.x-gcj compatible provides
#------------------------------------
Requires: java-1.5.0-gcj-aot-compile
Provides: java-gcj-compat-devel = %jgcver
Provides: java-1.5.0-gcj-devel = %javafullver
#------------------------------------
# standard JPackage devel provides
#Provides: java-sdk-%{javaver}-%{origin} = %{version}
#Provides: java-sdk-%{javaver} = %{version}
#Provides: java-sdk-%{origin} = %{version}
#Provides: java-sdk = %{javaver}
#Provides: java-%{javaver}-devel = %{version}
#Provides: java-devel-%{origin} = %{version}
#Provides: java-devel = %{javaver}
%if_with sinjdoc
Requires: sinjdoc
%endif

# jre
%package -n %jppname
Group: Development/Java
Summary: JPackage runtime compatibility layer for GCJ

# due to GC Warning: Couldn't read /proc/stat and errors
Requires: /proc
Requires(pre): /proc
PreReq: gcc%__gcc_version_base-java = %__gcc_version
Requires: gcc-java-common >= 1.4.12-alt1
Requires: java-common >= 1.1

Provides: java-gcj-compat = %jgcver
Provides: java-1.5.0-gcj = %javafullver

# standard JPackage base provides
#Provides: jre-%{javaver}-%{origin} = %{version}-%{release}
#Provides: jre-%{origin} = %{version}-%{release}
#Provides: jre-%{javaver} = %{version}-%{release}
#Provides: java-%{javaver} = %{version}-%{release}
#Provides: jre = %{javaver}
#Provides: java-%{origin} = %{version}-%{release}
#Provides: java = %{javaver}

%description
jdkgcj provides an interface to gcj that is compatible with the Sun and IBM
Java Development Kits (JDKs).
jdkgcj provides the javac, java and javah tools as well as jni.h, allowing
you to compile java extensions using JNI.

%description -n %jppname
This package installs directory structures, shell scripts and symbolic
links to simulate a JPackage-compatible runtime environment with GCJ.

#%description -n %jppname-devel
#This package installs directory structures, shell scripts and symbolic
#links to simulate a JPackage-compatible development environment with
#GCJ.

%prep
%setup -n %name -a1

%build
%configure \
	--prefix=%java_home \
	--bindir=%sdkbindir \
	--includedir=%java_home/include
xmlto -o man man %SOURCE2

%install
rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}
%make_install install DESTDIR=%buildroot

# install operating system include directory
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/include/linux

# install libjvm.so directories
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/client
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{_arch}/server

# install tools.jar directory
install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib

pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/jre/lib
  for jarname in jaas jce jdbc-stdext jndi jndi-cos jndi-dns \
    jndi-ldap jndi-rmi jsse sasl
  do
    ln -s rt.jar $jarname.jar
  done
popd

rln %_bindir/fastjar %sdkbindir/jar
for i in appletviewer keytool jarsigner javah orbd rmic rmid rmiregistry serialver tnameserv; do
      	#rln %_bindir/gcj %sdkbindir/$i
	rln %_bindir/g$i %sdkbindir/$i
done

install -p -m755 altgcj/jdkgcj-notimpl.sh %buildroot%sdkbindir/notimpl
install -pD -m755 altgcj/rebuild-gcj-db %buildroot%_bindir/rebuild-gcj-db
install -pD -m755 altgcj/rebuild-gcj-db.filetrigger %buildroot/usr/lib/rpm/rebuild-gcj-db.filetrigger

mkdir -p %buildroot%java_home/man/man1
install -pm644 man/javac.1 %buildroot%java_home/man/man1/jdkgcj.1
for f in javac javah jar rmic; do
	ln -s jdkgcj.1 %buildroot%java_home/man/man1/"$f".1
done

gcj_target_libdir=`gcj -print-search-dirs |sed -ne 's|^install: \(/.*\)/$|\1|p'`
for f in java javax jvmpi.h; do
	rln "$gcj_target_libdir/include/$f" %java_home/include/
done

for i in extcheck idlj javap jdb native2ascii; do
	ln -snf notimpl %buildroot%sdkbindir/$i
done
%if_with sinjdoc
rln %_bindir/sinjdoc %sdkbindir/javadoc
%else
ln -snf notimpl %buildroot%sdkbindir/javadoc
%endif #sinjdoc

# jre dir and stuff
mkdir -p %buildroot%jrebindir
pushd %buildroot%sdkbindir
    for i in java \
    policytool servertool pack200 unpack200
    do 
     	 [ -e "$i" ] && ln -s ../../bin/$i %buildroot%jrebindir/
    done
popd

install -dm 755 $RPM_BUILD_ROOT%{_jvmjardir}

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
mkdir -p %buildroot%_libdir/gcj

# extensions handling
install -dm 755 $RPM_BUILD_ROOT%{jvmjardir}
for jarname in jaas jce jdbc-stdext jndi jndi-cos jndi-dns \
    jndi-ldap jndi-rmi jsse sasl
do
  rln %{_jvmdir}/%{jredir}/lib/$jarname.jar %{jvmjardir}/$jarname-%{version}.jar
done
pushd $RPM_BUILD_ROOT%{jvmjardir}
  for jar in *-%{version}.jar
  do
    ln -sf ${jar} $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
    ln -sf ${jar} $(echo $jar | sed "s|-%{version}.jar|.jar|g")
  done
popd
#ln -s %jppname-%version %buildroot%{_jvmjardir}/%jppname

# amd64 compatibility link
%ifarch x86_64
pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib
  ln -s %{_arch} amd64
popd
%endif

mkdir -p %buildroot%_altdir
# jre alternative
%__cat <<EOF >%buildroot%_altdir/%name-java
%{_bindir}/java	%{jrebindir}/java	%priority
%_man1dir/java.1.gz	%java_home/man/man1/java.1.gz	%{jrebindir}/java
EOF
# binaries and manuals
for i in keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  [ -L %buildroot%jrebindir"$i" ] || [ -e %buildroot%jrebindir"$i" ] && \
  %__cat <<EOF >>%buildroot%_altdir/%name-java
%_bindir/$i	%jrebindir/$i	%{jrebindir}/java
EOF
  [ -L %java_home/man/man1/$i.1.gz ] || [ -e %java_home/man/man1/$i.1.gz ] && \
  %__cat <<EOF >>%buildroot%_altdir/%name-java
%_man1dir/$i.1.gz	%java_home/man/man1/$i.1.gz	%{jrebindir}/java
EOF
done

# javac alternative and manual
cat <<EOF>%buildroot%_altdir/%name-javac
%_bindir/javac	%sdkbindir/javac	%priority
%_man1dir/javac.1.gz	%java_home/man/man1/javac.1.gz	%sdkbindir/javac
EOF
# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver apt jconsole jinfo jmap jps jsadebugd jstack jstat jstatd \
jhat jrunscript jvisualvm schemagen wsgen wsimport xjc \
HtmlConverter
do
  [ -L $RPM_BUILD_ROOT%sdkbindir/$i ] || [ -e $RPM_BUILD_ROOT%sdkbindir/$i ] && \
  %__cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%sdkbindir/$i	%sdkbindir/javac
EOF
  [ -L $RPM_BUILD_ROOT%sdkbindir/$i ] || [ -e $RPM_BUILD_ROOT%java_home/man/man1/$i.1.gz ] && \
  %__cat <<EOF >>%buildroot%_altdir/%name-javac
%_man1dir/$i.1.gz	%java_home/man/man1/$i.1.gz	%sdkbindir/javac
EOF
done
# ----- JPackage compatibility alternatives ------
  %__cat <<EOF >>%buildroot%_altdir/%name-javac
%{_jvmdir}/java	%java_home	%sdkbindir/javac
%{_jvmdir}/java-%{origin}	%java_home	%sdkbindir/javac
%{_jvmdir}/java-%{javaver}	%java_home	%sdkbindir/javac
EOF


######## triggerin(jre) converted #############
%__cat <<EOF >>%buildroot%_altdir/%name-jaxp_parser_impl
%{_javadir}/jaxp_parser_impl.jar	%{_javadir}/libgcj-%__gcc_version_base.jar	20
EOF

# rt.jar
rln %{_javadir}/libgcj-%__gcc_version_base.jar %{_jvmdir}/%{sdkdir}/jre/lib/rt.jar
# libjawt.so
rln %_libdir/gcj-%__gcc_version_base/libjawt.so \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/libjawt.so
# libjvm.so
rln %_libdir/gcj-%__gcc_version_base/libjvm.so \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/client/libjvm.so
rln %_libdir/gcj-%__gcc_version_base/libjvm.so \
    %{_jvmdir}/%{jredir}/lib/%{_arch}/server/libjvm.so

######## triggerin(devel) converted #############
# tools.jar
rln %{_javadir}/libgcj-tools-%__gcc_version_base.jar \
    %{_jvmdir}/%{sdkdir}/lib/tools.jar

# create symbolic links to headers in gcj's versioned directory
for headername in jawt jni
do
  DIRECTORY=$(dirname $(gcj-%__gcc_version_base \
    -print-file-name=include/$headername.h))
  rln $DIRECTORY/$headername.h \
    %{_jvmdir}/%{sdkdir}/include/$headername.h
done
for headername in jawt_md jni_md
do
  DIRECTORY=$(dirname $(gcj-%__gcc_version_base \
    -print-file-name=include/$headername.h))
  rln $DIRECTORY/$headername.h \
    %{_jvmdir}/%{sdkdir}/include/linux/$headername.h
done
######## end triggerin converted #############

# versioned gcj-dbtool. hack not to depend on alternatives.
subst s,%_bindir/gcj-dbtool,%_bindir/%_target_platform-gcj-dbtool-%__gcc_version_base,g %buildroot%_bindir/rebuild-gcj-db

%post -n %jppname
%_bindir/rebuild-gcj-db ||:

%files
#%files -n %jppname-devel
%_altdir/%name-javac
%{_jvmdir}/%{sdklnk}
%java_home/include
%java_home/lib
%java_home/bin/javadoc

%files -n %jppname
%dir %java_home
# tmp hack until jre/bin will be filled properly
%exclude %java_home/bin/javadoc
%java_home/bin
%java_home/jre
%java_home/man
%{_jvmdir}/%{jrelnk}
%_altdir/%name-java
%_altdir/%name-jaxp_parser_impl
%dir %_libdir/gcj
%_bindir/rebuild-gcj-db
/usr/lib/rpm/rebuild-gcj-db.filetrigger
%_jvmjardir/%jppname
%_jvmjardir/%sdkdir
%_jvmjardir/jre-%{javaver}-%{origin}

%changelog
* Wed May 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.9-alt2
- rebuilt with gcc-4.6

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.5.9-alt1
- Rebuilt with gcc-4.5.3.

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 0.5.8-alt1
- Rebuild with gcc-4.5.1

* Wed Oct 13 2010 Dmitry V. Levin <ldv@altlinux.org> 0.5.7-alt1
- Rebuilt with gcc-4.4.5.

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.5.6-alt1
- Rebuild with gcc-4.4.4

* Sun Mar 28 2010 Kirill A. Shutemov <kas@altlinux.org> 0.5.5-alt2
- Fix requires to avoid error on %%post

* Fri Jan 22 2010 Kirill A. Shutemov <kas@altlinux.org> 0.5.5-alt1
- Rebuild with gcc-4.4.3

* Tue Oct 27 2009 Kirill A. Shutemov <kas@altlinux.org> 0.5.4-alt1
- Rebuild with gcc-4.4.2
- Do not use sinjdoc on ARM

* Tue Aug 18 2009 Dmitry V. Levin <ldv@altlinux.org> 0.5.3-alt1
- Rebuilt with gcc-4.4.1.

* Mon Jun 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- java-1.5.0-gcj moved to separate package
- rebuild-gcj-db now depends on specific gcj.

* Wed May 27 2009 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1
- added extra system jars
- sdkdir is set to gcj default value

* Mon May 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- added Requires: libgcj-plugins
- now provides standard system jars too
- added Sun compatible lib hierarchy
- java-1.5.0-gcj, java-1.5.0-gcj-devel prepared

* Mon May 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- added Requires: libgcj-jar, for javac to work

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt3
- added java-1.5.0-gcj provides

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2
- added Requires: /proc (GC Warning: Couldn't read /proc/stat)

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- updated list of supported utils
- added implementation of javadoc using sinjdoc

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- those 4.x series are intermediate releases aimed to transform
  jdkgcj to fully JPackage compliant java-1.5.0-gcj.
- this 4.0 features:
  + added aot-compile support
  + added java-gcj-compat provides.
  + added %_libdir/gcj
  + added rebuild-gcj-db
  + added rebuild-gcj-db.filetrigger

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt17
- Rebuilt with gcc-4.4.0.

* Fri Nov 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt16
- added /usr/lib/jvm/java alternative

* Fri Nov 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt15
- rewritten alternatives to be compatible with java-*-sun ones.

* Thu Oct 30 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt14
- Fixed links: appletviewer keytool jarsigner.
- Fixed gcc-4.3+ support in java and javac wrappers.

* Wed Oct 22 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt13
- Rebuilt with gcc-4.3.2.

* Thu Oct 09 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt12
- Changed %%jdkgcj_home/bin/jar symlink to point to %_bindir/fastjar.

* Fri Feb 22 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt11
- Workaround old broken docbook-style-xsl.

* Thu Feb 21 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt10
- Rebuilt with gcc-4.1.2.

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt9
- Rebuilt with gcc-4.1.1.

* Fri May 12 2006 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt8
- Rebuilt with gcc-4.1.0.

* Thu Mar 09 2006 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt7
- Rebuilt with gcc-3.4.5.
- Updated build dependencies.

* Sat Oct 08 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt6
- Changed %%jdkgcj_home to /usr/lib/%name.
- Converted rest of absolute symlinks into relative.

* Sun Aug 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt5
- Simplified targets of %%jdkgcj_home/bin/{javah,jar,rmic} symlinks.

* Thu Jun 23 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt4
- Converted alternatives config file to new format (0.2.0).
- Rebuilt with gcc-3.4.4.
- Removed noarch tag.

* Tue Jan 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt3
- Fixed alternatives.
- Rebuilt with gcc-3.4.3.

* Wed Jun 16 2004 Stanislav Ievlev <inger@altlinux.org> 0.3.3-alt2.1
- NMU: move to new alternatives scheme

* Sun Mar 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.3-alt2
- Requires java-common

* Sat Jan 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.3-alt1
- Updated to the upstream release 0.3.3, using cues from spec by Arklinux
- Install a stub script for the executable JDK alternatives missing in jdkgcj
- Provide a manpage to override the JDK manpage alternatives and say something
  about jdkgcj

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt5
- Rebuilt with gcc-3.3.3

* Tue Dec 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt4
- Rebuilt with gcc-3.3.2

* Mon Jun 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt3
- Rebuilt with gcc-3.2.3

* Tue Nov 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt2
- Specfile cleanup.
- Use libgcj version in emulation scripts.
- Fixed tmp handling in java emulation.

* Mon Nov 11 2002 AEN <aen@altlinux.ru> 0.2.3-alt1
- first build (RH package)

* Mon Jul 29 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.2.3-1
- Adapt to gcc 3.2 (#69948)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 13 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.2.2-1
- Handle weirdo options like "-D ."

* Wed Jun 12 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.2.1-1
- Fix passing of parameters containing spaces or quotes to java
  applications.

* Fri May 31 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.2.0-1
- Replace the java->gij symlink with a script that translates
  java options to gij options (allowing stuff like
  java -classpath "/foo" -Djava.library.path=/bar some/sub/class
  to work)

* Fri May 31 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.1.1-1
- Fix up default location of gcj jar file

* Fri May 31 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.1.0-1
- Fix up -d support in javac. It must handle multiple classes per file.

* Fri May 31 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.0.2-1
- Add support for -d in javac

* Fri May 31 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.0.1-1
- initial RPM
