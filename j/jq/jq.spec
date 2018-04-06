%def_disable static
%def_disable docs

Name: jq
%define lname lib%name
Version: 1.5
Release: alt2%ubt
Summary: Command-line JSON processor
Group: Development/Other
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Url: http://stedolan.github.io/jq/
License: BSD-style
Requires: %lname = %EVR

BuildRequires: flex  liboniguruma-devel
BuildRequires: %{?!_disable_check:/proc valgrind ruby-tools}
BuildRequires(pre):rpm-build-ubt

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
%_libdir/*.so.*

%files -n %lname-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%changelog
* Thu Apr 05 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt2%ubt
- rebuilt for new liboniguruma

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.5-alt1%ubt
- new version with security fixes (CVE-2015-8863)

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.4-alt1
- 1.4
- added library subpackages

* Tue Nov 12 2013 Led <led@altlinux.ru> 1.3-alt2
- fixed build with new automake

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.3-alt1
- initial build
