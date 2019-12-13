%define sname qpid-cpp
%define perftests "qpid-perftest qpid-topic-listener qpid-topic-publisher qpid-latency-test qpid-client-test qpid-txtest"
%define _libexecdir %_prefix/libexec

# disable build bindings
%def_disable perl
%def_enable python
%def_disable ruby
%def_enable rdma

Name: qpid
Version: 1.39.0
Release: alt2
Summary: Libraries for Qpid C++ client applications
License: ASL 2.0
Url: http://qpid.apache.org
Group: System/Servers

%define _pkgdocdir %_docdir/%name-%version

Source0: %name-%version.tar

Source11: qpidd.service
Source12: qpidd-primary.service
Source13: qpidd.tmpfiles
Source21: qpidd.init
Source22: qpidd-primary.init

BuildRequires: gcc-c++
BuildRequires: cmake rpm-macros-cmake
BuildRequires: boost-devel
BuildRequires: doxygen
%{?_enable_perl:BuildRequires: swig perl-devel}
%{?_enable_python:BuildRequires: swig python-devel python-module-setuptools}
%{?_enable_ruby:BuildRequires: swig ruby ruby-stdlibs}
BuildRequires: ruby
BuildRequires: libsasl2-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libuuid-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
#BuildRequires: libxqilla-devel
#BuildRequires: libxerces-c-devel
BuildRequires: libaio-devel
BuildRequires: libqpid-proton-devel >= 0.26.0
BuildRequires: libdb4-devel
BuildRequires: libdb4_cxx-devel
%{?_enable_rdma:BuildRequires: rdma-core-devel}

%description
Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.

%package -n libqpid
Summary: Libraries for Qpid C++ client applications
Group: System/Libraries

%description -n libqpid
Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.

%package -n libqpid-devel
Summary: Header files, documentation and testing tools for developing Qpid C++ clients
Group: Development/C++

%description -n libqpid-devel
Libraries, header files and documentation for developing AMQP clients
in C++ using Qpid.  Qpid implements the AMQP messaging specification.

%package -n libqmf2
Summary: Qpid Management Framework library
Group: System/Libraries

%description  -n libqmf2
Qpid Management Framework library

%package -n libqmf2-devel
Summary: Header files, documentation and testing tools for developing Qpid Management Framework
Group: Development/C++

%description -n libqmf2-devel
Libraries, header files and documentation for developing AMQP clients
in C++ using Qpid.  Qpid implements the AMQP messaging specification.

%package client
Summary: Libraries for Qpid C++ client applications
Group: Networking/Other

%description client
Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.

%package client-tests
Summary: Test tools for developing Qpid C++ clients
Group: Networking/Other

%description client-tests
Test tools for developing Qpid C++ clients.

%package client-devel-docs
Summary: AMQP client development documentation
Group: Development/Documentation
BuildArch: noarch

%description client-devel-docs
This package includes the AMQP clients development documentation in HTML
format for easy browsing.

%package server
Summary: An AMQP message broker daemon
Group: System/Servers
Requires: cyrus-sasl2

%description server
A message broker daemon that receives stores and routes messages using
the open AMQP messaging protocol.

%package server-ha
Summary: Provides extensions to the AMQP message broker to provide high availability
Group: System/Servers

%description server-ha
Provides extensions to the AMQP message broker to provide high availability.

%package -n qpid-tools
Summary: Management and diagostic tools for Apache Qpid
Group: Networking/Other

%description -n qpid-tools
Management and diagnostic tools for Apache Qpid brokers and clients.

%package client-rdma
Summary: RDMA Protocol support (including Infiniband) for Qpid clients
Group: Networking/Other
Requires: %name-client = %version-%release

%description client-rdma
A client plugin and support library to support RDMA protocols (including
Infiniband) as the transport for Qpid messaging.

%package server-rdma
Summary: RDMA Protocol support (including Infiniband) for the Qpid daemon
Group: System/Servers
Requires: %name-client-rdma = %version-%release
Requires: %name-server = %version-%release

%description server-rdma
A Qpid daemon plugin to support RDMA protocols (including Infiniband) as the
transport for AMQP messaging.

%package server-xml
Summary: XML extensions for the Qpid daemon
Group: System/Servers
Requires: %name-server = %version-%release

%description server-xml
A Qpid daemon plugin to support extended XML-based routing of AMQP
messages.

%package server-store
Summary: Persistence extension to the Qpid messaging system
Group: System/Servers
License: LGPLv2+
Requires: %name-server = %version-%release

