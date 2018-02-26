%define sover 0
Name: tamu_anova
Version: 0.2
Release: alt2
Summary: ANOVA Extensions to the GNU Scientific Library
License: GPL v2
Group: Sciences/Other
Url: http://www.stat.tamu.edu/~aredd/tamuanova/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.stat.tamu.edu/~aredd/tamuanova/tamu_anova-0.2.tar.gz

BuildPreReq: libgsl-devel

%description
ANOVA, or Analysis of Variance, is a method for comparing levels of some
continuous response variable between different groups. The main idea is
to compare variation within each group to variation between the groups;
if the groups vary considerably from one group to another in comparison
to the within group variation, we can reject the null hypothesis that
all the groups have similar levels of the response variable.

%package -n libtamuanova
Summary: Shared library of TAMU ANOVA
Group: System/Libraries

%description -n libtamuanova
ANOVA, or Analysis of Variance, is a method for comparing levels of some
continuous response variable between different groups. The main idea is
to compare variation within each group to variation between the groups;
if the groups vary considerably from one group to another in comparison
to the within group variation, we can reject the null hypothesis that
all the groups have similar levels of the response variable.

This package contains shared library of TAMU ANOVA.

%package -n libtamuanova-devel
Summary: Development files of TAMU ANOVA
Group: Development/C
Requires: libtamuanova = %version-%release

%description -n libtamuanova-devel
ANOVA, or Analysis of Variance, is a method for comparing levels of some
continuous response variable between different groups. The main idea is
to compare variation within each group to variation between the groups;
if the groups vary considerably from one group to another in comparison
to the within group variation, we can reject the null hypothesis that
all the groups have similar levels of the response variable.

This package contains development files of TAMU ANOVA.

%prep
%setup

%build
./autogen.sh
%add_optflags %optflags_shared
%configure
%make_build

%install
%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

pushd %buildroot%_libdir
LIB=libtamuanova
gcc -shared -Wl,--whole-archive $LIB.a -Wl,--no-whole-archive \
	-o $LIB.so.%sover -Wl,-soname,$LIB.so.%sover -lgsl -Wl,-z,defs
ln -s $LIB.so.%sover $LIB.so
rm -f $LIB.a
popd

%files -n libtamuanova
%doc NEWS README
%_libdir/*.so.*

%files -n libtamuanova-devel
%_libdir/*.so
%_includedir/*
%_infodir/*

%changelog
* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

