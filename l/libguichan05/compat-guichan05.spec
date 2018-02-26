# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/allegro-config /usr/bin/sdl-config gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname compat-guichan05
Name:           libguichan05
Version:        0.5.0
Release:        alt1_12
Summary:        Compatibility libraries for older guichan versions

Group:          Development/C++
License:        BSD
URL:            http://guichan.sourceforge.net
Source0:        http://downloads.sourceforge.net/guichan/guichan-%{version}-src.tar.gz
Obsoletes:      guichan < 0.6.0

BuildRequires:  liballegro-devel libSDL-devel libSDL_image-devel libGL-devel
BuildRequires:  libfreeglut-devel
Source44: import.info
Provides: guichan05 = %{version}-%{release}
Patch33: guichan-0.5.0-alt-underlinkage.patch
%set_verify_elf_method unresolved=relaxed

%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different objects for 
displaying graphics and grabbing user input.

This package contains compatibility libraries for guichan 0.5

%package devel
Summary:        Header and libraries for guichan development
Group:          Development/C++
Requires:       libguichan05 = %{version}-%{release}
Provides: guichan05-devel = %{version}-%{release}

%description devel
This package includes header and libraries files for development using
guichan, a small and efficient C++ GUI library designed for games. This
package is needed to build programs written using guichan.

%prep
%setup -q -n guichan-%{version}-src
%patch33 -p1

%build
autoreconf -fisv
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Removing Libtool and static archives
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# Move some things around for the compat package
mkdir -p $RPM_BUILD_ROOT%{_includedir}/guichan-0.5
mv $RPM_BUILD_ROOT%{_includedir}/guichan $RPM_BUILD_ROOT%{_includedir}/guichan-0.5
mv $RPM_BUILD_ROOT%{_includedir}/guichan.hpp $RPM_BUILD_ROOT%{_includedir}/guichan-0.5

mkdir -p $RPM_BUILD_ROOT%{_libdir}/guichan-0.5
for lib in libguichan libguichan_allegro libguichan_glut libguichan_opengl libguichan_sdl ; do
    rm -f $RPM_BUILD_ROOT%{_libdir}/${lib}.so
    ln -s ../${lib}.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/guichan-0.5/${lib}.so
done


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libguichan.so.*
%{_libdir}/libguichan_allegro.so.*
%{_libdir}/libguichan_glut.so.*
%{_libdir}/libguichan_opengl.so.*
%{_libdir}/libguichan_sdl.so.*

%files devel
%doc docs/html
%{_includedir}/guichan-0.5
%dir %{_libdir}/guichan-0.5
%{_libdir}/guichan-0.5/libguichan.so
%{_libdir}/guichan-0.5/libguichan_allegro.so
%{_libdir}/guichan-0.5/libguichan_glut.so
%{_libdir}/guichan-0.5/libguichan_opengl.so
%{_libdir}/guichan-0.5/libguichan_sdl.so


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_12
- update to new fc release

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_11
- initial release by fcimport