%description server-store
Persistence extension to the Qpid AMQP broker: persistent message
storage using either a libaio-based asynchronous journal, or synchronously
with Berkeley DB.

%package server-linearstore
Summary: Persistence extension to the Qpid messaging sytem
Group: System/Servers
License: LGPLv2+
Requires: %name-server = %version-%release

%description server-linearstore
Persistence extension to the Qpid AMQP broker: persistent message
storage using a libaio-based asynchronous journal.

%package -n perl-qpid_messaging
Summary: Qpid Perl Language Bindings
Group: Development/Perl

%description -n perl-qpid_messaging
Qpid Perl Language Bindings

%package -n python-module-qpid_messaging
Summary: Python bindings for the Qpid messaging framework
Group: Development/Python

%description -n python-module-qpid_messaging
Python bindings for the Qpid messaging framework

%package -n python-module-qmf
Summary: Python bindings for qmf
Group: Development/Python

%description -n python-module-qmf
Python bindings for qmf.

%package -n python-module-qmfgen
Summary: Python bindings for qmfgen
Group: Development/Python
BuildArch: noarch

%description -n python-module-qmfgen
Python bindings for qmfgen.

%prep
%setup

# replace generic python in shebangs with versioned python
find . -type f | xargs sed -i \
	-e 's:!/usr/bin/python$:!/usr/bin/python%_python_version:' \
	-e 's:!/usr/bin/env python$:!/usr/bin/env python%_python_version:' \
	%nil

%build
%cmake_insource \
	-DENABLE_WARNINGS:BOOL=OFF \
	-DENABLE_WARNING_ERROR:BOOL=OFF \
	-DDOC_INSTALL_DIR:PATH=%_pkgdocdir \
	%{?_disable_python:-DBUILD_BINDING_PYTHON:BOOL=OFF} \
	%{?_disable_ruby:-DBUILD_BINDING_RUBY:BOOL=OFF} \
	%{?_disable_perl:-DBUILD_BINDING_PERL:BOOL=OFF} \
	-DBUILD_LEGACYSTORE=false \
	-DBUILD_LINEARSTORE=true

%make_build
%make docs-user-api

%install
mkdir -p -m0755 %buildroot{%_bindir,%_unitdir,%_initdir,%_tmpfilesdir}

pushd management/python
%__python setup.py install \
    --install-purelib %python_sitelibdir \
    --root %buildroot
popd

%makeinstall_std

# install files
install -pm 644 %SOURCE11 %buildroot%_unitdir/qpidd.service
install -pm 644 %SOURCE12 %buildroot%_unitdir/qpidd-primary.service
install -pm 644 %SOURCE13 %buildroot%_tmpfilesdir/qpidd.conf

install -pm 755 %SOURCE21 %buildroot%_initdir/qpidd
install -pm 755 %SOURCE22 %buildroot%_initdir/qpidd-primary


# install perftests utilities
pushd src/tests
for ptest in %perftests; do
  libtool --mode=install install -m755 $ptest %buildroot/%_bindir
done
popd

mkdir -p %buildroot/%_runtimedir/qpidd
mkdir -p %buildroot/%_localstatedir/qpidd

