# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/valgrind gcc-c++ imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libfreetype-devel libreadline-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip zlib-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
Name:           libctl
Version:        3.1
Release:        alt2_2
Summary:        Guile-based support for flexible control files

Group:          System/Libraries
# integrator.c and cintergrator.c contain code licensed under GPLv2+
# The rest of the code is LGPLv2+, but most restrictive license wins
# for the package.
License:        GPLv2+
URL:            http://ab-initio.mit.edu/wiki/index.php/Libctl
Source0:        http://ab-initio.mit.edu/libctl/libctl-%{version}.tar.gz
BuildRequires:  gcc-fortran guile18-devel
Requires:       guile18
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
for i in %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin}/*; do
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
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_1
- initial import by fcimport

