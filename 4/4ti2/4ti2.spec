Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: swig
# END SourceDeps(oneline)
BuildRequires(pre): rpm-macros-environment-modules
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           4ti2
Version:        1.6.9
Release:        alt1_12
Summary:        Algebraic, geometric and combinatorial problems on linear spaces

%global relver %(tr . _ <<< %{version})

# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in the PDF manual.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# CM-Super: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later
URL:            https://4ti2.github.io/
Source0:        https://github.com/4ti2/4ti2/releases/download/Release_%{relver}/%{name}-%{version}.tar.gz
Source1:        4ti2.module.in
# Deal with a boolean variable that can somehow hold the value 2
Patch0:         %{name}-maxnorm.patch

BuildRequires:  environment(modules)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libglpk-devel
BuildRequires:  libgmp-devel libgmpxx-devel
BuildRequires:  tex(latex)
BuildRequires:  tex(epic.sty)

# 4ti2 contains a copy of gnulib, which has been granted a bundling exception:
# https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides
Provides:       bundled(gnulib)

Requires:       4ti2-libs = %{version}-%{release}
Requires:       environment(modules)
Source44: import.info

%description
A software package for algebraic, geometric and combinatorial problems
on linear spaces.

This package uses Environment Modules.  Prior to invoking the binaries,
you must run "module load 4ti2-%%{_arch}" to modify your PATH.

%package devel
Group: System/Libraries
Summary:        Headers needed to develop software that uses 4ti2
Requires:       4ti2-libs = %{version}-%{release}

%description devel
Headers and library files needed to develop software that uses 4ti2.

%package libs
Group: System/Libraries
Summary:        Library for problems on linear spaces

%description libs
A library for algebraic, geometric and combinatorial problems on linear
spaces.

%prep
%setup -q
%patch0


# Add a missing executable bit
chmod a+x ltmain.sh

# Fix encodings
iconv -f ISO8859-1 -t UTF-8 NEWS > NEWS.utf8
touch -r NEWS NEWS.utf8
mv -f NEWS.utf8 NEWS

# Update the C++ standard
sed -i 's/c++0x/c++11/g' configure

# Silence "egrep is obsolescent" warnings
for f in $(grep -Frl egrep src/groebner test); do
  sed -i.orig 's/egrep/grep -E/g' $f
  touch -r $f.orig $f
  rm $f.orig
done

%build
%configure --enable-shared --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Build the manual
export LD_LIBRARY_PATH=$PWD/src/4ti2/.libs:$PWD/src/fiber/.libs:$PWD/src/groebner/.libs:$PWD/src/ppi/.libs:$PWD/src/util/.libs:$PWD/src/zsolve/.libs
pushd doc
make update-manual
bibtex 4ti2_manual
pdflatex -interaction=batchmode 4ti2_manual
pdflatex -interaction=batchmode 4ti2_manual
popd

%install
%makeinstall_std

# Move the include files into a private directory
mkdir -p %{buildroot}%{_includedir}/tmp
mv %{buildroot}%{_includedir}/{4ti2,groebner,util,zsolve} \
   %{buildroot}%{_includedir}/tmp
mv %{buildroot}%{_includedir}/tmp %{buildroot}%{_includedir}/4ti2

# Move the 4ti2 binaries
mkdir -p %{buildroot}%{_libdir}/4ti2
mv %{buildroot}%{_bindir} %{buildroot}%{_libdir}/4ti2

# Make the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#'%{_libdir}/4ti2'#g;' < %SOURCE1 >%{buildroot}%{_modulesdir}/4ti2-%{_arch}

# We don't need or want libtool files
rm -f %{buildroot}%{_libdir}/*.la

# We don't want documentation in _datadir
rm -fr %{buildroot}%{_datadir}/4ti2/doc

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check

%files
%doc doc/4ti2_manual.pdf
%{_libdir}/4ti2/
%{_modulesdir}/4ti2-%{_arch}

%files devel
%{_includedir}/4ti2/
%{_libdir}/lib4ti2*.so
%{_libdir}/libzsolve*.so

%files libs
%doc NEWS README THANKS TODO
%doc --no-dereference COPYING
%{_libdir}/lib4ti2*.so.0*
%{_libdir}/libzsolve*.so.0*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.6.9-alt1_12
- update to new release by fcimport

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_7
- fixed build

* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_4
- update to new release by fcimport

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_2
- new version

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_0
- new version (manual update)

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt3_13
- update to new release by fcimport

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt3_12.1
- Rebuilt with glpk 4.48

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt3_12
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt3_11
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt3_8
- rebuild to get rid of #27020

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt2_8
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt2_7.1
- update to new release by fcimport

* Mon Nov 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_7.1
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_7
- converted from Fedora by srpmconvert script

