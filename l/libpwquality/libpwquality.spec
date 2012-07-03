%define _name pwquality

Name: lib%_name
Version: 1.1.0
Release: alt1

Summary: A library for password generation and password quality checking
License: BSD or GPL+
Group: System/Libraries
Url: https://fedorahosted.org/%name/

Source: http://fedorahosted.org/releases/l/i/%name/%name-%version.tar.bz2

Provides: pam_%_name = %version-%release
Requires: cracklib-words pam
BuildRequires: cracklib-devel pam-devel python-devel

%description

This is a library for password quality checks and generation of random
passwords that pass the checks.

This library uses the cracklib and cracklib dictionaries to perform some
of the checks.

%package devel
Group: Development/C
Summary: Files needed for developing PAM-aware applications and modules for PAM
Requires: %name = %version-%release

%description devel
Files needed for development of applications using the libpwquality
library.

See the pwquality.h header file for the API.

%package -n python-module-%_name
Group: Development/Python
Summary: Python bindings for the libpwquality library
Requires: %name = %version-%release

%description -n python-module-%_name
This is pwquality Python module that provides Python bindings
for the libpwquality library. These bindings can be used
for easy password quality checking and generation of random
pronounceable passwords from Python applications.


%prep
%setup

%build
%configure \
	--with-securedir=%_pam_modules_dir \
	--with-pythonsitedir=%python_sitelibdir \
	--disable-static

%make_build

%install
%makeinstall_std

# relocate %name.so.1 to %_lib
mkdir -p %buildroot/%_lib
mv %buildroot/%_libdir/%name.so.1* %buildroot/%_lib/
ln -sf ../../%_lib/%name.so.1 %buildroot%_libdir/%name.so

%find_lang %name

%check
%make check

%files -f libpwquality.lang
%_bindir/pwmake
%_bindir/pwscore
%_pam_modules_dir/pam_pwquality.so
/%_lib/%name.so.*
%config(noreplace) %_sysconfdir/security/%_name.conf
%_man1dir/*
%_man5dir/*
%_man8dir/*
%doc COPYING README NEWS AUTHORS

%exclude %_pam_modules_dir/*.la

%files devel
%_includedir/%_name.h
%_libdir/%name.so
%_pkgconfigdir/%_name.pc

%files -n python-module-%_name
%python_sitelibdir/%_name.so

%changelog
* Wed Jun 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus

