
Name: libmongo-client
Version: 0.1.6.1
Release: alt1

Summary: Alternative C driver for MongoDB
License: %asl
Group: System/Libraries
Url: https://github.com/algernon/libmongo-client
Source: %name-%version.tar
# git://github.com/algernon/libmongo-client.git

BuildPreReq: rpm-build-licenses
BuildRequires: pkgconfig(glib-2.0) >= 2.12.0
BuildRequires: graphviz
BuildRequires: doxygen fonts-ttf-liberation

%description
Alternative C driver for MongoDB. Libmongo-client is meant
to be a stable (API, ABI and quality alike), clean, well documented
and well tested shared library, that strives to make the most
common use cases as convenient as possible.

%package devel
Summary: Development files for libmongo-client
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files (libraries and include files) for libmongo-client

%package doc
Summary: Documentation for libmongo-client
Group: Documentation
BuildArch: noarch

%description doc
Subpackage contains documentation for libmongo-client

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build
%make doxygen

%install
%makeinstall

%files
%doc LICENSE NEWS README.rst
%_libdir/%name.so.*

%files devel
%_pkgconfigdir/*.pc
%_libdir/%name.so
%_includedir/*

%files doc
%doc docs/html

%changelog
* Thu Dec 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.6.1-alt1
- initial build
