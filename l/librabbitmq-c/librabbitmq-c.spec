Name:           librabbitmq-c
Version:        0.0.1
Release:        alt1
Summary:        This is a C-language AMQP client library for use with AMQP servers speaking protocol versions 0-9-1
Group:          System/Libraries
License:        MIT
URL:            http://hg.rabbitmq.com/rabbitmq-c/
Source:        %name-%version.tar

BuildRequires: python-module-simplejson libpopt-devel xmlto

%description
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.

%package	devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%_bindir/*
%_man1dir/*
%_man7dir/*
%_libdir/librabbitmq.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.1-alt1
- first build for ALT Linux
