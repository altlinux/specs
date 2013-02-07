# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:	Java GNOME bindings
Name:		java-gnome
Version:	4.1.1
Release:	alt1_5jpp7
URL:		http://java-gnome.sourceforge.net
Source0:	http://ftp.gnome.org/pub/gnome/sources/java-gnome/4.0/java-gnome-%{version}.tar.xz
# This is the "Classpath" exception.
License:	GPLv2 with exceptions
Group:		System/Libraries
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo-svg)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	gettext
BuildRequires:	junit
BuildRequires:	jpackage-utils
Requires:	jpackage-utils

# Java 1.7 compat.
# http://thread.gmane.org/gmane.comp.gnome.bindings.java.devel/1665/focus=1668
Patch0:		java-gnome-4.1.1-extendsboxed.patch
Source44: import.info
Patch33: java-gnome-4.1.1-alt-gcc.patch

%description
These are the Java bindings for GTK and GNOME! Featuring a robust 
engineering design, completely generated internals, a lovingly 
crafted layer presenting the public API, and steadily increasing 
coverage of the underlying libraries.

You can use java-gnome to develop sophisticated user interfaces 
for Linux applications so that they richly integrate with the 
GNOME Desktop while leveraging the power of the Java language 
and your expertise with it.

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch:	noarch

%description	javadoc
This package contains the API documentation for %%{name}, along with
design documentation and sample code.

%prep
%setup -q

%patch0 -p1

if find -name '*.class' -o -name '*.jar' | grep . >&2; then
    echo >&2 "Prebuilt binaries found in the sources. See https://fedoraproject.org/wiki/Packaging:Java#Pre-built_JAR_files_.2F_Other_bundled_software for instructions."
    exit 1
fi
%patch33 -p0

%build
# It'll get two conflicting --libdir parameters, but the last one
# happens to win which is what we want.
%configure --jardir=%{_libdir}/%{name} --libdir=%{_libdir}/%{name}

# The build system does not support parallell builds, so no
# _smp_mflags.
make V=1 build-java doc

%install

mkdir -p %{buildroot}%{_javadir}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_javadocdir}
cp -rp doc/api %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc README NEWS LICENCE
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.jar
%{_libdir}/%{name}/*.so

%files javadoc
# Note that not all here is javadoc. Two subpackages for documentation
# seems silly.
%doc doc/design doc/examples
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_5jpp7
- initial build

