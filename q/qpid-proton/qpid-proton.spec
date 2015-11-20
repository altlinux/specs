# a hack: should be fixed
%def_without doc

%define proton_datadir %_datadir/proton-%version

Name: qpid-proton
Version: 0.8
Release: alt2
Summary: A high performance, lightweight messaging library
Group: System/Libraries

License: ASL 2.0
Url: http://qpid.apache.org/proton/

Source: %name-%version.tar
Patch0001: 0001-PROTON-731-Installing-Python-requires-Proton-be-inst.patch
Patch0002: 0001-NO-JIRA-Perl-to-use-the-utils-module.patch

BuildRequires: cmake >= 2.6

BuildRequires: swig
BuildRequires: doxygen
BuildRequires: libuuid-devel
BuildRequires: libssl-devel
BuildRequires: python-devel
BuildRequires: python-module-epydoc
BuildRequires: perl-devel
BuildRequires: perl-Test-Exception

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

%patch0001 -p1
%patch0002 -p1

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

%files -n lib%name
%dir %proton_datadir
%doc %proton_datadir/LICENSE
%doc %proton_datadir/README
%doc %proton_datadir/TODO
%_bindir/proton
%_bindir/proton-dump
%_libdir/libqpid-proton.so.*
%_man1dir/*

%files -n lib%name-devel
%_includedir/proton
%_libdir/libqpid-proton.so
%_libdir/pkgconfig/libqpid-proton.pc
%_libdir/cmake/Proton
%_datadir/proton/examples

%if_with doc
%files -n lib%name-devel-doc
%doc %proton_datadir/docs/api-c
%endif

%files -n python-module-qpid-proton
%python_sitelibdir/_cproton.so
%python_sitelibdir/cproton.*
%python_sitelibdir/proton.*


%if_with doc
%files -n python-module-qpid-proton-doc
%doc %proton_datadir/docs/api-py
%endif

%files -n perl-qpid_proton
%perl_vendor_archlib/*

%changelog
* Fri Nov 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2
- fixed build for perl 5.22 update
- (conditional doc; quick hack to fix the build)


* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- initial build
