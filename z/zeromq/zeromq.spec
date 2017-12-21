%def_without pgm

Name: zeromq
Version: 4.2.3
Release: alt1

Summary: a software library that lets you quickly design and implement a fast message-based application
Group: System/Libraries
License: GPLv3, LGPLv3
Url: http://www.zeromq.org

Source: %name-%version.tar
Source1: https://raw.githubusercontent.com/zeromq/cppzmq/master/zmq.hpp
Source2: https://raw.githubusercontent.com/zeromq/cppzmq/master/LICENSE

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: gcc-c++ libuuid-devel glib2-devel asciidoc xmlto
%{?_with_pgm:BuildRequires: libopenpgm-devel}

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

%package -n lib%name-cpp-devel
Summary: Development files for cppzmq
Group: Development/C++
License: MIT
Requires: lib%name-devel = %version-%release

%description -n lib%name-cpp-devel
This package contains files for developing C++ %name applications.

%prep
%setup
cp -a %SOURCE2 .

%build
%autoreconf
%configure --disable-static \
	--with-pic \
	--with-gnu-ld \
	%{subst_with pgm}

%make_build

%install
%makeinstall_std
install -m644 -p %SOURCE1 %buildroot%_includedir/

%check
%make check

%files -n lib%name
%_libdir/libzmq.so.*
%doc AUTHORS ChangeLog NEWS
%_man7dir/zmq.7*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/libzmq.so
%_pkgconfigdir/libzmq.pc
%_man3dir/zmq_*3*
%_man7dir/zmq_*7*

%files -n lib%name-cpp-devel
%_includedir/zmq.hpp
%doc LICENSE

%changelog
* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.3-alt1
- Updated to upstream version 4.2.3.

* Fri Jan 27 2017 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0
- new lib%%name-cpp-devel subpackage

* Wed Apr 13 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 4.0.5-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.5-alt1
- Version 4.0.5

* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2.2-alt1
- New version 3.2.2

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

