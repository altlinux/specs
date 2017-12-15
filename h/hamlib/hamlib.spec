
Name:           hamlib
Version:        3.1
Release:        alt1.1.qa1.1
Summary:        Run-time library to control radio transceivers and receivers

Group:          System/Libraries
License:        GPLv2+ and LGPLv2+
URL:            http://hamlib.sourceforge.net
Source0:        %name-%version.tar

# Install python and perl bindings into proper dirs
Patch0:         hamlib-3.0-bindings.patch
BuildRequires:  gcc-c++
BuildRequires:  python-devel, swig, libgd2-devel, libxml2-devel, tcl-devel
BuildRequires:  libusb-devel, pkgconfig, boost-devel, libltdl3-devel
BuildRequires:  doxygen
BuildRequires:  perl-devel
BuildRequires:  libusb-compat-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program 'rigctl',
which lets one control a radio transceiver or receiver, either from
command line interface or in a text-oriented interactive interface.

%package devel
Summary: Development library to control radio transceivers and receivers
Group: Development/C
Requires: hamlib = %version-%release

%description devel
Hamlib radio control library C development headers and libraries
for building C applications with Hamlib.

%package doc
Summary: Documentation for the hamlib radio control library
Group: Documentation
BuildArch: noarch

%description doc
This package provides the developers documentation for the hamlib radio
control library API.

%package c++
Summary: Hamlib radio control library C++ binding
Group: System/Libraries
Requires: hamlib = %version-%release

%description c++
Hamlib radio control library C++ language binding.

%package c++-devel
Summary: Hamlib radio control library C++ binding development headers and libraries
Group: Development/C++
Requires: hamlib-devel = %version-%release
Requires: hamlib-c++ = %version-%release

%description c++-devel
Hamlib radio control library C++ binding development headers and libraries
for building C++ applications with Hamlib.


%package perl
Summary: Hamlib radio control library Perl binding
Group: Development/Perl
Requires: hamlib = %version-%release

%description perl
Hamlib PERL Language bindings to allow radio control from PERL scripts.

%package -n python-module-hamlib
Summary: Hamlib radio control library Python binding
Group: Development/Python
Provides: %name-python = %version-%release
Requires: hamlib = %version-%release

%description -n python-module-hamlib
Hamlib Python Language bindings to allow radio control from Python scripts.

%package tcl
Summary: Hamlib radio control library TCL binding
Group: Development/Tcl
Requires: hamlib = %version-%release

%description tcl
Hamlib TCL Language bindings to allow radio control from TCL scripts.

%prep
%setup -q
%autoreconf
%patch0 -p2

%build
%configure \
        --with-xml-support \
        --with-tcl-binding \
        --with-perl-binding \
        --with-python-binding \
        --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Build libs, drivers, and programs, won't build with smpflags
make
# Build Documentation
make -C doc doc

%install
%makeinstall_std
#install documentation
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/html/search
for f in `find doc/html/ -type f -maxdepth 1`
        do install -D -m 0644 $f $RPM_BUILD_ROOT%{_docdir}/%{name}/`echo $f | cut -d '/' -f2`
done
for f in `find doc/html/search -type f -maxdepth 1`
        do install -D -m 0644 $f $RPM_BUILD_ROOT%{_docdir}/%{name}/html/`echo $f | cut -d '/' -f3`
 done
# move installed docs to include them in subpackage via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv ${RPM_BUILD_ROOT}%{_docdir}/%{name}/* __tmp_doc

rm -f $RPM_BUILD_ROOT%{_libdir}/hamlib-*.a $RPM_BUILD_ROOT%{_libdir}/hamlib-*.la

find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

#fix permissions
find $RPM_BUILD_ROOT -type f -name Hamlib.so -exec chmod 0755 {} ';'

#remove this, not needed
find $RPM_BUILD_ROOT -type f -name pkgIndex.tcl -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name Hamlib.bs -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name perltest.pl -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog PLAN COPYING.LIB COPYING README THANKS TODO
%doc README.developer
%_bindir/*
%_libdir/libhamlib.so.*
%_man1dir/*
%_infodir/*

%files devel
%_libdir/libhamlib.so
%_datadir/aclocal/hamlib.m4
%dir %_includedir/hamlib
%_includedir/hamlib/rig.h
%_includedir/hamlib/riglist.h
%_includedir/hamlib/rig_dll.h
%_includedir/hamlib/rotator.h
%_includedir/hamlib/rotlist.h
%_libdir/pkgconfig/hamlib.pc

%files doc

%files c++
%_libdir/libhamlib++.so.*

%files c++-devel
%_libdir/libhamlib++.so
%_includedir/hamlib/rigclass.h
%_includedir/hamlib/rotclass.h

%files perl
%perl_vendorarch/*

%files -n python-module-hamlib
%python_sitelibdir/*.py*
%python_sitelibdir/_Hamlib.so

%files tcl
%_libdir/tcl/Hamlib/hamlibtcl*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1.1.qa1.1
- rebuild with new perl 5.26.1

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.1-alt1.1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1.1
- rebuild with new perl 5.24.1

* Tue Jan 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- new version 3.1

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1.1.1
- NMU: added BR: texinfo

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1.1
- rebuild with new perl 5.22.0

* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- New version

* Sun Dec 28 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.15.3-alt1
- Build for Sisyphus (thans Red Hat maintainers)

