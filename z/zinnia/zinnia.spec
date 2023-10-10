BuildRequires: chrpath
%add_optflags %optflags_shared
Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-python3
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		zinnia
Version:	0.06
Release:	alt1_66
Summary:	Online handwriting recognition system with machine learning

License:	BSD-3-Clause
URL:		http://zinnia.sourceforge.net/
Source0:	http://downloads.sourceforge.net/zinnia/%{name}-%{version}.tar.gz
Source1:	http://zinnia.svn.sourceforge.net/viewvc/zinnia/zinnia/tomoe2s.pl
Source2:	Makefile.tomoe
Patch0:		zinnia-0.05-bindings.patch
Patch1:		zinnia-0.06-fixes-ppc-float.patch
Patch2:		always-store-data-in-little-endian-format.patch
Patch3:		zinnia-fixes-gcc6-compile.patch
BuildRequires:	gcc-c++
BuildRequires:	libdb6-devel, python3-devel
BuildRequires:	swig
BuildRequires:	perl-devel
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	tomoe
BuildRequires:	autoconf
BuildRequires:	gnome-common
BuildRequires:	python3-module-pkg_resources python3-module-setuptools
Source44: import.info

%description
Zinnia provides a simple, customizable, and portable dynamic OCR
system for hand-written input, based on Support Vector Machines.

Zinnia simply receives user pen strokes as coordinate data and outputs
the best matching characters sorted by SVM confidence. To maintain
portability, it has no rendering functionality. In addition to
recognition, Zinnia provides a training module capable of creating
highly efficient handwriting recognition models.

This package contains the shared libraries.

%package -n libzinnia0
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n libzinnia0
Zinnia provides a simple, customizable, and portable dynamic OCR
system for hand-written input, based on Support Vector Machines.

Zinnia simply receives user pen strokes as coordinate data and outputs
the best matching characters sorted by SVM confidence. To maintain
portability, it has no rendering functionality. In addition to
recognition, Zinnia provides a training module capable of creating
highly efficient handwriting recognition models.

This package contains the shared libraries.

This package contains the shared library.

%package        -n libzinnia-devel
Group: Development/C
Summary:	Development files for %{name}
Requires:	libzinnia0 = %EVR
Provides: %name-devel = %EVR

%description    -n libzinnia-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package 	utils
Group: Development/C
Summary:	Utils for the zinnia library
Requires:	libzinnia0 = %EVR

%description	utils
The %{name}-utils package provides utilities for zinnia library that 
use %{name}.

%package 	doc
Group: Development/C
Summary:	Documents for the zinnia library
Requires:	libzinnia0 = %EVR
BuildArch:	noarch

%description	doc
The %{name}-doc package provide documents for zinnia library that 
use %{name}.

%package  	perl
Group: Development/C
Summary:	Perl bindings for %name
Requires:	libzinnia0 = %EVR


%description 	perl
This package contains perl bindings for %{name}.

%package 	-n python3-module-zinnia
Group: Development/C
%{?python_provide:%python_provide python3-zinnia}
Summary:	Python bindings for %{name}
Requires:	libzinnia0 = %EVR

%description 	-n python3-module-zinnia
This package contains python bindings for %{name}.

%package	tomoe-ja
Group: Development/C
Summary:        Japanese tomoe model file for %{name}
Requires:       libzinnia0 = %EVR
Provides:       zinnia-tomoe = %{version}-%{release}
Obsoletes:      zinnia-tomoe < 0.06-19

%description	tomoe-ja
This package contains Japanese tomoe model files for %{name}.

%package	tomoe-zh_CN
Group: Development/C
Summary:        Simplified Chinese tomoe model file for %{name}
Requires:       libzinnia0 = %EVR
Provides:       zinnia-tomoe = %{version}-%{release}
Obsoletes:      zinnia-tomoe < 0.06-19

%description	tomoe-zh_CN
This package contains Simplified Chinese tomoe model files for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0  -p1 -b .bindings
%patch1  -p1 -b .ppc
%patch2  -p1 -R -b .little-endian
%patch3  -p1 -b .gcc6

find . -type f -name "*.pyc" -exec rm -f {} ';'
cp %{SOURCE1} .
cp %{SOURCE2} .
pushd doc
iconv -f latin1 -t utf8 zinnia.css > zinnia.css.bak 
mv -f zinnia.css.bak zinnia.css
popd

# re-generate zinnia.py and zinnia_wrap.cxx for python 3.x
pushd swig
make python
popd

%build
gnome-autogen.sh
%configure --disable-static --disable-rpath
make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %{?_smp_mflags}
make -f Makefile.tomoe build

pushd perl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build
popd

pushd python
CFLAGS="$RPM_OPT_FLAGS -I../" LDFLAGS="$RPM_LD_FLAGS -L../.libs" python3 setup.py build
popd

%install
make install DESTDIR=$RPM_BUILD_ROOT
make -f Makefile.tomoe install DESTDIR=$RPM_BUILD_ROOT

pushd perl
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
popd

pushd python
python3 setup.py install --root $RPM_BUILD_ROOT

#the following line fixes RHBZ#2048104
rm -rf $RPM_BUILD_ROOT%{python3_sitelibdir}/zinnia_python-0.0.0-py%{__python3_version}.egg-info
pushd

#remove something unnecessary
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.bs" -size 0c -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

#change the privilege of some files
chmod 0755 $RPM_BUILD_ROOT%{perl_vendor_archlib}/auto/%{name}/%{name}.so


chrpath -d %buildroot%{perl_vendor_archlib}/auto/%{name}/*.so




%files -n libzinnia0
%doc README COPYING
%_libdir/libzinnia.so.0
%_libdir/libzinnia.so.0.*

%files -n libzinnia-devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%{_libdir}/pkgconfig/%{name}.pc

%files utils
%{_bindir}/zinnia
%{_bindir}/zinnia_convert
%{_bindir}/zinnia_learn

%files doc
%doc doc/*

%files	perl
%{perl_vendor_archlib}/auto/%{name}/
%{perl_vendor_archlib}/%{name}.pm

%files	-n python3-module-zinnia
%{python3_sitelibdir}/_%{name}.*.so
%{python3_sitelibdir}/%{name}*
%{python3_sitelibdir}/__pycache__/*

%files tomoe-ja
%dir %{_datadir}/zinnia/model/tomoe/
%{_datadir}/zinnia/model/tomoe/handwriting-ja.model

%files tomoe-zh_CN
%dir %{_datadir}/zinnia/model/tomoe/
%{_datadir}/zinnia/model/tomoe/handwriting-zh_CN.model

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.06-alt1_66
- update to new release by fcimport

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 0.06-alt1_60
- new version

