Name: mingw32-w32api-bootstrap
Version: 3.13
Release: alt1
Summary: Win32 header files and stubs

License: Public Domain
Group: Development/Other
Url: http://www.mingw.org/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://dl.sourceforge.net/sourceforge/mingw/w32api-%version-mingw32-dev.tar.gz

BuildArch: noarch

Requires: mingw32-runtime

BuildRequires: rpm-build-mingw32

Provides: mingw32-w32api

%description
MinGW Windows cross-compiler Win32 header files.

%prep
%build
%install
mkdir -p %buildroot%_mingw32_prefix
cd %buildroot%_mingw32_prefix
tar -xzf %SOURCE0

%files
%_mingw32_includedir/*
%_mingw32_libdir/*.a

%changelog
* Fri Jul 17 2009 Boris Savelev <boris@altlinux.org> 3.13-alt1
- initial build

