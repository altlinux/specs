Name: libefx
Version: 1.11.99
Release: alt1.git.4.g1792af5

Summary: Auxiliary Enlightenment library
License: LGPL2
Group: System/Libraries
Url: https://git.enlightenment.org/devs/discomfitor/efx.git/commit/

# GIT https://git.enlightenment.org/devs/discomfitor/efx.git/commit/
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 02 2016
# optimized out: efl-libs fontconfig gnu-config libgpg-error pkg-config
BuildRequires: efl-libs-devel

%description
A library for 2D effects

%package -n %name-devel
Summary: Development files for libefx
Group: Development/C
PreReq: %name = %version-%release
License: LGPL2

%description -n %name-devel
This package contains development files required for packaging
libefx-based software.

%prep
%setup

%build
./autogen.sh \
	--prefix=%_prefix \

%make_build

%install
%makeinstall
rm %buildroot%_bindir/*

%files
#%%exclude %_bindir/*
%_libdir/%name.so.*
%_datadir/efx
%doc AUTHORS TODO

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 02 2016 Ildar Mulyukov <ildar@altlinux.ru> 1.11.99-alt1.git.4.g1792af5
- initial build for ALT Linux Sisyphus

