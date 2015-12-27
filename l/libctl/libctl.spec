# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/guile /usr/bin/guile-config /usr/bin/indent guile18-devel libnlopt-devel libreadline-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
Group: System/Libraries
%add_optflags %optflags_shared
Name:           libctl
Version:        3.2.2
Release:        alt1_2
Summary:        Guile-based support for flexible control files
# integrator.c and cintergrator.c contain code licensed under GPLv2+
# The rest of the code is LGPLv2+, but most restrictive license wins
# for the package.
License:        GPLv2+
URL:            http://ab-initio.mit.edu/wiki/index.php/Libctl
Source0:        http://ab-initio.mit.edu/libctl/libctl-%{version}.tar.gz
Patch0:         0001-Add-check-for-sincos-function-from-libm-to-configure.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-fortran
BuildRequires:  guile-devel
BuildRequires:  libtool
Requires:       guile
Source44: import.info

%description
libctl is a Guile-based library that provides support for
flexible control files in scientific simulations.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
F77=gfortran              \
%configure                \
        --disable-rpath   \
        --enable-shared   \
        --disable-static  \
        --includedir=%{_includedir}/ctl

%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete -print
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done

%files
%doc COPYING COPYRIGHT
%{_libdir}/libctl*.so.*

%files devel
%doc AUTHORS NEWS
%doc doc/
%{_bindir}/gen-ctl-io
%{_includedir}/ctl/
%{_libdir}/libctl*.so
%{_mandir}/man1/gen-ctl-io.1*
%{_datadir}/libctl/

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_1
- update to new release by fcimport

* Tue Oct 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_1
- initial import by fcimport

