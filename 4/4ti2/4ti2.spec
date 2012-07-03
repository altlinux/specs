# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           4ti2
Version:        1.3.2
Release:        alt3_11
Summary:        A software package for problems on linear spaces

Group:          System/Libraries
License:        GPLv2+
URL:            http://www.4ti2.de/
Source0:        http://www.4ti2.de/version_%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.4ti2.de/4ti2_manual.pdf
Source2:        4ti2.module.in
Patch0:         4ti2-1.3.2-gcc47.patch
Requires:       environment-modules
BuildRequires:  libgmp-devel libgmp_cxx-devel
BuildRequires:  libglpk-devel
Source44: import.info

%description
A software package for algebraic, geometric and combinatorial
problems on linear spaces.

This package uses Environment Modules, to load the binaries onto
your PATH you will need to run module load %{name}-%{_arch}

%prep
%setup -q
cp -p %{SOURCE1} .
%patch0 -p1 -b .gcc47

%build
CXXFLAGS="%{optflags} -I%{_includedir}/glpk" \
CFLAGS="%{optflags} -I%{_includedir}/glpk" \
./configure --disable-shared --disable-static \
            --prefix=%{_libdir}/%{name} \
            --libdir=%{_libdir}/%{name}/lib/ \
            --bindir=%{_libdir}/%{name}/bin/
perl -pi -e 's|hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=\"-L\\\$libdir\"|g;' libtool

make %{?_smp_mflags}

%install
make install-exec DESTDIR=%{buildroot}

# Make the environment-modules file
mkdir -p %{buildroot}%{_datadir}/Modules/modulefiles/
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#'%{_libdir}/%{name}'#g;' < %SOURCE2 >%{buildroot}%{_datadir}/Modules/modulefiles/%{name}-%{_arch} 

# The libraries are not really fit for use outside the package.
rm -rf %{buildroot}/%{_libdir}/%{name}/lib*

%check
make check

%files
%doc COPYING TODO 4ti2_manual.pdf
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}
%{_datadir}/Modules/modulefiles/%{name}-%{_arch} 
%{_libdir}/%{name}/bin/output
%{_libdir}/%{name}/bin/4ti2gmp
%{_libdir}/%{name}/bin/4ti2int32
%{_libdir}/%{name}/bin/4ti2int64
%{_libdir}/%{name}/bin/circuits
%{_libdir}/%{name}/bin/genmodel
%{_libdir}/%{name}/bin/gensymm
%{_libdir}/%{name}/bin/graver
%{_libdir}/%{name}/bin/groebner
%{_libdir}/%{name}/bin/hilbert
%{_libdir}/%{name}/bin/markov
%{_libdir}/%{name}/bin/minimize
%{_libdir}/%{name}/bin/normalform
%{_libdir}/%{name}/bin/ppi
%{_libdir}/%{name}/bin/qsolve
%{_libdir}/%{name}/bin/rays
%{_libdir}/%{name}/bin/walk
%{_libdir}/%{name}/bin/zbasis
%{_libdir}/%{name}/bin/zsolve

%changelog
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

