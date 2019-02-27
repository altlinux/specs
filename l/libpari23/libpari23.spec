Group: System/Libraries
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libpari23
Version:	2.3.5
Release:	alt1_15
Summary:	Number Theory-oriented Computer Algebra Library
# No version is specified
License:	GPL+
URL:		http://pari.math.u-bordeaux.fr/
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/unix/OLD/2.3/pari-%{version}.tar.gz
Patch1:		libpari23-optflags.patch
Patch2:		libpari23-fsf-address.patch
Patch3:		Math-Pari-2.01080604-extra-stack-for-test.patch
Patch4:		pari-2.3.5-Fix-build-with-no-dot-in-INC.patch
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	perl-devel
BuildRequires:	perl(lib.pm)
BuildRequires:	readline-devel
BuildRequires:	sed
BuildRequires:	tex(tex)
BuildRequires:	tex(dvips)
BuildRequires:	gccmakedep imake lndir makedepend
%add_findreq_skiplist %{_datadir}/%name/*
%add_findreq_skiplist %{_datadir}/pari/PARI/*
Source44: import.info

%description
PARI is a widely used computer algebra system designed for fast computations in
number theory (factorizations, algebraic number theory, elliptic curves...),
but also contains a large number of other useful functions to compute with
mathematical entities such as matrices, polynomials, power series, algebraic
numbers, etc., and a lot of transcendental functions.

This is an old version of the library, for compatibility with applications and
library bindings that have not been migrated to the current stable release.

%package devel
Group: Development/Other
Summary:	Header files and libraries for PARI development
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Header files and libraries for PARI development with the old version 2.3.x
API.

%prep
%setup -q -n pari-%{version}

# Use our optflags, not upstream's
%patch1
sed -i -e 's|@OPTFLAGS@|%{optflags} -fPIC|' config/get_cc

# Update FSF address in copyright notices
%patch2 -p1

# perl-Math-Pari uses libpari23's test suite but needs more stack on some architectures
%patch3 -p2

# Fix build for Perls without '.' in @INC
%patch4

# Avoid unwanted rpaths
sed -i "s|runpathprefix='.*'|runpathprefix=''|" config/get_ld

# Fix up shellbangs
sed -i "s|@perl@|%{__perl}|" doc/gphelp.in misc/tex2mail.in

# Create a pkg-config file
cat > libpari23.pc << __EOF__
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}
datadir=%{_datadir}
paridir=%{_datadir}/%{name}

Name: Libpari23
Description: Number Theory-oriented Computer Algebra Library.
URL: http://pari.math.u-bordeaux.fr/
Version: %{version}
Libs: -lpari23
Cflags: -I\${includedir}/%{name}
__EOF__

%build
./Configure \
    --prefix=%{_prefix} \
    --share-prefix=%{_datadir} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir}/man1 \
    --datadir=%{_datadir}/pari \
    --without-gmp
%make_build all

%install
make install \
	DESTDIR=%{buildroot} \
	INSTALL="install -p" \
	STRIP=/bin/true

# we move pari.cfg to the docdir
rm -rf %{buildroot}%{_prefix}/lib/pari

# We'll link to this library as libpari23 rather than libpari
mv %{buildroot}%{_libdir}/libpari{.so,23.so}

# Move header files to avoid conflicting with pari-devel
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/{pari,%{name}/pari}

# Install tests and documentation, needed e.g. by perl-Math-Pari
mkdir -p %{buildroot}%{_datadir}/%{name}/src/
cp -a src/test/ %{buildroot}%{_datadir}/%{name}/src/
cp -a doc %{buildroot}%{_datadir}/%{name}/

# Additional headers needed e.g. by perl-Math-Pari
mkdir -p %{buildroot}%{_datadir}/%{name}/src/{graph,gp,headers,language}/
cp -a src/graph/*.h %{buildroot}%{_datadir}/%{name}/src/graph/
cp -a src/gp/*.h %{buildroot}%{_datadir}/%{name}/src/gp/
cp -a src/headers/*.h %{buildroot}%{_datadir}/%{name}/src/headers/
cp -a src/language/*.h %{buildroot}%{_datadir}/%{name}/src/language/

# Install our pkg-config file so the library can be found
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
cp -p libpari23.pc %{buildroot}%{_libdir}/pkgconfig/

# Remove emacs support files if built on a system with emacs
rm -rf %{buildroot}%{_datadir}/emacs/site-lisp/pari/

# Placate rpmlint regarding binary and library permissions
# %{_fixperms} %{buildroot}{%{_bindir},%{_libdir}}

%check
make dobench
make dotest-compat
make dotest-intnum
make dotest-qfbsolve
make dotest-rfrac
make dotest-round4



%files
%doc --no-dereference COPYING
%doc AUTHORS CHANGES* COMPAT NEW README
%doc Olinux-*/pari.cfg
%{_libdir}/libpari.so.%{version}
%{_libdir}/libpari.so.2

# Files for the pari-gp calculator, which we don't ship
%exclude %{_bindir}/gp
%exclude %{_bindir}/gp-2.3
%exclude %{_bindir}/gphelp
%exclude %{_bindir}/tex2mail
%exclude %doc %{_datadir}/pari/PARI/
%exclude %doc %{_datadir}/pari/doc/
%exclude %doc %{_datadir}/pari/examples/
%exclude %{_datadir}/pari/misc/
%exclude %{_datadir}/pari/pari.desc
%exclude %{_mandir}/man1/gp-2.3.1*
%exclude %{_mandir}/man1/gp.1*
%exclude %{_mandir}/man1/gphelp.1*
%exclude %{_mandir}/man1/pari.1*
%exclude %{_mandir}/man1/tex2mail.1*

%files devel
%{_includedir}/%{name}/pari/
%{_libdir}/libpari23.so
%{_libdir}/pkgconfig/libpari23.pc
%{_datadir}/%{name}/

%changelog
* Wed Feb 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_15
- to Sisyphus as perl-Math-Pari dep

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_11
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_10
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_9
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_8
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_7
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_4
- initial fc import

