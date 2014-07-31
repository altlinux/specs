# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/valgrind gcc-c++ perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/File.pm) perl(Test.pm) perl(XSLoader.pm) perl-devel perl-podlators pkgconfig(lua) valgrind-devel
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		sigar
Version:	1.6.5
Release:	alt1_0.8.git58097d9jpp7
Summary:	System Information Gatherer And Reporter

%global sigar_suffix  0-g4b67f57
%global sigar_hash    58097d9

Group:		System/Libraries
License:	ASL 2.0
URL:		http://sigar.hyperic.com/

# Once 1.6.5 is released, we can use tarballs from GitHub:
#    Source0:	http://download.github.com/hyperic-sigar-{name}-{version}-{sigar_suffix}.tar.gz
#
# Until then the tarball can be re-generated with:
#    git clone git://github.com/hyperic/sigar.git
#    cd sigar
#    git archive --prefix=sigar-1.6.5/ 833ca18 | bzip2 > sigar-1.6.5-833ca18.tbz2
#
# The diff from 1.6.4 is too huge to contemplate cherrypicking from
Source0:	%{name}-%{version}-%{sigar_hash}.tbz2


BuildRequires:	gcc ctest cmake

Patch100: bz714249-1-cpu-count.patch
Patch101: bz746288-1-cpu-count-arch.patch
Source44: import.info

%description
The Sigar API provides a portable interface for gathering system
information such as:
- System memory, swap, CPU, load average, uptime, logins
- Per-process memory, CPU, credential info, state, arguments,
  environment, open files
- File system detection and metrics
- Network interface detection, configuration info and metrics
- Network route and connection tables

This information is available in most operating systems, but each OS
has their own way(s) providing it. SIGAR provides developers with one
API to access this information regardless of the underlying platform.

#The core API is implemented in pure C with bindings currently
#implemented for Java, Perl and C#.

%package devel 
License:	ASL 2.0
Group:		Development/Java
Summary:	SIGAR Development package - System Information Gatherer And Reporter
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for developing against the Sigar API

%prep
# When using the GitHub tarballs, use:
# setup -q -n hyperic-{name}-{sigar_hash}
%setup -q -n %{name}-%{version}

%patch100 -p1 -b .bz714249
%patch101 -p1 -b .bz746288

%build

# Fix lib directory
sed -i.sed s:DESTINATION\ lib:DESTINATION\ %{_lib}: src/CMakeLists.txt

mkdir build
pushd build
%{fedora_cmake} ..
make %{?_smp_mflags}
popd

%install
pushd build
%{fedora_cmake} ..
make install DESTDIR=$RPM_BUILD_ROOT
popd

%files
%doc ChangeLog README LICENSE NOTICE AUTHORS
%{_libdir}/libsigar.so

%files devel
%{_includedir}/sigar*.h
%doc LICENSE NOTICE AUTHORS

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1_0.8.git58097d9jpp7
- new release

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1_0.7.git58097d9jpp7
- new release

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt2_1jpp6
- fixed build

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_1jpp6
- new version

