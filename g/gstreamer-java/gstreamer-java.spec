# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 18
%global arch_with_swt %{ix86} x86_64 ppc ppc64 ia64 sparc sparc64
BuildArch: noarch

Summary:	Java interface to the gstreamer framework
Name:		gstreamer-java
Version:	1.5
Release:	alt1_4jpp7
License:	LGPLv3 and CC-BY-SA
Group:		System/Libraries
URL:		http://code.google.com/p/gstreamer-java/
# zip -r ~/rpm/SOURCES/gstreamer-java-src-1.5.zip gstreamer-java -x \*/.svn*
Source:		http://gstreamer-java.googlecode.com/files/%{name}-src-%{version}.zip
Patch1:		gstreamer-java-swt.patch
#Patch2:	gstreamer-java-osx.patch
Patch3:		gstreamer-java-nameClash.patch
Patch10:	gstreamer-java-1.5.patch
# for ExcludeArch and no noarch see bug: 468831
# since noarch pacakge can't contain ExcludeArch :-( imho it's an rpm bug
ExcludeArch:	ppc ppc64

# Don't build debuginfo packages since it's actualy a noarch package
%global debug_package %{nil}

Requires:	jpackage-utils jna
Requires:	gstreamer gst-plugins-base gst-plugins-good
BuildRequires:	jpackage-utils jna
BuildRequires:	gstreamer-devel gst-plugins-devel gst-plugins-good
BuildRequires:	ant ant-junit
%if 0%{?fedora} >= 9 || 0%{?rhel} > 5
BuildRequires:	junit4
%endif
%ifarch %{arch_with_swt} noarch
BuildRequires:	jna-contrib
%if 0%{?fedora} >= 9 || 0%{?rhel} > 5
BuildRequires:	eclipse-swt
%else
BuildRequires:	libswt3-gtk2
%endif
%endif
Source44: import.info

%description
An unofficial/alternative set of java bindings for the gstreamer multimedia
framework.

%ifarch %{arch_with_swt} noarch
%package swt
Summary:	SWT support for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
BuildRequires:	jna-contrib
%if 0%{?fedora} >= 9 || 0%{?rhel} > 5
BuildRequires:	eclipse-swt
%else
BuildRequires:	libswt3-gtk2
%endif

%description swt
This package contains SWT support for %%{name}.
%endif
%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.


%prep
%setup -q -n %{name}
%ifarch %{arch_with_swt} noarch
%patch1 -p1 -b .swt
#upstreamed
#%patch2 -p1 -b .osx
%patch10 -p1 -b .15
%patch3 -p2

# replace included jar files with the system packaged version SWT
sed -i -e "s,\(file.reference.swt.jar=\).*,\1$(find %{_libdir} -name swt*.jar 2>/dev/null|sort|head -1)," \
	nbproject/project.properties
%endif
cp -p src/org/freedesktop/tango/COPYING COPYING.CC-BY-SA

# remove prebuild binaries
find . -name '*.jar' -delete

# replace included jar files with the system packaged version (JNA, SWT, GStreamer plugins dir)
sed -i -e "s,\(file.reference.jna.jar=\).*,\1$(build-classpath jna)," \
	-e "s,\(file.reference.platform.jar=\).*,\1$(build-classpath jna/platform.jar)," \
	-e "s,\(run.jvmargs=-Djna.library.path=\).*,\1%{_libdir}:$(pkg-config --variable=pluginsdir gstreamer-0.10)," \
	nbproject/project.properties

# from Fedora-9 we've got ant-1.7.0 and junit4 while on older releases and EPEL
# have only ant-1.6.5 and junit-3.8.2 therefore on older releases and EPEL we
# have small hacks like ant-1.6.5 need packagenames for javadoc task
# and test targets need ant-1.7.x and junit4 so we skip the test during packaging
%if 0%{?fedora} >= 9 || 0%{?rhel} > 5
sed -i -e "s,\(file.reference.junit4.jar=\).*,\1$(build-classpath junit4)," \
	nbproject/project.properties
%else
sed -i -e 's,\(<javadoc destdir="${dist.javadoc.dir}" source="${javac.source}"\),\1 packagenames="*",' \
	build.xml
%endif
%build
ant jar javadoc


%if 0%{?fedora} >= 9 || 0%{?rhel} > 5
%check
#ant test
%endif


%install
mkdir -p -m0755 %{buildroot}%{_javadir}
install -m 0644  dist/*.jar	%{buildroot}%{_javadir}

mkdir -p -m0755 %{buildroot}%{_javadocdir}/%{name}
cp -rp dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/%{name}.jar
%doc CHANGES COPYING* tutorials/*
%ifarch %{arch_with_swt} noarch
%files swt
%{_javadir}/%{name}-swt.jar
%endif

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_4jpp7
- initial build

