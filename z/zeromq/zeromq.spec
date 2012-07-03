Name: zeromq
Version: 2.1.11
Release: alt1
Summary: a software library that lets you quickly design and implement a fast message-based application

Group: System/Libraries
License: LGPL
Url: http://www.zeromq.org

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: gcc-c++ libuuid-devel glib2-devel
Requires: lib%name = %version-%release

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging patterns,
message filtering (subscriptions), seamless access to multiple transport
protocols and more.
This package contains 0mq binaries

%package -n lib%name
Group: System/Libraries
Summary: a software library that lets you quickly design and implement a fast message-based application

%description -n lib%name
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging patterns,
message filtering (subscriptions), seamless access to multiple transport
protocols and more.
This package contains 0mq library

%package -n lib%name-devel
Group: Development/C++
Summary: a software library that lets you quickly design and implement a fast message-based application
Requires: lib%name = %version-%release

%description -n lib%name-devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging patterns,
message filtering (subscriptions), seamless access to multiple transport
protocols and more.
This package contains 0mq library headers

%prep
%setup -q

%build
%autoreconf
%configure --with-pgm --with-pic --with-gnu-ld --disable-static
%make_build

%install
%makeinstall_std

%check
make check

%files -n lib%name
%_libdir/libzmq.so.*
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS README
%_man7dir/zmq.7*

%files -n lib%name-devel
%_includedir/zmq*
%_libdir/libzmq.so
%_pkgconfigdir/libzmq.pc
%_man3dir/zmq_*3*
%_man7dir/zmq_*7*

%changelog
* Sat Jan 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.11-alt1
- New version 2.1.11
- add make check
- Remove subpackage %name

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.10-alt1
- New version 2.0.10

* Sun Sep 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.9-alt1
- New version 2.0.9

* Fri Sep 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.8-alt1
- New version 2.0.8

* Fri Jun 18 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.7-alt1
- initial build

