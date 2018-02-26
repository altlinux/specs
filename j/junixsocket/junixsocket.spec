Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: java-devel-default


Name:           junixsocket
Version:        1.3
Release:        alt4
Summary:        Java/JNI library that allows the use of Unix Domain Sockets
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://junixsocket.googlecode.com/
Source0:        http://junixsocket.googlecode.com/files/%{name}-%{version}-src.tar.bz2
BuildRequires: jpackage-utils rpm-build-java ant ant-nodeps junit4 ant-junit

%description
junixsocket is a Java/JNI library that allows the use of Unix Domain Sockets (AF_UNIX sockets) from Java.

In contrast to other implementations, junixsocket extends the Java Sockets API (java.net.Socket, java.net.SocketAddress etc.) and even supports RMI over AF_UNIX. It is also possible to use it in conjunction with Connector/J to connect to a local MySQL server via Unix domain sockets.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q 
# bad biarch in alt...
#grep -v 'param name="gccM" value="-m32"' build.xml > build.xml.0
#mv build.xml.0 build.xml

%build
export LANG=en_US.ISO8859-1
export CLASSPATH=`build-classpath junit4`
%ifarch %ix86
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dskip64=true dist javadoc
%else
%ifarch x86_64
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dskip32=true dist javadoc
%else
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist javadoc
%endif
%endif

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/

install -m 644 dist/%{name}*-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}/

(cd $RPM_BUILD_ROOT%{_javadir}/%{name}/ && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

cp -pr javadoc/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

#see src/main/org/newsclub/net/unix/NativeUnixSocket.java
install -d $RPM_BUILD_ROOT%{_libdir}/
install -m 755 lib-native/libjunixsocket-linux*.so $RPM_BUILD_ROOT%{_libdir}/

%files
%{_javadir}/%{name}/*.jar
%{_libdir}/lib*.so*

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4
- fixed build with java7

* Fri May 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3
- fix thanks to manowar@

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2
- corrected files section

* Wed Sep 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- first build for Sisyphus
