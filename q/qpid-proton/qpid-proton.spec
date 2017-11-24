# a hack: should be fixed
%def_without doc

%define proton_datadir %_datadir/proton-%version

Name: qpid-proton
Version: 0.18.1
Release: alt1
Summary: A high performance, lightweight messaging library
Group: System/Libraries

License: ASL 2.0
Url: http://qpid.apache.org/proton/

Source: %name-%version.tar

BuildRequires: cmake >= 2.6

BuildRequires: swig
BuildRequires: doxygen
BuildRequires: libuuid-devel
BuildRequires: libssl-devel
BuildRequires: libsasl2-devel
BuildRequires: python-devel
BuildRequires: python-module-epydoc
BuildRequires: perl-devel
BuildRequires: perl-Test-Exception perl-Switch

%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package -n lib%name
Summary: C libraries for Qpid Proton
Group: System/Libraries

%description -n lib%name
C libraries for Qpid Proton
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

C libraries for Qpid Proton

%package -n lib%name-devel
Requires: lib%name = %version-%release
Summary: Development libraries for writing messaging apps with Qpid Proton
Group: Development/C

%description -n lib%name-devel
Development libraries for writing messaging apps with Qpid Proton

%package -n python-module-qpid-proton
Summary: Python language bindings for the Qpid Proton messaging framework
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-qpid-proton
Python language bindings for the Qpid Proton messaging framework

%package  -n lib%name-devel-doc
Summary: Documentation for the C development libraries for Qpid Proton
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Documentation for the C development libraries for Qpid Proton

%package -n python-module-qpid-proton-doc
Summary: Documentation for the Python language bindings for Qpid Proton
Group: Development/Documentation
BuildArch: noarch

%description -n python-module-qpid-proton-doc
Documentation for the Python language bindings for Qpid Proton

%package -n perl-qpid_proton
Summary: Perl language bindings for Qpid Proton
Group: Development/Perl
Requires: lib%name = %version-%release

%description -n perl-qpid_proton
Perl language bindings for Qpid Proton


#%%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_archlib -Mqpid::proton -Mqpid::proton::Mapping' PERL5LIB='%buildroot%_libdir'
%define _perl_req_method relaxed

%prep
%setup

%build
%cmake \
    -DPYTHON_SITEARCH_PACKAGES=%python_sitelibdir \
    -DNOBUILD_RUBY=1 \
    -DNOBUILD_PHP=1 \
    -DSYSINSTALL_PYTHON=1 \
    -DSYSINSTALL_PERL=1 \
    -DCHECK_SYSINSTALL_PYTHON=0 \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build VERBOSE=1

%install
%cmakeinstall_std
mkdir -p %buildroot%_defaultdocdir/%name-%version
mv %buildroot%proton_datadir/examples %buildroot%_defaultdocdir/%name-%version/

%files -n lib%name
%dir %proton_datadir
%doc %proton_datadir/LICENSE
%doc %proton_datadir/README*
%_libdir/libqpid-proton.so.*
%_libdir/libqpid-proton-core.so.*
%_libdir/libqpid-proton-proactor.so.*

%files -n lib%name-devel
%_includedir/proton
%_libdir/libqpid-proton.so
%_libdir/libqpid-proton-core.so
%_libdir/libqpid-proton-proactor.so
%_libdir/pkgconfig/libqpid-proton.pc
%_libdir/pkgconfig/libqpid-proton-core.pc
%_libdir/pkgconfig/libqpid-proton-proactor.pc
%_libdir/cmake/Proton
%doc %_defaultdocdir/%name-%version/

%if_with doc
%files -n lib%name-devel-doc
%doc %proton_datadir/docs/api-c
%endif

%files -n python-module-qpid-proton
%python_sitelibdir/_cproton.so
%python_sitelibdir/cproton.*
%python_sitelibdir/proton


%if_with doc
%files -n python-module-qpid-proton-doc
%doc %proton_datadir/docs/api-py
%endif

%files -n perl-qpid_proton
%perl_vendor_archlib/*

%changelog
* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.18.1-alt1
- NMU: fixed build && updated version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1.1
- rebuild with new perl 5.24.1

* Tue Aug 30 2016 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2.1
- rebuild with new perl 5.22.0

* Fri Nov 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2
- fixed build for perl 5.22 update
- (conditional doc; quick hack to fix the build)


* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- initial build
