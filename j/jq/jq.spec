%def_enable shared
%def_enable static
%def_disable docs

Name: jq
%define lname lib%name
Version: 1.4
Release: alt1
Summary: Command-line JSON processor
Group: Development/Other
Source: %name-%version.tar
Patch: %name-%version-%release.patch
URL: http://stedolan.github.io/jq/
License: BSD-style
%{?_enable_shared:Requires: %lname = %version-%release}

BuildRequires: flex %{?!_disable_check:/proc valgrind}

%description
%name is a command-line JSON processor.


%if_enabled shared
%package -n %lname
Summary: %name shared library
Group: System/Libraries

%description -n %lname
%name shared library.
%endif


%package -n %lname-devel
Summary: Files for devel with %name library
Group: Development/C
%{?_disable_shared:BuildArch: noarch}
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

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
%setup -q
%patch -p1


%build
%autoreconf
%configure \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable docs}
%make_build V=1


%install
%makeinstall_std docdir=%_docdir/%name-%version
ln -sf README.md %buildroot%_docdir/%name-%version/README


%check
%make_build check


%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Sun Jun 15 2014 Led <led@altlinux.ru> 1.4-alt1
- 1.4
- added library subpackages

* Tue Nov 12 2013 Led <led@altlinux.ru> 1.3-alt2
- fixed build with new automake

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.3-alt1
- initial build
