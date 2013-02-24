# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/guile /usr/bin/guile-config /usr/bin/indent guile18-devel libnlopt-devel libreadline-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
Name:           libctl
Version:        3.2.1
Release:        alt1_1
Summary:        Guile-based support for flexible control files

Group:          System/Libraries
# integrator.c and cintergrator.c contain code licensed under GPLv2+
# The rest of the code is LGPLv2+, but most restrictive license wins
# for the package.
License:        GPLv2+
URL:            http://ab-initio.mit.edu/wiki/index.php/Libctl
Source0:        http://ab-initio.mit.edu/libctl/libctl-%{version}.tar.gz
BuildRequires:  gcc-fortran guile-devel
Requires:       guile
Source44: import.info

%description
The libctl package is a Guile-based library that provides support for
flexible control files in scientific simulations.

%package devel
Summary:        Development files for libctl
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libctl.

%prep
%setup -q

%build
%configure F77=gfortran --enable-shared --disable-static \
  --includedir=%{_includedir}/ctl LDFLAGS='%{optflags} -lm'
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done

%files
%doc COPYING AUTHORS NEWS 
%{_libdir}/*.so.*

%files devel
%doc ChangeLog
%{_bindir}/gen-ctl-io
%{_includedir}/ctl
%{_libdir}/*.so
%{_mandir}/man1/*
%{_datadir}/libctl

%changelog
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

