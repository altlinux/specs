# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: unzip
%add_optflags %optflags_shared
Name:           libnoise
Version:        1.0.0
Release:        alt3_6
Summary:        A general-purpose library that generates three-dimensional coherent noise

Group:          System/Libraries
License:        LGPLv2+
URL:            http://libnoise.sourceforge.net/
Source0:        http://download.sourceforge.net/libnoise/libnoisesrc-%{version}.zip
Patch0:         libnoise-make.patch

BuildRequires:  libtool
BuildRequires:  doxygen
Source44: import.info


%description
libnoise is a portable C++ library that is used to generate coherent
noise, a type of smoothly-changing noise. libnoise can generate Perlin
noise, ridged multifractal noise, and other types of coherent-noise.

Coherent noise is often used by graphics programmers to generate
natural-looking textures, planetary terrain, and other things.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}


%description    doc
The %{name}-doc package contains documentation for developing
applications that use %{name}.


%prep
%setup -q -c -n noise

# The contents of the upstream zip file are a file called COPYING.txt
# and a directory called 'noise' with the source.  We don't want to
# pollute the buildroot, so everything goes in a subdirectory and we
# cd into the noise directory to build and install.

cd noise
%patch0 -p0
# add libtool tag
sed -i 's,\(--mode=\(compile\|link\)\) \$(\(CC\|CXX\)),--tag=\3 &,' `find . -name Makefile`



%build
cd noise/src

# The makefile seems somewhat broken.  If 'make' is run in the root
# directory first, libnoise.a isn't generated.

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"

cd ..
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"


%install

sed -i 's/\r//' COPYING.txt

cd noise

# make install does not work.

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/noise
cp doc/htmldata/*png doc/html
cp doc/htmldata/*css doc/html

sed -i 's/\r//' doc/html/doxygen.css

rm include/Makefile

mkdir -p $RPM_BUILD_ROOT/%{_includedir}/noise/
cp -R include/* $RPM_BUILD_ROOT/%{_includedir}/noise/

mkdir -p $RPM_BUILD_ROOT/%{_libdir}
cp lib/libnoise.so.0.3 $RPM_BUILD_ROOT/%{_libdir}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
ln -sf libnoise.so.0.3 $RPM_BUILD_ROOT/%{_libdir}/libnoise.so.0.3.0
ln -sf libnoise.so.0.3 $RPM_BUILD_ROOT/%{_libdir}/libnoise.so
ln -sf libnoise.so.0.3 $RPM_BUILD_ROOT/%{_libdir}/libnoise.so.0


%files
%doc COPYING.txt
%{_libdir}/*.so.*


%files devel
%{_includedir}/noise/
%{_libdir}/*.so


%files doc
%doc noise/doc/html


%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_6
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5
- initial import by fcimport

