%add_optflags %optflags_shared
Name:           libsx
Summary:        Simple X library
Version:        2.05
Release:        alt3_20
Group:          System/Libraries
License:        LGPLv2+
Url:            ftp://ftp.ac-grenoble.fr/ge/Xlibraries/
Source:         ftp://ftp.ac-grenoble.fr/ge/Xlibraries/%{name}-%{version}.tar.bz2
# simpler example for freq
Source1:        libsx-simple_freq.c
Patch0:         libsx-no_nested_prototypes.diff
Patch1:         libsx-comment_caddr_t.diff
Patch2:         libsx-strdup.diff
Patch3:         libsx-examples.diff
Patch4:         libsx-link_mkdir.diff
Patch6:         libsx-rgb.diff
Patch7:         libsx-trunc.diff
# libXt-devel requires libX11-devel and libXaw-devel requires libXmu-devel
BuildRequires:  libXaw-devel libXpm-devel libXt-devel
Source44: import.info

%description
Libsx (the Simple X library) is a library of code that sits on top of and 
to the side of the Athena widget set.  Its purpose is to make writing X 
applications *much* easier.  

%package devel
Summary:       Headers and development libraries for libsx
Group:         Development/C
Requires:      %{name} = %{version}-%{release}
#Requires:      xorg-x11-devel

%description devel
Libsx (the Simple X library) is a library of code that sits on top of and
to the side of the Athena widget set.

The libsx-devel package contains headers and development libraries
necessary for building programs against libsx.


%prep
%setup -q
# static function cannot be within other function
%patch0 -p1
# don't redefine caddr_t
%patch1
# set strdup prototypes only if strdup isn't a macro
%patch2 -p1 -b .strdup
# use the new GetFile in freq, remove libsx.h from prerequisite and other
# fixes allowing examples to compile
%patch3 -p1 -b .examples
# use mkdir -p to create directories
# shared library with fine soname
# fix compile flags
%patch4 -p1 -b .link_mkdir
# allow the rgb file location to be redefined
%patch6 -p1 -b .rgb
# prevent clash with system trunc()
%patch7 -p1 -b .trunc

# example of a simple use of the new GetFile
cp -p %{SOURCE1} freq/simple_freq.c

%build
make CFLAGS="%{optflags} -fPIC -DRGBTXT=\"\\\"%{_datadir}/X11/rgb.txt\\\"\""

%install

pushd src
make install LIBDIR=%{buildroot}%{_libdir} \
      INCLUDEDIR=%{buildroot}%{_includedir} \
      SHAREDIR=%{buildroot}%{_datadir}/libsx \
      copyfile='cp -p'
popd
rm %{buildroot}%{_libdir}/libsx.a

# prepare examples directory
rm -rf __dist_examples
mkdir -p __dist_examples/examples
# pcurve doesn't build since it requires OPENGL_SUPPORT to be used, 
# and we don't use it, since it is maked as experimental.
example_dirs="bezier controlbox creq demo* draw_demo frac freq multireq skel xmore xrootbg" 
cp -a $example_dirs libsx_defs pcurve __dist_examples/examples/
# remove symlinks pointing to libsx.h in example directories
find __dist_examples/examples/ -name libsx.h -a -type l -exec rm \{\} \;
find __dist_examples/examples/ -name makefile.examples -exec rm \{\} \;
rm __dist_examples/examples/freq/freq.c.strdup
for dir in $example_dirs; do
  make -C __dist_examples/examples/$dir clean
done


# fix symbolic links for shared library. It is not completly obvious
# that using 0.0.0 like in libtool makes sense, do it anyway.
pushd %{buildroot}/%{_libdir}
mv libsx.so libsx.so.0.0.0
chmod +x libsx.so.0.0.0
ln -s libsx.so.0.0.0 libsx.so.0
ln -s libsx.so.0 libsx.so
popd

%files
%doc CHANGES HELP HINTS LICENSE README 
%{_libdir}/libsx.so.*
%{_datadir}/libsx/

%files devel
%doc docs/ __dist_examples/examples/
%{_libdir}/libsx.so
%{_includedir}/libsx.h

%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.05-alt3_20
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.05-alt2_20
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.05-alt2_19
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1_19
- initial import by fcimport

