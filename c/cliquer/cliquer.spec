# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define fontpkgname cliquer
%define soname 1

Name: cliquer
Version: 1.22
Release: alt2

Summary: Find cliques in arbitrary weighted graphs

License: GPL-2.0+
Group: Engineering
Url: https://users.aalto.fi/~pat/cliquer.html

Source: https://github.com/dimpase/autocliquer/releases/download/v%version/%name-%version.tar.gz
Source1: http://users.aalto.fi/~pat/%name/%{name}_fm.pdf
Source2: http://users.aalto.fi/~pat/%name/%name.pdf
Source3: http://users.aalto.fi/~pat/%name/%{name}_bm.pdf
# Man page formatting by Jerry James, text from the sources
Source4: %name.1
Source44: import.info

Requires: lib%name%soname = %version-%release

BuildRequires: gcc

%description
The main cliquer package contains a command-line interface to the
cliquer library.  Note that the upstream binary name is "cl", which is
too generic for Fedora.  Therefore, the binary is named "cliquer".

%package -n lib%name%soname
Group: System/Libraries
Summary: Library to find cliques in arbitrary weighted graphs
Provides: %name-libs = %version-%release

%description -n lib%name%soname
Cliquer is a set of C routines for finding cliques in an arbitrary
weighted graph.  It uses an exact branch-and-bound algorithm developed
by Patric A.stergA.rd.  It is designed with the aim of being efficient
while still being flexible and easy to use.

%package -n lib%name-devel
Group: Development/Other
Summary: Development files for cliquer
Provides: %name-devel = %version-%release

%description -n lib%name-devel
Development files for cliquer.

%prep
%setup

cp -p %SOURCE1 %SOURCE2 %SOURCE3 .

sed -i \
    's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    COPYING

%build
%configure --disable-static --disable-silent-rules

# Get rid of undesirable hardcoded rpaths.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build

%install
%makeinstall_std

# Add missing executable bit
chmod 0755 %buildroot%_libdir/libcliquer.so.%{soname}.*

# We do not want the libtool archive
rm %buildroot%_libdir/*.la

# We do not want to install the examples
rm -fr %buildroot%_datadir/%name

# The name "cl" is very short and ambiguous
mv %buildroot%_bindir/cl %buildroot%_bindir/%name

# Install the man page
mkdir -p %buildroot%_man1dir
cp -p %SOURCE4 %buildroot%_man1dir

%check
LD_LIBRARY_PATH=. make test

%files
%doc cliquer*.pdf
%_bindir/%name
%_man1dir/*

%files -n lib%name%soname
%doc ChangeLog README
%doc --no-dereference COPYING
%_libdir/libcliquer.so.%{soname}*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/libcliquer.so

%changelog
* Wed Nov 10 2021 Leontiy Volodin <lvol@altlinux.org> 1.22-alt2
- Initial build for ALT Sisyphus (from autoimports).
- Applied SharedLibsPolicy.
- Built as require for sagemath.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.22-alt1_2
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.22-alt1_1
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.21-alt2_20
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.21-alt2_19
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_19
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_18
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_17
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_16
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_15
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_13
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_11
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_10
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_9
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_7
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_6
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_5
- initial fc import

