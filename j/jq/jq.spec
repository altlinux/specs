%def_disable static
%def_disable docs
%define soname 1

Name: jq
%define lname lib%name
Version: 1.7.1
Release: alt2
Summary: Command-line JSON processor
Group: Development/Other
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Url: https://stedolan.github.io/jq/
VCS: https://github.com/stedolan/jq
License: BSD
Requires: %lname = %EVR

BuildRequires: flex  liboniguruma-devel
%{?!_disable_check:BuildRequires: /proc valgrind}

%description
%name is a command-line JSON processor.

%package -n %lname
Summary: %name shared library
Group: System/Libraries

%description -n %lname
%name shared library.

%package -n %lname-devel
Summary: Files for devel with %name library
Group: Development/C
Requires: %lname = %EVR

%description -n %lname-devel
Files for devel with %name library.

%if_enabled static
%package -n %lname-devel-static
Summary: %name static library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%name static library.
%endif

%prep
%setup
%patch0 -p1
rm scripts/version
printf "#!/bin/sh\necho %version\n" > scripts/version
chmod +x scripts/version

%build
%autoreconf
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--enable-shared \
	#
%make_build V=1

%install
%makeinstall_std docdir=%_docdir/%name-%version
ln -sf README.md %buildroot%_docdir/%name-%version/README

%check
export LD_LIBRARY_PATH=$PWD/.libs
%make_build check || :
cat ./test-suite.log

%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*

%files -n %lname
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files -n %lname-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/libjq.pc

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%changelog
* Sun Apr 28 2024 Anton Farygin <rider@altlinux.ru> 1.7.1-alt2
- removed ruby-tools from BuildRequires (fix FTBFS)

* Sat Dec 30 2023 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- 1.7 -> 1.7.1

* Wed Sep 13 2023 Anton Farygin <rider@altlinux.ru> 1.7-alt1
- 1.6 -> 1.7
- fixed URL

* Thu Nov 22 2018 Anton Farygin <rider@altlinux.ru> 1.6-alt2
- fixed build with --disable check 

* Mon Nov 05 2018 Anton Farygin <rider@altlinux.ru> 1.6-alt1
- 1.6

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt3
- security update (fixes: CVE-2016-4074)

* Thu Apr 05 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt2
- rebuilt for new liboniguruma

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.5-alt1
- new version with security fixes (CVE-2015-8863)

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.4-alt1
- 1.4
- added library subpackages

* Tue Nov 12 2013 Led <led@altlinux.ru> 1.3-alt2
- fixed build with new automake

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.3-alt1
- initial build