#cleanup
rm -f %buildroot%_bindir/*.bat

%pre server
%_sbindir/groupadd -r -f qpidd 2>/dev/null ||:
%_sbindir/useradd -r -g qpidd  -c 'Owner of Qpidd Daemons' \
        -s /sbin/nologin  -d %_localstatedir/qpidd qpidd 2>/dev/null ||:

%post server
%post_service qpidd

%preun server
%preun_service qpidd

%post server-ha
%post_service qpidd-primary

%preun server-ha
%preun_service qpidd-primary

%files -n libqpid
%_libdir/libqpidcommon.so.*
%_libdir/libqpidclient.so.*
%_libdir/libqpidtypes.so.*
%_libdir/libqpidmessaging.so.*

%files -n libqpid-devel
%_libdir/*.so
%exclude %_libdir/liblinearstoreutils.so
%exclude %_libdir/libqpidbroker.so
%exclude %_libdir/libqmf2.so
%_includedir/qpid
%_pkgconfigdir/qpid.pc
%_datadir/qpid
%_libdir/cmake/Qpid

%files -n libqmf2
%_libdir/libqmf2.so.*

%files -n python-module-qmfgen
%python_sitelibdir_noarch/qmfgen
%exclude %python_sitelibdir_noarch/qmfgen/templates/CMakeLists.cmake

%files -n python-module-qmf
%python_sitelibdir/qmf

%files -n libqmf2-devel
%_libdir/libqmf2.so
%_includedir/qmf
%_pkgconfigdir/qmf2.pc
%_bindir/qmf-gen
%_man1dir/qmf-gen*

%files client
%_bindir/qpid-receive
%_bindir/qpid-send
%_man1dir/qpid-receive*
%_man1dir/qpid-send*
%doc LICENSE.txt
%doc NOTICE.txt
%doc README.md
%dir %_libdir/qpid
%dir %_libdir/qpid/client
%_libdir/qpid/client/*
%exclude %_libdir/qpid/client/rdmaconnector.so

%dir %_sysconfdir/qpid
%config(noreplace) %_sysconfdir/qpid/qpidc.conf

%files client-tests
%_bindir/qpid-perftest
%_bindir/qpid-topic-listener
%_bindir/qpid-topic-publisher
%_bindir/qpid-latency-test
%_bindir/qpid-client-test
%_bindir/qpid-txtest
%_libexecdir/qpid/tests

%files server
%_libdir/libqpidbroker.so.*
%_sbindir/qpidd
%_initdir/qpidd
%_unitdir/qpidd.service
%_tmpfilesdir/qpidd.conf
%config(noreplace) %_sysconfdir/qpid/qpidd.conf
%config(noreplace) %_sysconfdir/sasl2/qpidd.conf
%dir %_libdir/qpid/daemon
%_libdir/qpid/daemon/amqp.so
%attr(755, qpidd, qpidd) %_localstatedir/qpidd
%attr(755, qpidd, qpidd) %_runtimedir/qpidd
%_man1dir/qpidd*

%files server-ha
%_initdir/qpidd-primary
%_unitdir/qpidd-primary.service
%_libdir/qpid/daemon/ha.so
%doc docs/ha.txt

%if_enabled rdma
%files client-rdma
%_libdir/librdmawrap.so.*
%_libdir/qpid/client/rdmaconnector.so

%files server-rdma
%_libdir/qpid/daemon/rdma.so
%endif

#%files server-xml
#%_libdir/qpid/daemon/xml.so

%files server-store
%_libdir/qpid/daemon/store.so*

%files server-linearstore
%_libdir/qpid/daemon/linearstore.so
%_libdir/liblinearstoreutils.so

%if_enabled perl
%files -n perl-qpid_messaging
%_libdir/perl5/*
%endif

%if_enabled python
%files -n python-module-qpid_messaging
%python_sitelibdir/*qpid_messaging*
%endif

%files -n qpid-tools
%_bindir/qpid-config
%_bindir/qpid-ha
%_bindir/qpid-printevents
%_bindir/qpid-queue-stats
%_bindir/qpid-route
%_bindir/qpid-stat
%_bindir/qpid-tool
%_man1dir/qpid-config*
%_man1dir/qpid-ha*
%_man1dir/qpid-printevents*
%_man1dir/qpid-queue-stats*
%_man1dir/qpid-route*
%_man1dir/qpid-stat*
%_man1dir/qpid-tool*
%python_sitelibdir/qpidtoollibs
%_libexecdir/qpid-qls-analyze
%dir %_datadir/qpid-tools
%dir %_datadir/qpid-tools/python
%_datadir/qpid-tools/python/qlslibs
%python_sitelibdir/qpid_tools-*.egg-info

%files client-devel-docs
%doc %_pkgdocdir

%changelog
* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.39.0-alt2
- Rebuilt with boost-1.71.0.

* Thu Jan 31 2019 Alexey Shabalin <shaba@altlinux.org> 1.39.0-alt1
- new version 1.39.0
- disable build bindings

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.36.0-alt1.3
- rebuild with new perl 5.28.1

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.36.0-alt1.2
- NMU: rebuilt with boost-1.67.0.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.36.0-alt1.1
- rebuild with new perl 5.26.1

* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 1.36.0-alt1
- NMU: new version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.35.0-alt0.rc.1
- rebuild with new perl 5.24.1

* Tue Sep 06 2016 Alexey Shabalin <shaba@altlinux.ru> 1.35.0-alt0.rc
- 1.35.0-rc

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.34-alt1
- 0.34

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1.1
- rebuild with new perl 5.22.0

* Tue Mar 24 2015 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1
- initial build
