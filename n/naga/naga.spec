# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global svnrel 82

Name:           naga
Version:        3.0
Release:        alt1_1.82svnjpp7
Summary:        Simplified Java NIO asynchronous sockets

Group:        	System/Base
License:        MIT
URL:            http://code.google.com/p/naga/
# Upstream does not release stable source tarballs.
# Tarball created with
# svn checkout -r %{svnrel} http://naga.googlecode.com/svn/trunk/ naga
# rm -rf naga/.svn
# tar jcf naga-%{svnrel}svn.tar.bz2 naga
Source0:        naga-%{svnrel}svn.tar.bz2
# Force utf8
Patch0:		naga-encoding.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant

Requires:       jpackage-utils
Source44: import.info

%description
Naga aims to be a very small NIO library that provides a handful of
java classes to wrap the usual Socket and ServerSocket with
asynchronous NIO counterparts (similar to NIO2 planned for Java 1.7).

All of this is driven from a single thread, making it useful for both
client (e.g. allowing I/O to be done in the AWT-thread without any
need for threads) and server programming (1 thread for all connections
instead of 2 threads/connection).

Internally Naga is a straightforward NIO implementation without any
threads or event-queues thrown in, it is "just the NIO-stuff", to let
you build things on top of it.

Naga contains the code needed to get NIO up and running without having
to code partially read buffers and setting various selection key
flags.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .encoding

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
ant build javadoc

%install
mkdir -p %{buildroot}%{_javadir}
install -D -p -m 644 -t %{buildroot}%{_javadir}/ _DIST/naga-3_0.jar 

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp _BUILD/docs/api/* %{buildroot}%{_javadocdir}/%{name}

# Install symlink
ln -s naga-3_0.jar %{buildroot}%{_javadir}/naga.jar

%files
%{_javadir}/naga-3_0.jar
%{_javadir}/naga.jar

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_1.82svnjpp7
- new version

