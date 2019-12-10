%set_verify_elf_method relaxed
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	Java bindings for the OpenGL API
Epoch:		1
Name:		jogl
Version:	1.1.1
Release:	alt1_13jpp8
Group:		Development/Java
License:	BSD
URL:		http://jogl.dev.java.net/
Source0:	https://jogl.dev.java.net/files/documents/27/17108/%{name}-%{version}-src.zip
Source1:	%{name}.properties
Patch0:		%{name}-1.1.1-src-no-link-against-sun-java.patch
Patch1:		%{name}-1.1.1-fix-gluegen-properties.patch
Patch2:		%{name}-1.1.1-fix-antlr-classpath.patch
BuildRequires:	ant
BuildRequires:	ant-antlr
BuildRequires:	antlr
BuildRequires:	jpackage-utils
BuildRequires:	unzip
BuildRequires:	xml-commons-apis
BuildRequires:	cpptasks
BuildRequires:	pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:	libEGL-devel
BuildRequires:	libGL-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(freeglut)
#BuildRequires:	mesaglesv1-devel
BuildRequires:	libglvnd-devel
BuildRequires:	libXxf86vm-devel
Requires:	java >= 1.5
ExclusiveArch:	%{ix86} x86_64
Source44: import.info

%description 
The JOGL Project hosts a reference implementation of the Java bindings for
OpenGL API, and is designed to provide hardware-supported 3D graphics to
applications written in the Java programming language.

It is part of a suite of open-source technologies initiated bu the Game
Technology Group at Sun Microsystems.

JOGL provides full access to the APIs in the OpenGL 1.5 specification as
well as nearly all vendor extensions, and integrated with the AWT and Swing
widget sets.

%package javadoc
Summary:	Javadoc for jogl
Group:		Development/Java

%description javadoc
Javadoc for jogl.

%package manual
Summary:	User documetation for jogl
Group:		Development/Java
BuildArch: noarch

%description manual
Usermanual for jogl.


%prep
rm -rf gluegen
%setup -q -n %{name}
pushd make
%patch0 -p0
popd
(
cd ../gluegen/
%patch1 -p1
%patch2 -p1
)

cp %{SOURCE1} make

%build
export OPT_JAR_LIST="antlr ant/antlr"
export CLASSPATH=$(build-classpath antlr ant/ant-antlr)

pushd make
perl -pi -e 's@/usr/X11R6/%{_lib}@%{_libdir}@g' build.xml

%ant \
    -Duser.home=%{_topdir}/SOURCES \
    -Dantlr.jar=$(build-classpath antlr) \
    -Dc.compiler.debug=true \
    all \
    javadoc.dev.x11

popd

%install
# jars
install -dm 755 %{buildroot}%{_javadir}
install -m 644 build/%{name}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

# native lib
install -dm 755 %{buildroot}%{_libdir}
install -m 744 build/obj/lib*.so \
	%{buildroot}%{_libdir}

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr javadoc_jogl_dev/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink
for rpm404_ghost in %{_javadocdir}/%{name}
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


%post javadoc
%__rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%attr(755,root,root) %{_libdir}/libjogl.so
%attr(755,root,root) %{_libdir}/libjogl_awt.so

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc doc/*


%changelog
* Tue Dec 10 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1_13jpp8
- new version
