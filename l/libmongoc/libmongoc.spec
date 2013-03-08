Name: libmongoc
Version: 0.7.1
Release: alt1
Summary: C Driver for MongoDB
Group: System/Libraries
License: ASL 2.0
Url: https://github.com/mongodb/mongo-c-driver
Source: %name-%version.tar

BuildRequires: python-module-sphinx-devel doxygen

%description
This is then 10gen-supported MongoDB C driver. There are two goals for this driver.
The first is to provide a strict, default compilation option for ultimate portability, no dependencies, and generic embeddability.
The second is to support more advanced, platform-specific features, like socket timeout, by providing an interface for platform-specific modules.
Until the 1.0 release, this driver should be considered alpha. Keep in mind that the API will be in flux until then.

%package devel
Group: Development/C
Summary: C Driver for MongoDB
%description devel
This is then 10gen-supported MongoDB C driver. There are two goals for this driver.
The first is to provide a strict, default compilation option for ultimate portability, no dependencies, and generic embeddability.
The second is to support more advanced, platform-specific features, like socket timeout, by providing an interface for platform-specific modules.
Until the 1.0 release, this driver should be considered alpha. Keep in mind that the API will be in flux until then.

%prep
%setup

%build
%make_build
%make docs

%install
%makeinstall_std INSTALL_INCLUDE_PATH=%buildroot%_includedir INSTALL_LIBRARY_PATH=%buildroot%_libdir

%check
#make test

%files
%doc README.md HISTORY.md APACHE-2.0.txt docs/html
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Mar 08 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- Biuld fot ALT
