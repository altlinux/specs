# Set the version number here.
%define ACEVER  8.0.1
%define TAOVER  4.0.1

# Conditional build
# Default values are
#                    --with ipv6         (IPv6 support)
#                    --with opt          (Optimized build)
#                    --with zlib         (Zlib compressor)
#                    --with bzip2        (Bzip2 compressor)
#                    --with tao          (TAO)
#                    --without fltk      (No ftlk support)
#                    --without tk        (No tk support)
#                    --without xt        (No xt support)
#                    --without fox       (No fox support)
#                    --without qt        (No qt support)
#                    --without inline    (Code inlining disabled)
#                    --without versioned (Versioned namespace)

#
# Read: If neither macro exists, then add the default definition.
%{!?_with_ipv6: %{!?_without_ipv6: %define _with_ipv6 --with-ipv6}}
%{!?_with_opt: %{!?_without_opt: %define _with_opt --with-opt}}
%{!?_with_zlib: %{!?_without_zlib: %define _with_zlib --with-zlib}}
%{!?_with_bzip2: %{!?_without_bzip2: %define _with_bzip2 --with-bzip2}}
%{!?_with_tao: %{!?_without_tao: %global _with_tao --with-tao}}
%{!?_with_ftlk: %{!?_without_ftlk: %define _without_ftlk --without-ftlk}}
%{!?_with_tk: %{!?_without_tk: %define _without_tk --without-tk}}
%{!?_with_xt: %{!?_without_xt: %define _without_xt --without-xt}}
%{!?_with_fox: %{!?_without_fox: %define _without_fox --without-fox}}
%{!?_with_qt: %{!?_without_qt: %define _without_qt --without-qt}}
%{!?_with_inline: %{!?_without_inline: %define _without_inline --without-inline}}
%{!?_with_versioned: %{!?_without_versioned: %define _without_versioned 0}}
#
# Read: It's an error if both or neither required options exist.
%{?_with_ipv6: %{?_without_ipv6: %{error: both _with_ipv6 and _without_ipv6}}}
%{?_with_opt: %{?_without_opt: %{error: both _with_opt and _without_opt}}}
%{?_with_zlib: %{?_without_zlib: %{error: both _with_zlib and _without_zlib}}}
%{?_with_bzip2: %{?_without_bzip2: %{error: both _with_bzip2 and _without_bzip2}}}
%{?_with_tao: %{?_without_tao: %{error: both _with_tao and _without_tao}}}
%{?_with_fltk: %{?_without_fltk: %{error: both _with_fltk and _without_fltk}}}
%{?_with_tk: %{?_without_tk: %{error: both _with_tk and _without_tk}}}
%{?_with_xt: %{?_without_xt: %{error: both _with_xt and _without_xt}}}
%{?_with_fox: %{?_without_fox: %{error: both _with_fox and _without_fox}}}
%{?_with_qt: %{?_without_qt: %{error: both _with_qt and _without_qt}}}
%{?_with_inline: %{?_without_inline: %{error: both _with_inline and _without_inline}}}
%{?_with_versioned: %{?_without_versioned: %{error: both _with_versioned and _without_versioned}}}

%{!?skip_make:%global skip_make 0}
%{!?make_nosrc:%global make_nosrc 0}

%define have_fox 0

%if %{?_with_opt:0}%{!?_with_opt:1}
%define OPTTAG .O0
%endif

#All packages start with dre prefix meaning Distributed Real-time and Embedded (DRE) Systems
Name: dre-ace-tao
Version: %ACEVER
Release: alt2

%if 0%{?_with_tao:1}%{?_without_tao:0}
Summary: The ADAPTIVE Communication Environment (ACE) and The ACE ORB (TAO)
%else
Summary: The ADAPTIVE Communication Environment (ACE)
%endif
License: DOC
Group: Development/C++
Url: http://www.dre.vanderbilt.edu/~schmidt/ACE.html

%if 0%{?_with_tao:1}%{?_without_tao:0}
Source0: http://download.dre.vanderbilt.edu/previous_versions/ACE+TAO-src-%ACEVER.tar
%else
Source0: http://download.dre.vanderbilt.edu/previous_versions/ACE-src-%ACEVER.tar
%endif
Source1: ace-tao-rpmlintrc
Source2: ace-tao-init-alt.tar

%define _extension .xz

%if 0%{?mdkversion}
BuildRequires: sendmail
%endif

BuildRequires: openssl-devel
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

%if %{?_with_zlib:1}%{!?_with_zlib:0}
BuildRequires: zlib-devel
%endif

%if %{?_with_bzip2:1}%{!?_with_bzip2:0}
BuildRequires: bzip2
%endif

BuildRequires: perl perl-Net-Telnet

%if %{?_with_fltk:1}%{!?_with_fltk:0}
BuildRequires: fltk-devel
%define fltk_pac dre-ace-flreactor
%endif

%if %{?_with_tk:1}%{!?_with_tk:0}
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: tk
%define tk_pac dre-ace-tkreactor
%define tao_tk_pac dre-tao-tkresource
%endif

%if %{?_with_qt:1}%{!?_with_qt:0}
%define qt_pack dre-ace-qtreactor
%define tao_qt_pac dre-tao-qtresource

%define qtpacname qt5

BuildRequires: %qtpacname-base-devel
%endif

%if %{?_with_fox:1}%{!?_with_fox:0}
%define fox_pac dre-ace_foxreactor
%endif

%if %{?_with_xt:1}%{!?_with_xt:0}
%define xt_pac dre-ace-xtreactor
%define tao_xt_pac dre-tao-xtresource
%endif

%if %{?_with_fl:1}%{!?_with_fl:0}
%define tao_fl_pac dre-tao-flresource
%endif


%description -n dre-ace-tao
The ADAPTIVE Communication Environment (ACE) is a freely available,
open-source object-oriented (OO) framework that implements many core
patterns for concurrent communication software. ACE provides a rich
set of reusable C++ wrapper facades and framework components that
perform common communication software tasks across a range of OS
platforms. The communication software tasks provided by ACE include
event demultiplexing and event handler dispatching, signal handling,
service initialization, interprocess communication, shared memory
management, message routing, dynamic (re)configuration of distributed
services, concurrent execution and synchronization.

TAO is a real-time implementation of CORBA built using the framework
components and patterns provided by ACE. TAO contains the network
interface, OS, communication protocol, and CORBA middleware components
and features. TAO is based on the standard OMG CORBA reference model,
with the enhancements designed to overcome the shortcomings of
conventional ORBs for high-performance and real-time applications.

# ---------------- ace ----------------

%package -n     dre-ace
Summary: The ADAPTIVE Communication Environment (ACE)
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: openssl

%description -n dre-ace
The ADAPTIVE Communication Environment (ACE) is a freely available,
open-source object-oriented (OO) framework that implements many core
patterns for concurrent communication software. ACE provides a rich
set of reusable C++ wrapper facades and framework components that
perform common communication software tasks across a range of OS
platforms. The communication software tasks provided by ACE include
event demultiplexing and event handler dispatching, signal handling,
service initialization, interprocess communication, shared memory
management, message routing, dynamic (re)configuration of distributed
services, concurrent execution and synchronization.

# ---------------- ace-devel ----------------

%package -n     dre-ace-devel
Summary: Header files and development components for ACE
Version: %ACEVER
Group: Development/C++
AutoReqProv: no
Requires: dre-ace = %ACEVER
Requires: openssl-devel

%description -n dre-ace-devel
This package contains the components needed for developing programs
using ACE.

# ---------------- ace-xml ----------------

%package -n     dre-ace-xml
Summary: ACE XML Runtime Support
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER

%description -n dre-ace-xml
ACE XML Parser interfaces follows the the design of SAX 2.0, which is
a public domain specification for Java.  The major difference between
ACE XML Parser interfaces and SAX is that we added an reference of
ACEXML_Env to every SAX method to accommodate platforms/compilers that
don't support C++ exceptions.  SAX is defined by David Megginson
<david@megginson.com>

# ---------------- ace-gperf ----------------

%package -n     dre-ace-gperf
Summary: ACE gperf
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER

%description -n dre-ace-gperf
ACE gperf utility

# ---------------- ace-xml-devel ----------------

%package -n     dre-ace-xml-devel
Summary: Header files and development components for ACE XML
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-xml = %ACEVER

%description -n dre-ace-xml-devel
This package contains the components needed for developing programs
using ACEXML.

# ---------------- ace-kokyu ----------------

%package -n     dre-ace-kokyu
Summary: Kokyu scheduling framework for ACE
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER

%description -n dre-ace-kokyu
Kokyu is a portable middleware scheduling framework designed to
provide flexible scheduling and dispatching services within the
context of higher-level middleware. Kokyu currently provides real-time
scheduling and dispatching services for TAO's real-time Event Service
which mediates supplier-consumer relationships between application
operations. Kokyu also provides a scheduling and dispatching framework
for threads. This is being used by the TAO RTCORBA 2.0 scheduler
implementations.

# ---------------- ace-kokyu-devel ----------------

%package -n     dre-ace-kokyu-devel
Summary: Header files and development components for the ACE Kokyu scheduler
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-kokyu = %ACEVER

%description -n dre-ace-kokyu-devel
This package contains the components needed for developing programs
using Kokyu.

# ---------------- ace-foxreactor ----------------

%if %{?_with_fox:1}%{!?_with_fox:0}
%if 0%{?have_fox} == 1
%package -n     dre-ace-foxreactor
Summary: ACE_FoxReactor for use with the FOX toolkit
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER
Requires: fox16

%description -n dre-ace-foxreactor
A Reactor implementation that uses the FOX toolkit for
event demultiplexing.  This will let us integrate the FOX toolkit with
ACE and/or TAO.
%endif
%endif

# ---------------- ace-foxreactor-devel ----------------

%if %{?_with_fox:1}%{!?_with_fox:0}
%if 0%{?have_fox} == 1
%package -n     dre-ace-foxreactor-devel
Summary: Header files for development with ACE_FoxReactor
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-foxreactor = %ACEVER
Requires: fox16-devel

%description -n dre-ace-foxreactor-devel
This package contains the components needed for developing programs
using the ACE_FoxReactor.
%endif
%endif

# ---------------- ace-flreactor ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}
%package -n     dre-ace-flreactor
Summary: ACE_FlReactor for use with the Fast-Light toolkit
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER
Requires: fltk

%description -n dre-ace-flreactor
A Reactor implementation that uses the Fast-Light (FL) toolkit for
event demultiplexing.  This will let us integrate the FL toolkit with
ACE and/or TAO.
%endif

# ---------------- ace-flreactor-devel ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}
%package -n     dre-ace-flreactor-devel
Summary: Header files for development with ACE_FlReactor
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-flreactor = %ACEVER
Requires: fltk-devel

%description -n dre-ace-flreactor-devel
This package contains the components needed for developing programs
using the ACE_FlReactor.
%endif

# ---------------- ace-qtreactor ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}
%package -n     dre-ace-qtreactor
Summary: ACE_QtReactor for use with Qt library
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER
Requires: qt5

%description -n dre-ace-qtreactor
A Reactor implementation that uses the Qt toolkit for event
demultiplexing.  This will let us integrate the Qt toolkit with ACE
and/or TAO.
%endif

# ---------------- ace-qtreactor-devel ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}
%package -n     dre-ace-qtreactor-devel
Summary: Header files for development with ACE_QtReactor
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-qtreactor = %ACEVER
Requires: qt5-base-devel

%description -n dre-ace-qtreactor-devel
This package contains the components needed for developing programs
using the ACE_QtReactor.
%endif

# ---------------- ace-tkreactor ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}
%package -n     dre-ace-tkreactor
Summary: ACE_TkReactor for use with Tk toolkit
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER
Requires: tk

%description -n dre-ace-tkreactor
A Reactor implementation that uses the Tk toolkit for event
demultiplexing.  This will let us integrate the Tk toolkit with ACE
and/or TAO.
%endif

# ---------------- ace-tkreactor-devel ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}
%package -n     dre-ace-tkreactor-devel
Summary: Header files for development with ACE_TkReactor
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-tkreactor = %ACEVER
Requires: tk-devel

%description -n dre-ace-tkreactor-devel
This package contains the components needed for developing programs
using the ACE_TkReactor.
%endif

# ---------------- ace-xtreactor ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}
%package -n     dre-ace-xtreactor
Summary: ACE_XtReactor for use with the X Toolkit
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER
# The xorg packaging scheme changed, let autoreq to the job for now.
# Requires: xorg-x11-libs

%description -n dre-ace-xtreactor
A Reactor implementation that uses the X Toolkit for event
demultiplexing.  This will let us integrate the X Toolkit with ACE
and/or TAO.
%endif

# ---------------- ace-xtreactor-devel ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}
%package -n     dre-ace-xtreactor-devel
Summary: Header files for development with ACE_XtReactor
Version: %ACEVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-xtreactor = %ACEVER
# The xorg package naming scheme changed, use specific files for now.
# old -> Requires: xorg-x11-devel
# new -> Requires: libX11-devel
Requires: libX11-devel
Requires: libXt-devel

%description -n dre-ace-xtreactor-devel
This package contains the components needed for developing programs
using the ACE_XtReactor.
%endif

# ---------------- MPC ----------------

%package -n   dre-mpc
Summary: Make Project Creator
Version: %ACEVER
Group: Development/Tools
Conflicts: mpc
AutoReqProv: noperl

%description -n dre-mpc
The Makefile, Project and Workspace Creator.
Designed by Justin Michel (michel_j@ociweb.com) and Chad Elliott.
Implemented by Chad Elliott (elliott_c@ociweb.com).

A single tool (MPC) can be used to generate tool specific input (i.e.
Makefile, dsp, vcproj, etc). The generator takes platform and building
tool generic files (mpc files) as input which describe basic information
needed to generate a "project" file for various build tools. These tools
include Make, NMake, Visual C++ 6, Visual C++ 7, etc.

# ---------------- tao ----------------
%if 0%{?_with_tao:1}%{?_without_tao:0}

%package -n     dre-tao
Summary: The ACE ORB (TAO)
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace = %ACEVER

%description -n dre-tao
TAO is a real-time implementation of CORBA built using the framework
components and patterns provided by ACE. TAO contains the network
interface, OS, communication protocol, and CORBA middleware components
and features. TAO is based on the standard OMG CORBA reference model,
with the enhancements designed to overcome the shortcomings of
conventional ORBs for high-performance and real-time applications.

# ---------------- tao-devel ----------------

%package -n     dre-tao-devel
Summary: Header files and development components for TAO
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: dre-ace-devel = %ACEVER
Requires: dre-ace-gperf = %ACEVER

%description -n dre-tao-devel
This package contains the components needed for developing programs
using TAO.

# ---------------- tao-utils ----------------

%package -n     dre-tao-utils
Summary: TAO naming service and IOR utilities
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER

%description -n dre-tao-utils
This package includes programs to query or control a CORBA naming service,
and to dump an IOR.

The following programs are included:
* tao-nslist, to list naming context and object bindings
* tao-nsadd, to create bindings
* tao-nsdel, to remove bindings
* tao-catior, to dump the content of an Interoperable Object Reference

# ---------------- tao-cosnaming ----------------

%package -n     dre-tao-cosnaming
Summary: The TAO CORBA Naming Service (CosNaming) and Interoperable Naming Service (INS)
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: logrotate

%description -n dre-tao-cosnaming
OMG defined CORBA Naming Service to provide a basic service location
mechanism for CORBA systems. CosNaming manages a hierarchy of
name-to-object-reference mappings. Anything, but typically the server
process hosting an object, may bind an object reference with a name in
the Naming Service by providing the name and object
reference. Interested parties (typically clients) can then use the
Naming Service to resolve a name to an object reference.

More recently, CORBA Naming Service was subsumed/extended by the CORBA
Interoperable Naming Service, a.k.a. INS. INS inherits all the
functionality from the original Naming Service specification in
addition to addressing some its shortcomings. In particular, INS
defines a standard way for clients and servers to locate the Naming
Service itself. It also allows the ORB to be administratively
configured for bootstrapping to services not set up with the orb at
install time.

# ---------------- tao-cosevent ----------------

%package -n     dre-tao-cosevent
Summary: The TAO CORBA CosEvent Service
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: logrotate

%description -n dre-tao-cosevent
The CosEvent_Service is a COS compliant Event Service.

The service is registered with the naming service with the name
"CosEventService" . It exposes the <EventChannel> interface which can be
used by suppliers and consumers to send and receive events.

# ---------------- tao-cosnotification ----------------

%package -n     dre-tao-cosnotification
Summary: The TAO CORBA Notification Service
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: logrotate

%description -n dre-tao-cosnotification
The Notify_Service is a COS compliant Notification Service.

The Notify_Service executable starts up a Notification Service factory
and registers it with the Naming Service under the name
"NotifyEventChannelFactory"

# ---------------- tao-costrading ----------------

%package -n     dre-tao-costrading
Summary: The TAO CORBA Trading Service
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: logrotate

%description -n dre-tao-costrading
The Trading_Service is a COS compliant Trading Service.

# ---------------- tao-rtevent ----------------

%package -n     dre-tao-rtevent
Summary: The TAO Real-time Event Service
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: logrotate

%description -n dre-tao-rtevent
The TAO Real-Time Event Service. This is a TAO specific service
implementation

# ---------------- tao-cosconcurrency ----------------

%package -n     dre-tao-cosconcurrency
Summary: The TAO CORBA Concurrency Service
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-tao = %TAOVER
Requires: logrotate

%description -n dre-tao-cosconcurrency
The CORBA Concurrency Service. One of the standard CORBA services.

# ---------------- tao-flresource ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}
%package -n     dre-tao-flresource
Summary: FlResource_Factory for creating FlReactor
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-flreactor = %ACEVER
Requires: dre-tao = %TAOVER

%description -n dre-tao-flresource
This factory is intended for creating FlReactor for ORB. This factory
can be feed into ORB using TAO_ORB_Core::set_gui_resource_factory
method which is usually done by TAO_FlResource_Loader.
%endif

# ---------------- tao-flresource-devel ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}
%package -n     dre-tao-flresource-devel
Summary: Header files for development with FlResource_Factory
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-flreactor-devel = %ACEVER
Requires: dre-tao-devel = %TAOVER
Requires: dre-tao-flresource = %TAOVER

%description -n dre-tao-flresource-devel
This package contains the components needed for developing programs
using the FlResource_Factory.
%endif

# ---------------- tao-qtresource ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}
%package -n     dre-tao-qtresource
Summary: QtResource_Factory for creating QtReactor
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-qtreactor = %ACEVER
Requires: dre-tao = %TAOVER

%description -n dre-tao-qtresource
This factory is intended for creating QtReactor for ORB. This factory
can be feed into ORB using TAO_ORB_Core::set_gui_resource_factory
method which is usually done by TAO_QtResource_Loader.
%endif

# ---------------- tao-qtresource-devel ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}
%package -n     dre-tao-qtresource-devel
Summary: Header files for development with QtResource_Factory
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-qtreactor-devel = %ACEVER
Requires: dre-tao-devel = %TAOVER
Requires: dre-tao-qtresource = %TAOVER

%description -n dre-tao-qtresource-devel
This package contains the components needed for developing programs
using the QtResource_Factory.
%endif

# ---------------- tao-tkresource ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}
%package -n     dre-tao-tkresource
Summary: TkResource_Factory for creating TkReactor
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-tkreactor = %ACEVER
Requires: dre-tao = %TAOVER

%description -n dre-tao-tkresource
This factory is intended for creating TkReactor for ORB. This factory
can be feed into ORB using TAO_ORB_Core::set_gui_resource_factory
method which is usually done by TAO_TkResource_Loader.
%endif

# ---------------- tao-tkresource-devel ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}
%package -n     dre-tao-tkresource-devel
Summary: Header files for development with TkResource_Factory
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-tkreactor-devel = %ACEVER
Requires: dre-tao-devel = %TAOVER
Requires: dre-tao-tkresource = %TAOVER

%description -n dre-tao-tkresource-devel
This package contains the components needed for developing programs
using the TkResource_Factory.
%endif

# ---------------- tao-xtresource ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}
%package -n     dre-tao-xtresource
Summary: XtResource_Factory for creating XtReactor
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-xtreactor = %ACEVER
Requires: dre-tao = %TAOVER

%description -n dre-tao-xtresource
This factory is intended for creating XtReactor for ORB. This factory
can be feed into ORB using TAO_ORB_Core::set_gui_resource_factory
method which is usually done by TAO_XtResource_Loader.
%endif

# ---------------- tao-xtresource-devel ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}
%package -n     dre-tao-xtresource-devel
Summary: Header files for development with XtResource_Factory
Version: %TAOVER
Group: Development/C++
AutoReqProv: noperl
Requires: dre-ace-xtreactor-devel = %ACEVER
Requires: dre-tao-devel = %TAOVER
Requires: dre-tao-xtresource = %TAOVER

%description -n dre-tao-xtresource-devel
This package contains the components needed for developing programs
using the XtResource_Factory.
%endif

%endif

# ================================================================
# prep
# ================================================================

%prep
%setup -n ACE_wrappers
tar xf %SOURCE2 -C .

#deleting perl scrits for alt linux perl rpmbuild
cd bin/PerlACE
rm -rf Process_VMS.pm Process_Win32.pm ProcessAndroid.pm ProcessVX_Win32.pm ProcessWinCE_Unix.pm ProcessWinCE.pm TestTarget_Android.pm

# ================================================================
# build
# ================================================================

%build
export ACE_ROOT=$(pwd)
export MPC_ROOT=$ACE_ROOT/MPC
export LD_LIBRARY_PATH=$ACE_ROOT/lib
%if 0%{?_with_tao:1}%{?_without_tao:0}
export TAO_ROOT=$ACE_ROOT/TAO
%endif

# Dump the g++ versions, in case the g++ version is broken we can
# easily see this in the build log
g++ --version
g++ -dumpversion

%define inline %nil

%if %skip_make

cd .. && rm -rf ACE_wrappers && ln -s ACE_wrappers-BUILT ACE_wrappers

%else

cat > $ACE_ROOT/ace/config.h << EOF
EOF

# If ipv6 support is indicated insert some lines into the config.h file
%if %{?_with_ipv6:1}%{!?_with_ipv6:0}
cat >> $ACE_ROOT/ace/config.h << EOF
#define ACE_HAS_IPV6
#define ACE_USES_IPV4_IPV6_MIGRATION
EOF
%endif

# Include platform include
cat >> $ACE_ROOT/ace/config.h << EOF
#include "ace/config-linux.h"
EOF

%if %{?_with_inline:1}%{!?_with_inline:0}
%define inline -D__ACE_INLINE__ -U__ACE_NO_INLINE__
%else
%define inline -D__ACE_NO_INLINE__ -U__ACE_INLINE__
%endif

cat > $ACE_ROOT/include/makeinclude/platform_macros.GNU <<EOF
CCFLAGS += %optflags
CFLAGS += %optflags
ssl = 1

%if %{?_with_inline:1}%{!?_with_inline:0}
inline = 1
%else
inline = 0
%endif

%if %{?_with_xt:1}%{!?_with_xt:0}
xt = 1
ace_xtreactor = 1
x11 = 1
tao_xtresource = 1
%endif

%if %{?_with_tk:1}%{!?_with_tk:0}
ace_tkreactor = 1
tao_tkresource = 1
tk = 1
%endif

%if %{?_with_fl:1}%{!?_with_fl:0}
fl = 1
tao_flresource = 1
ace_flreactor = 1
%endif

%if %{?_with_qt:1}%{!?_with_qt:0}
qt5 = 1
gl = 1
ace_qt5reactor = 1
tao_qt5resource = 1
%endif
EOF

%if %{?_with_fox:1}%{!?_with_fox:0}
%if 0%{?have_fox} == 1
cat >> $ACE_ROOT/include/makeinclude/platform_macros.GNU <<EOF
fox = 1
ace_foxreactor = 1
tao_foxresource = 1
EOF
%endif
%endif


#buildbits sets -m64 options for compiler
cat >> $ACE_ROOT/include/makeinclude/platform_macros.GNU <<EOF
%ifarch x86_64 ia64 ppc64 s390x
buildbits = 64
%endif

%ifarch ppc64
minimaltoc = 1
%endif

%if %{?_with_opt:0}%{!?_with_opt:1}
optimize = 0
%else
optimize = 1
%endif

include \$(ACE_ROOT)/include/makeinclude/platform_linux.GNU
EOF

cat > $ACE_ROOT/bin/MakeProjectCreator/config/default.features <<EOF
ssl=1

%if %{?_with_bzip2:1}%{!?_with_bzip2:0}
bzip2 = 1
%endif

%if %{?_with_zlib:1}%{!?_with_zlib:0}
zlib = 1
%endif

%if %{?_with_versioned:1}%{!?_with_versioned:0}
versioned_namespace = 1
%endif
EOF

# We don't use default.features to enable ipv6 cause it conflicts w/
# the config.h generated version.  Config.h is superior because it is
# shipped to the end-user machines and also defines
# ACE_USES_IPV4_IPV6_MIGRATION which the default.features technique
# does not seem to set.

%if %{?_with_fox:1}%{!?_with_fox:0}
%if 0%{?have_fox} == 1
cat >> $ACE_ROOT/bin/MakeProjectCreator/config/default.features <<EOF
fox=1
EOF
%endif
%endif

# Need to regenerate all of the GNUMakefiles
# then make everything that we have generated for
%if 0%{?_with_tao:1}%{?_without_tao:0}
bin/mwc.pl -type gnuace TAO/TAO_ACE.mwc
make %{?_smp_mflags} -C $TAO_ROOT
%else
bin/mwc.pl -type gnuace ACE.mwc
make %{?_smp_mflags} -C $ACE_ROOT
%endif

%endif

# ================================================================
# install
# ================================================================

%define ACEVERSO %ACEVER
%define TAOVERSO %TAOVER

%install
export ACE_ROOT=$(pwd)
%if 0%{?_with_tao:1}%{?_without_tao:0}
export TAO_ROOT=$ACE_ROOT/TAO
%endif

# ---------------- Runtime Components ----------------

# install shared libraries
install -vd %buildroot%_libdir

# ACE + XML libraries
INSTLIBS=`ls ${ACE_ROOT}/lib/libACE*.so.%ACEVERSO`
install -v $INSTLIBS %buildroot%_libdir

# ACE-Kokyu libraries
INSTLIBS=`ls ${ACE_ROOT}/lib/libKokyu.so.%ACEVERSO`
install -v $INSTLIBS %buildroot%_libdir

%if 0%{?_with_tao:1}%{?_without_tao:0}
# TAO libraries
INSTLIBS=`ls ${ACE_ROOT}/lib/libTAO*.so.%TAOVERSO`
install -v $INSTLIBS %buildroot%_libdir
%endif

# Create un-versioned symbolic links for libraries
(cd %buildroot%_libdir && \
 ls *.so.* | awk 'BEGIN{FS="."}{print "ln -sf " $0 " " $1 "." $2;}' | sh)

# install binaries
install -vd %buildroot%_sbindir

# Rename the TAO service binaries:

%if 0%{?_with_tao:1}%{?_without_tao:0}

install -v ${ACE_ROOT}/TAO/orbsvcs/Naming_Service/tao_cosnaming \
    %buildroot%_sbindir/tao-cosnaming

install -v ${ACE_ROOT}/TAO/orbsvcs/CosEvent_Service/tao_cosevent \
    %buildroot%_sbindir/tao-cosevent

install -v ${ACE_ROOT}/TAO/orbsvcs/Notify_Service/tao_cosnotification \
    %buildroot%_sbindir/tao-cosnotification

install -v ${ACE_ROOT}/TAO/orbsvcs/Trading_Service/tao_costrading \
    %buildroot%_sbindir/tao-costrading

install -v ${ACE_ROOT}/TAO/orbsvcs/Event_Service/tao_rtevent \
    %buildroot%_sbindir/tao-rtevent

install -v ${ACE_ROOT}/TAO/orbsvcs/Concurrency_Service/tao_cosconcurrency \
    %buildroot%_sbindir/tao-cosconcurrency


mkdir -p %buildroot%_cachedir/tao
# Create data files which will be ghosted.
touch %buildroot%_cachedir/tao/tao-cosnaming.dat

mkdir -p %buildroot%_logdir/tao
# Create data files which will be ghosted.
for logfile in cosnaming cosconcurrency cosevent cosnotification costrading rtevent; do
    touch %buildroot%_logdir/tao/tao-${logfile}.log
done

%endif

# ---------------- Development Components ----------------

# INSTHDR="cp --preserve=timestamps"
INSTHDR="install -m 0644 -p"

# install headers
install -vd %buildroot%_includedir
( set +x
echo "Building list of headers..."

# Generate raw dependency output
BASEHDR=`find \
    ace \
    ACEXML/common \
    ACEXML/parser/parser \
    Kokyu \
    -name '*.h' -not -name 'config-*'`
%if 0%{?_with_tao:1}%{?_without_tao:0}
TAO_MM_OPTS="-I TAO -I TAO/orbsvcs -I TAO/orbsvcs/orbsvcs"
BASEHDR="$BASEHDR `find \
    TAO/tao \
    TAO/orbsvcs/orbsvcs \
    -name '*.h' -not -name 'config-*'`"
%endif
for j in $BASEHDR; do
        echo $j >> rawhdrs.log
        echo '#include <'$j'>' | \
        g++ %inline \
            -I . \
            -I protocols \
            $TAO_MM_OPTS \
            -x c++ - -MM -MF mmout 2>> rawhdrs.log && cat mmout || true;
done > mmraw.list

%if 0%{?_with_tao:1}%{?_without_tao:0}
# Append IDL headers to the raw list.
find \
    TAO/tao \
    TAO/orbsvcs/orbsvcs \
    -regex '.*\.p?idl$' >> mmraw.list
%endif

# Cleanup dependency output:
#   remove '-:' sequences
#   change all sequences of whitespace into \n
#   remove leading './'
#   cannonicalize up to two levels of '/../../'
#   remove duplicates
cat mmraw.list |\
        sed -e 's/^-://g' -e 's/\\//g' | \
        tr -s [:space:] "\n" | \
        sed -e 's#^./##g' | \
        sed -e 's#/[^/]\+/\.\./#/#g' -e 's#/[^/]\+/\.\./#/#g' | \
        sort -u > allhdrs.list

# Add missing headers.
ls ace/*{.h,.inl,.cpp} >> allhdrs.list
%if 0%{?_with_tao:1}%{?_without_tao:0}
ls TAO/tao/*{.h,.inl,_T.cpp} >> allhdrs.list
ls TAO/tao/*/*{.h,.inl,.cpp} >> allhdrs.list
ls TAO/orbsvcs/orbsvcs/*{.idl,.h,.inl,_T.cpp} >> allhdrs.list
ls TAO/orbsvcs/orbsvcs/*/*{.h,.inl,_T.cpp} >> allhdrs.list
ls TAO/orbsvcs/orbsvcs/ESF/*.cpp >> allhdrs.list
%endif

# Install headers and create header lists
rm -f ace-headers.tmp
rm -f acexml-headers.tmp
rm -f kokyu-headers.tmp
rm -f tao-headers.tmp

for i in `cat allhdrs.list`; do
    case "$i" in
    protocols/ace/*)
        mkdir -p `dirname %buildroot%_includedir/${i/protocols\/}`
        $INSTHDR $i %buildroot%_includedir/${i/protocols/}
        echo '%%dir %_includedir/'`dirname ${i/protocols/}` >> ace-headers.tmp
        echo '%_includedir/'${i/protocols/} >> ace-headers.tmp
        ;;
    ace/*)
        mkdir -p `dirname %buildroot%_includedir/$i`
        $INSTHDR $i %buildroot%_includedir/$i
        echo '%%dir %_includedir/'`dirname $i` >> ace-headers.tmp
        echo '%_includedir/'$i >> ace-headers.tmp
        ;;
    ACEXML/*)
        mkdir -p `dirname %buildroot%_includedir/$i`
        $INSTHDR $i %buildroot%_includedir/$i
        echo '%%dir %_includedir/'`dirname $i` >> acexml-headers.tmp
        echo '%_includedir/'$i >> acexml-headers.tmp
        ;;
    Kokyu/*)
        mkdir -p `dirname %buildroot%_includedir/$i`
        $INSTHDR $i %buildroot%_includedir/$i
        echo '%%dir %_includedir/'`dirname $i` >> kokyu-headers.tmp
        echo '%_includedir/'$i >> kokyu-headers.tmp
        ;;
    TAO/tao/*)
        mkdir -p `dirname %buildroot%_includedir/${i/TAO\/}`
        $INSTHDR $i %buildroot%_includedir/${i/TAO\/}
        echo '%%dir %_includedir/'`dirname ${i/TAO\/}` >> tao-headers.tmp
        echo '%_includedir/'${i/TAO\/} >> tao-headers.tmp
        ;;
    TAO/orbsvcs/orbsvcs/*)
        mkdir -p `dirname %buildroot%_includedir/${i/TAO\/orbsvcs\/}`
        $INSTHDR $i %buildroot%_includedir/${i/TAO\/orbsvcs\/}
        echo '%%dir %_includedir/'`dirname ${i/TAO\/orbsvcs\/}` >> tao-headers.tmp
        echo '%_includedir/'${i/TAO\/orbsvcs\/} >> tao-headers.tmp
        ;;
    *)
        echo $i
        ;;
    esac
done

echo '%_defattr' > ace-headers.list
sort -u < ace-headers.tmp >> ace-headers.list
rm -f ace-headers.tmp

echo '%_defattr' > acexml-headers.list
sort -u < acexml-headers.tmp >> acexml-headers.list
rm -f acexml-headers.tmp

echo '%_defattr' > kokyu-headers.list
sort -u < kokyu-headers.tmp >> kokyu-headers.list
rm -f kokyu-headers.tmp

%if 0%{?_with_tao:1}%{?_without_tao:0}
echo '%_defattr' > tao-headers.list
sort -u < tao-headers.tmp >> tao-headers.list
rm -f tao-headers.tmp
%endif

)

# Will also be needed for mpc.
install -vd %buildroot%_bindir

%if 0%{?_with_tao:1}%{?_without_tao:0}

# install the TAO_IDL compiler
install -vd %buildroot%_libdir

install -v ${ACE_ROOT}/bin/ace_gperf %buildroot%_bindir
install -v ${ACE_ROOT}/bin/tao_idl %buildroot%_bindir
install -v ${ACE_ROOT}/bin/tao_imr %buildroot%_bindir
install -v ${ACE_ROOT}/bin/tao_ifr %buildroot%_bindir
install -v ${ACE_ROOT}/TAO/orbsvcs/IFR_Service/tao_ifr_service %buildroot%_bindir
install -v ${ACE_ROOT}/bin/tao_catior %buildroot%_bindir/tao_catior
install -v ${ACE_ROOT}/bin/tao_nsadd %buildroot%_bindir/tao_nsadd
install -v ${ACE_ROOT}/bin/tao_nsdel %buildroot%_bindir/tao_nsdel
install -v ${ACE_ROOT}/bin/tao_nslist %buildroot%_bindir/tao_nslist
%endif

# ================================================================
# Config & Options
# ================================================================

install -vd %buildroot%_sysconfdir
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_sysconfdir/tao
cp -vR ${ACE_ROOT}/rpmbuild/etc/logrotate.d/* %buildroot%_sysconfdir/logrotate.d/
cp -vR ${ACE_ROOT}/rpmbuild/etc/tao/* %buildroot%_sysconfdir/tao/

mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
cp -vR ${ACE_ROOT}/ace-tao-init-alt/rc.d/init.d/* %buildroot%_initdir
cp -vR ${ACE_ROOT}/rpmbuild/ace-tao-init-fedora/tao/* %buildroot%_sysconfdir/tao/

# ================================================================
# Makefiles
# ================================================================

install -vd %buildroot%_datadir
install -vd %buildroot%_datadir/ace
install -vd %buildroot%_datadir/ace/include
install -vd %buildroot%_datadir/ace/include/makeinclude
install -vd %buildroot%_datadir/mpc
%if 0%{?_with_tao:1}%{?_without_tao:0}
install -vd %buildroot%_datadir/tao
install -vd %buildroot%_datadir/tao/orbsvcs
install -vd %buildroot%_datadir/tao/MPC
%endif

for mk_macros in \
    all_in_one.GNU \
    component_check.GNU \
    macros.GNU \
    platform_g++_common.GNU \
    platform_linux.GNU \
    platform_linux_common.GNU \
    platform_macros.GNU \
    rules.bin.GNU \
    rules.common.GNU \
    rules.lib.GNU \
    rules.local.GNU \
    rules.nested.GNU \
    rules.nolocal.GNU \
    rules.nonested.GNU \
    wrapper_macros.GNU; do (
        install -v ${ACE_ROOT}/include/makeinclude/$mk_macros %buildroot%_datadir/ace/include/makeinclude)
done

%if 0%{?_with_tao:1}%{?_without_tao:0}
install -v ${TAO_ROOT}/rules.tao.GNU %buildroot%_datadir/tao
%endif

cp -va ${ACE_ROOT}/MPC/* %buildroot%_datadir/mpc

install -vd %buildroot%_datadir/ace/bin
cp -va ${ACE_ROOT}/bin/DependencyGenerator %buildroot%_datadir/ace/bin
cp -va ${ACE_ROOT}/bin/MakeProjectCreator %buildroot%_datadir/ace/bin
install -vd %buildroot%_datadir/ace/bin/PerlACE
cp -va ${ACE_ROOT}/bin/PerlACE/* %buildroot%_datadir/ace/bin/PerlACE
install -v ${ACE_ROOT}/bin/mpc.pl %buildroot%_datadir/ace/bin
install -v ${ACE_ROOT}/bin/mwc.pl %buildroot%_datadir/ace/bin
install -v ${ACE_ROOT}/bin/g++dep %buildroot%_datadir/ace/bin
install -v ${ACE_ROOT}/bin/depgen.pl %buildroot%_datadir/ace/bin
install -v ${ACE_ROOT}/bin/generate_export_file.pl %buildroot%_datadir/ace/bin
install -v ${ACE_ROOT}/bin/add_rel_link.sh %buildroot%_datadir/ace/bin
install -v ${ACE_ROOT}/bin/{ACEutils,Uniqueid}.pm %buildroot%_datadir/ace/bin

ln -vsr %_includedir/ace %buildroot%_datadir/ace
%if 0%{?_with_tao:1}%{?_without_tao:0}
ln -vsr %_includedir/tao %buildroot%_datadir/tao
ln -vsr %_includedir/orbsvcs %buildroot%_datadir/tao/orbsvcs
%endif
ln -vsr %_libdir %buildroot%_datadir/ace/lib

ln -vsr install ${TAO_ROOT}/TAO_IDL/tao_idl %buildroot%_datadir/ace/bin

%if 0%{?_with_tao:1}%{?_without_tao:0}
cp -va ${TAO_ROOT}/MPC/* %buildroot%_datadir/tao/MPC

# Set TAO_IDL setting for the user
cat > %buildroot%_datadir/ace/include/makeinclude/platform_macros.GNU.tmp <<EOF
TAO_IDL = %_bindir/tao_idl
TAO_IDL_DEP = %_bindir/tao_idl
EOF
cat %buildroot%_datadir/ace/include/makeinclude/platform_macros.GNU >> %buildroot%_datadir/ace/include/makeinclude/platform_macros.GNU.tmp
mv %buildroot%_datadir/ace/include/makeinclude/platform_macros.GNU.tmp %buildroot%_datadir/ace/include/makeinclude/platform_macros.GNU
%endif

install -vd %buildroot%_sysconfdir/profile.d
cat > %buildroot%_sysconfdir/profile.d/mpc.sh <<EOF
MPC_ROOT=/usr/share/mpc
export MPC_ROOT
EOF
cat > %buildroot%_sysconfdir/profile.d/ace-devel.sh <<EOF
ACE_ROOT=/usr/share/ace
export ACE_ROOT
EOF
%if 0%{?_with_tao:1}%{?_without_tao:0}
cat > %buildroot%_sysconfdir/profile.d/tao-devel.sh <<EOF
TAO_ROOT=/usr/share/tao
export TAO_ROOT
EOF
%endif

# convenience symlinks
ln -vsr %_datadir/ace/bin/mpc.pl %buildroot%_bindir/mpc.pl
ln -vsr %_datadir/ace/bin/mwc.pl %buildroot%_bindir/mwc.pl

%add_perl_lib_path %buildroot%_datadir/mpc/modules/Depgen/
%add_perl_lib_path %buildroot%_datadir/mpc/modules/
%add_perl_lib_path %buildroot%_datadir/ace/bin/MakeProjectCreator/modules/
%add_perl_lib_path %buildroot%_datadir/ace/bin/
%add_perl_lib_path %buildroot%_datadir/ace/bin/PerlACE/
%add_perl_lib_path %buildroot%_datadir/ace/bin/PerlACE/MSProject/

# ================================================================
# Manuals
# ================================================================
install -vd %buildroot%_mandir
install -vd %buildroot%_mandir/man1
install -v ${ACE_ROOT}/apps/gperf/ace_gperf.1 %buildroot%_mandir/man1
%if 0%{?_with_tao:1}%{?_without_tao:0}
install -v ${TAO_ROOT}/TAO_IDL/tao_idl.1 %buildroot%_mandir/man1
%endif
install -vd %buildroot%_infodir
install -v ${ACE_ROOT}/apps/gperf/ace_gperf.info %buildroot%_infodir

# ================================================================
# Create lists of symlinked so's.  We need two lists because we need
# the unversioned symlinks in the runtime package for so's that can
# be loaded in the svc.conf.
# ================================================================

# Make a list of all shared objects.
(cd %buildroot/%_libdir && ls *.so | \
        awk '{ print "%_libdir/"$1; }' | \
        sort) > all-so.list

# Make a list of likely svc.conf targets.
(cd %buildroot/%_libdir && ls *.so | \
    nm --print-file-name *.so | \
    grep _make_ | \
    awk 'BEGIN { FS=":"} /^[^:]+:/ { print "%_libdir/"$1; }' | \
    sort -u) > rough-svc-so.list

# Remove false positives (IMPORTANT keep this list sorted!)
cat > falsepos-svc-so.list <<EOF
%_libdir/libACE.so
%_libdir/libTAO.so
EOF
comm -2 -3 rough-svc-so.list falsepos-svc-so.list > svc-so.list

# Find the list of non-sv.conf target files.
comm -2 -3 all-so.list svc-so.list > nonsvc-so.list

# Generate file lists.
grep libACE svc-so.list > ace-svc-so.list
grep libACE nonsvc-so.list > ace-nonsvc-so.list
%if 0%{?_with_tao:1}%{?_without_tao:0}
grep libTAO svc-so.list > tao-svc-so.list
grep libTAO nonsvc-so.list > tao-nonsvc-so.list
%endif

# Concatenate file lists as neccessary
%if 0%{?_with_tao:1}%{?_without_tao:0}
cat tao-headers.list tao-nonsvc-so.list > tao-devel-files.list
%endif
cat ace-headers.list ace-nonsvc-so.list > ace-devel-files.list

# ================================================================
# pre install
# ================================================================

%if 0%{?_with_tao:1}%{?_without_tao:0}

# ---------------- tao-cosnaming ----------------

%pre -n dre-tao-cosnaming
getent group tao >/dev/null || /usr/sbin/groupadd -r tao
getent passwd tao >/dev/null || \
/usr/sbin/useradd -r -g tao -d %_sysconfdir/tao -s /sbin/nologin \
    -c "TAO Services" tao
exit 0

# ---------------- tao-cosevent ----------------

%pre -n dre-tao-cosevent
getent group tao >/dev/null || /usr/sbin/groupadd -r tao
getent passwd tao >/dev/null || \
/usr/sbin/useradd -r -g tao -d %_sysconfdir/tao -s /sbin/nologin \
    -c "TAO Services" tao
exit 0

# ---------------- tao-cosnotification ----------------

%pre -n dre-tao-cosnotification
getent group tao >/dev/null || /usr/sbin/groupadd -r tao
getent passwd tao >/dev/null || \
/usr/sbin/useradd -r -g tao -d %_sysconfdir/tao -s /sbin/nologin \
    -c "TAO Services" tao
exit 0

# ---------------- tao-costrading ----------------

%pre -n dre-tao-costrading
getent group tao >/dev/null || /usr/sbin/groupadd -r tao
getent passwd tao >/dev/null || \
/usr/sbin/useradd -r -g tao -d %_sysconfdir/tao -s /sbin/nologin \
    -c "TAO Services" tao
exit 0

# ---------------- tao-rtevent ----------------

%pre -n dre-tao-rtevent
getent group tao >/dev/null || /usr/sbin/groupadd -r tao
getent passwd tao >/dev/null || \
/usr/sbin/useradd -r -g tao -d %_sysconfdir/tao -s /sbin/nologin \
    -c "TAO Services" tao
exit 0

# ---------------- tao-cosconcurrency ----------------

%pre -n dre-tao-cosconcurrency
getent group tao >/dev/null || /usr/sbin/groupadd -r tao
getent passwd tao >/dev/null || \
/usr/sbin/useradd -r -g tao -d %_sysconfdir/tao -s /sbin/nologin \
    -c "TAO Services" tao
exit 0

%endif

# ================================================================
# post install
# ================================================================

# ---------------- tao-cosnaming ----------------

%post -n dre-tao-cosnaming
/sbin/chkconfig --add tao-cosnaming

# ---------------- tao-cosevent ----------------

%post -n dre-tao-cosevent
/sbin/chkconfig --add tao-cosevent

# ---------------- tao-cosnotification ----------------

%post -n dre-tao-cosnotification
/sbin/chkconfig --add tao-cosnotification

# ---------------- tao-costrading ----------------

%post -n dre-tao-costrading
/sbin/chkconfig --add tao-costrading

# ---------------- tao-rtevent ----------------

%post -n dre-tao-rtevent
/sbin/chkconfig --add tao-rtevent

# ---------------- tao-cosconcurrency ----------------

%post -n dre-tao-cosconcurrency
/sbin/chkconfig --add tao-cosconcurrency

# ================================================================
# pre uninstall
# ================================================================

%if 0%{?_with_tao:1}%{?_without_tao:0}

# ---------------- tao-cosnaming ----------------

%preun -n dre-tao-cosnaming
if [ $1 = 0 ]; then
    /sbin/service tao-cosnaming stop > /dev/null 2>&1
    /sbin/chkconfig --del tao-cosnaming
fi

# ---------------- tao-cosevent ----------------

%preun -n dre-tao-cosevent
if [ $1 = 0 ]; then
    /sbin/service tao-cosevent stop > /dev/null 2>&1
    /sbin/chkconfig --del tao-cosevent
fi

# ---------------- tao-cosnotification ----------------

%preun -n dre-tao-cosnotification
if [ $1 = 0 ]; then
    /sbin/service tao-cosnotification stop > /dev/null 2>&1
    /sbin/chkconfig --del tao-cosnotification
fi

# ---------------- tao-costrading ----------------

%preun -n dre-tao-costrading
if [ $1 = 0 ]; then
    /sbin/service tao-costrading stop > /dev/null 2>&1
    /sbin/chkconfig --del tao-costrading
fi

# ---------------- tao-rtevent ----------------

%preun -n dre-tao-rtevent
if [ $1 = 0 ]; then
    /sbin/service tao-rtevent stop > /dev/null 2>&1
    /sbin/chkconfig --del tao-rtevent
fi

# ---------------- tao-cosconcurrency ----------------

%preun -n dre-tao-cosconcurrency
if [ $1 = 0 ]; then
    /sbin/service tao-cosconcurrency stop > /dev/null 2>&1
    /sbin/chkconfig --del tao-cosconcurrency
fi

%endif

# ================================================================
# post uninstall
# ================================================================

# ---------------- tao-cosnaming ----------------

%postun -n dre-tao-cosnaming
if [ "$1" -ge "1" ]; then
    /sbin/service dre-tao-cosnaming condrestart > /dev/null 2>&1
fi

# ---------------- tao-cosevent ----------------

%postun -n dre-tao-cosevent
if [ "$1" -ge "1" ]; then
    /sbin/service dre-tao-cosevent condrestart > /dev/null 2>&1
fi

# ---------------- tao-cosnotification ----------------

%postun -n dre-tao-cosnotification
if [ "$1" -ge "1" ]; then
    /sbin/service dre-tao-cosnotification condrestart > /dev/null 2>&1
fi

# ---------------- tao-costrading ----------------

%postun -n dre-tao-costrading
if [ "$1" -ge "1" ]; then
    /sbin/service dre-tao-costrading condrestart > /dev/null 2>&1
fi

# ---------------- tao-rtevent ----------------

%postun -n dre-tao-rtevent
if [ "$1" -ge "1" ]; then
    /sbin/service dre-tao-rtevent condrestart > /dev/null 2>&1
fi

# ---------------- tao-cosconcurrency ----------------

%postun -n dre-tao-cosconcurrency
if [ "$1" -ge "1" ]; then
    /sbin/service dre-tao-cosconcurrency condrestart > /dev/null 2>&1
fi

# ================================================================
# files
# ================================================================

# ---------------- ace ----------------

%files -n dre-ace
%_libdir/libACE.so.%ACEVERSO
%_libdir/libACE_ETCL_Parser.so.%ACEVERSO
%_libdir/libACE_ETCL.so.%ACEVERSO
%_libdir/libACE_HTBP.so.%ACEVERSO
%_libdir/libACE_Monitor_Control.so.%ACEVERSO
%_libdir/libACE_RMCast.so.%ACEVERSO
%_libdir/libACE_TMCast.so.%ACEVERSO
%_libdir/libACE_SSL.so.%ACEVERSO
%_libdir/libACE_INet.so.%ACEVERSO
%_libdir/libACE_INet_SSL.so.%ACEVERSO
%_libdir/libACE_Compression.so.%ACEVERSO
%_libdir/libACE_RLECompression.so.%ACEVERSO

%doc AUTHORS
%doc COPYING
%doc PROBLEM-REPORT-FORM
%doc README
%doc VERSION.txt

# ---------------- ace-devel ----------------

%files -n dre-ace-devel -f ace-devel-files.list
%_libdir/libACE_HTBP.so
%_libdir/libACE_SSL.so
%dir %_datadir/ace
%_datadir/ace/include
%_datadir/ace/bin
%_datadir/ace/ace
%_datadir/ace/lib
%config %_sysconfdir/profile.d/ace-devel.sh

%if %{?_with_fox:1}%{!?_with_fox:0}
%exclude %_includedir/ace/FoxReactor/FoxReactor.h
%exclude %_includedir/ace/FoxReactor/ACE_FoxReactor_export.h
%endif
%if %{?_with_fl:1}%{!?_with_fl:0}
%exclude %_includedir/ace/FlReactor/FlReactor.h
%exclude %_includedir/ace/FlReactor/ACE_FlReactor_export.h
%endif
%if %{?_with_qt:1}%{!?_with_qt:0}
%exclude %_includedir/ace/QtReactor/QtReactor.h
%exclude %_includedir/ace/QtReactor/ACE_QtReactor_export.h
%endif
%if %{?_with_tk:1}%{!?_with_tk:0}
%exclude %_includedir/ace/TkReactor/TkReactor.h
%exclude %_includedir/ace/TkReactor/ACE_TkReactor_export.h
%endif
%if %{?_with_xt:1}%{!?_with_xt:0}
%exclude %_includedir/ace/XtReactor/XtReactor.h
%exclude %_includedir/ace/XtReactor/ACE_XtReactor_export.h
%endif
%exclude %_libdir/libACEXML*.so

# ---------------- ace-xml ----------------

%files -n dre-ace-xml
%_libdir/libACEXML*.so.%ACEVERSO

# ---------------- ace-gperf ----------------

%files -n dre-ace-gperf
%_bindir/ace_gperf
%attr(0644,root,root) %_mandir/man1/ace_gperf.1%_extension
%attr(0644,root,root) %_infodir/ace_gperf.info%_extension

# ---------------- ace-xml-devel ----------------

%files -n dre-ace-xml-devel -f acexml-headers.list
%_libdir/libACEXML*.so

# These get missed by the automatic list generator because they
# contain no immediate files.
%dir %_includedir/ACEXML/parser
%dir %_includedir/ACEXML

# ---------------- ace-kokyu ----------------

%files -n dre-ace-kokyu
%_libdir/libKokyu.so.%ACEVERSO

# ---------------- ace-kokyu-devel ----------------

%files -n dre-ace-kokyu-devel -f kokyu-headers.list
%_libdir/libKokyu.so

# ---------------- ace-foxreactor ----------------

%if 0%{?have_fox} == 1
%if %{?_with_fox:1}%{!?_with_fox:0}
%files -n dre-ace-foxreactor
%_libdir/libACE_FoxReactor.so.%ACEVERSO

%endif
%endif
# ---------------- ace-flreactor ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}

%files -n dre-ace-flreactor
%_libdir/libACE_FlReactor.so.%ACEVERSO

%endif

# ---------------- ace-flreactor-devel ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}

%files -n dre-ace-flreactor-devel
%dir %_includedir/ace/FlReactor
%_libdir/libACE_FlReactor.so
%_includedir/ace/FlReactor/FlReactor.h
%_includedir/ace/FlReactor/ACE_FlReactor_export.h

%endif

# ---------------- ace-qtreactor ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}

%files -n dre-ace-qtreactor
%_libdir/libACE_QtReactor.so.%ACEVERSO

%endif

# ---------------- ace-qtreactor-devel ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}

%files -n dre-ace-qtreactor-devel
%_libdir/libACE_QtReactor.so
%dir %_includedir/ace/QtReactor
%_includedir/ace/QtReactor/QtReactor.h
%_includedir/ace/QtReactor/ACE_QtReactor_export.h

%endif

# ---------------- ace-tkreactor ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}

%files -n dre-ace-tkreactor
%_libdir/libACE_TkReactor.so.%ACEVERSO

%endif

# ---------------- ace-tkreactor-devel ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}

%files -n dre-ace-tkreactor-devel
%_libdir/libACE_TkReactor.so
%dir %_includedir/ace/TkReactor
%_includedir/ace/TkReactor/TkReactor.h
%_includedir/ace/TkReactor/ACE_TkReactor_export.h

%endif

# ---------------- ace-xtreactor ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}

%files -n dre-ace-xtreactor
%_libdir/libACE_XtReactor.so.%ACEVERSO

%endif

# ---------------- ace-xtreactor-devel ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}

%files -n dre-ace-xtreactor-devel
%_libdir/libACE_XtReactor.so
%dir %_includedir/ace/XtReactor
%_includedir/ace/XtReactor/XtReactor.h
%_includedir/ace/XtReactor/ACE_XtReactor_export.h

%endif

# ---------------- mpc ----------------

%files -n dre-mpc
%_datadir/mpc
%config %_sysconfdir/profile.d/mpc.sh
%_bindir/mpc.pl
%_bindir/mwc.pl

# ---------------- tao ----------------

%if 0%{?_with_tao:1}%{?_without_tao:0}

# NOTE - Some of the TAO service modules need to be found by dlopen at
# runtime.  Currently this means these specific .so files need to be
# shipped in the runtime package instead of the devel package.

%files -n dre-tao -f tao-svc-so.list
%_datadir/tao
%exclude %_datadir/tao/MPC
%exclude %_datadir/tao/tao
%exclude %_datadir/tao/orbsvcs

%_libdir/libTAO*.so.%TAOVERSO

%if %{?_with_fl:1}%{!?_with_fl:0}
%exclude %_libdir/libTAO_FlResource.so*
%endif
%if %{?_with_qt:1}%{!?_with_qt:0}
%exclude %_libdir/libTAO_QtResource.so*
%endif
%if %{?_with_tk:1}%{!?_with_tk:0}
%exclude %_libdir/libTAO_TkResource.so*
%endif
%if %{?_with_xt:1}%{!?_with_xt:0}
%exclude %_libdir/libTAO_XtResource.so*
%endif

%doc TAO/COPYING
%doc TAO/PROBLEM-REPORT-FORM
%doc TAO/TAO-INSTALL.html
%doc TAO/VERSION.txt
%doc TAO/README

# ---------------- tao-devel ----------------

# NOTE - Some of the TAO service modules need to be found by dlopen() at
# runtime. Currently this means these specific .so files need to be
# shipped in the runtime package instead of the development package.

%files -n dre-tao-devel -f tao-devel-files.list
%config %_sysconfdir/profile.d/tao-devel.sh

%_bindir/tao_imr
%_bindir/tao_ifr
%_bindir/tao_ifr_service
%_datadir/tao/MPC
%_bindir/tao_idl
%attr(0644,root,root) %doc %_mandir/man1/tao_idl.1%_extension
%_datadir/tao/tao
%_datadir/tao/orbsvcs

# These get missed by the automatic list generator because they
# contain no immediate files.
%dir %_includedir/orbsvcs/FtRtEvent

%if %{?_with_fl:1}%{!?_with_fl:0}
%exclude %_includedir/tao/FlResource/FlResource_Factory.h
%exclude %_includedir/tao/FlResource/FlResource_Loader.h
%exclude %_includedir/tao/FlResource/TAO_FlResource_Export.h
%exclude %_libdir/libTAO_FlResource.so
%endif
%if %{?_with_qt:1}%{!?_with_qt:0}
%exclude %_includedir/tao/QtResource/QtResource_Factory.h
%exclude %_includedir/tao/QtResource/QtResource_Loader.h
%exclude %_includedir/tao/QtResource/TAO_QtResource_Export.h
%exclude %_libdir/libTAO_QtResource.so
%endif
%if %{?_with_tk:1}%{!?_with_tk:0}
%exclude %_includedir/tao/TkResource/TkResource_Factory.h
%exclude %_includedir/tao/TkResource/TkResource_Loader.h
%exclude %_includedir/tao/TkResource/TAO_TkResource_Export.h
%exclude %_libdir/libTAO_TkResource.so
%endif
%if %{?_with_xt:1}%{!?_with_xt:0}
%exclude %_includedir/tao/XtResource/XtResource_Factory.h
%exclude %_includedir/tao/XtResource/XtResource_Loader.h
%exclude %_includedir/tao/XtResource/TAO_XtResource_Export.h
%exclude %_libdir/libTAO_XtResource.so
%endif

# ---------------- tao-utils ----------------

%files -n dre-tao-utils
%_bindir/tao_catior
%_bindir/tao_nsadd
%_bindir/tao_nsdel
%_bindir/tao_nslist

%doc TAO/utils/catior/README.catior
%doc TAO/utils/nslist/README.nslist

# ---------------- tao-cosnaming ----------------

%files -n dre-tao-cosnaming
%dir %_sysconfdir/tao

%_sbindir/tao-cosnaming

%_initdir/tao-cosnaming
%config(noreplace) %_sysconfdir/tao/tao-cosnaming.opt

%config(noreplace) %_sysconfdir/tao/tao-cosnaming.conf
%config(noreplace) %_sysconfdir/logrotate.d/tao-cosnaming
%attr(-,tao,tao) %dir %_cachedir/tao
%attr(0644,tao,tao) %ghost %_cachedir/tao/tao-cosnaming.dat
%attr(-,tao,tao) %dir %_logdir/tao
%attr(0644,tao,tao) %ghost %_logdir/tao/tao-cosnaming.log

# ---------------- tao-cosevent ----------------

%files -n dre-tao-cosevent
%dir %_sysconfdir/tao
%_sbindir/tao-cosevent

%_initdir/tao-cosevent
%config(noreplace) %_sysconfdir/tao/tao-cosevent.opt

%config(noreplace) %_sysconfdir/tao/tao-cosevent.conf
%config(noreplace) %_sysconfdir/logrotate.d/tao-cosevent
%attr(-,tao,tao) %dir %_logdir/tao
%attr(0644,tao,tao) %ghost %_logdir/tao/tao-cosevent.log

# ---------------- tao-cosnotification ----------------

%files -n dre-tao-cosnotification
%_sbindir/tao-cosnotification
%dir %_sysconfdir/tao

%_initdir/tao-cosnotification
%config(noreplace) %_sysconfdir/tao/tao-cosnotification.opt

%config(noreplace) %_sysconfdir/tao/tao-cosnotification.conf
%config(noreplace) %_sysconfdir/logrotate.d/tao-cosnotification
%attr(-,tao,tao) %dir %_logdir/tao
%attr(0644,tao,tao) %ghost %_logdir/tao/tao-cosnotification.log

# ---------------- tao-costrading ----------------

%files -n dre-tao-costrading
%dir %_sysconfdir/tao

%_sbindir/tao-costrading

%_initdir/tao-costrading
%config(noreplace) %_sysconfdir/tao/tao-costrading.opt

%config(noreplace) %_sysconfdir/tao/tao-costrading.conf
%config(noreplace) %_sysconfdir/logrotate.d/tao-costrading
%attr(-,tao,tao) %dir %_logdir/tao
%attr(0644,tao,tao) %ghost %_logdir/tao/tao-costrading.log

# ---------------- tao-rtevent ----------------

%files -n dre-tao-rtevent
%dir %_sysconfdir/tao
%_sbindir/tao-rtevent

%_initdir/tao-rtevent
%config(noreplace) %_sysconfdir/tao/tao-rtevent.opt

%config(noreplace) %_sysconfdir/tao/tao-rtevent.conf
%config(noreplace) %_sysconfdir/logrotate.d/tao-rtevent
%attr(-,tao,tao) %dir %_logdir/tao
%attr(0644,tao,tao) %ghost %_logdir/tao/tao-rtevent.log

# ---------------- tao-cosconcurrency ----------------

%files -n dre-tao-cosconcurrency
%dir %_sysconfdir/tao
%_sbindir/tao-cosconcurrency

%_initdir/tao-cosconcurrency
%config(noreplace) %_sysconfdir/tao/tao-cosconcurrency.opt

%config(noreplace) %_sysconfdir/tao/tao-cosconcurrency.conf
%config(noreplace) %_sysconfdir/logrotate.d/tao-cosconcurrency
%attr(-,tao,tao) %dir %_logdir/tao
%attr(0644,tao,tao) %ghost %_logdir/tao/tao-cosconcurrency.log

# ---------------- tao-flresource ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}

%files -n dre-tao-flresource
%_libdir/libTAO_FlResource.so.%TAOVERSO

%endif

# ---------------- tao-flresource-devel ----------------

%if %{?_with_fl:1}%{!?_with_fl:0}

%files -n dre-tao-flresource-devel
%_libdir/libTAO_FlResource.so
%dir %_includedir/tao
%_includedir/tao/FlResource/FlResource_Factory.h
%_includedir/tao/FlResource/FlResource_Loader.h
%_includedir/tao/FlResource/TAO_FlResource_Export.h

%endif

# ---------------- tao-qtresource ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}

%files -n dre-tao-qtresource
%_libdir/libTAO_QtResource.so.%TAOVERSO

%endif

# ---------------- tao-qtresource-devel ----------------

%if %{?_with_qt:1}%{!?_with_qt:0}

%files -n dre-tao-qtresource-devel
%_libdir/libTAO_QtResource.so
%dir %_includedir/tao
%_includedir/tao/QtResource/QtResource_Factory.h
%_includedir/tao/QtResource/QtResource_Loader.h
%_includedir/tao/QtResource/TAO_QtResource_Export.h

%endif

# ---------------- tao-tkresource ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}

%files -n dre-tao-tkresource
%_libdir/libTAO_TkResource.so.%TAOVERSO

%endif

# ---------------- tao-tkresource-devel ----------------

%if %{?_with_tk:1}%{!?_with_tk:0}

%files -n dre-tao-tkresource-devel
%_libdir/libTAO_TkResource.so
%dir %_includedir/tao
%_includedir/tao/TkResource/TkResource_Factory.h
%_includedir/tao/TkResource/TkResource_Loader.h
%_includedir/tao/TkResource/TAO_TkResource_Export.h

%endif

# ---------------- tao-xtresource ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}

%files -n dre-tao-xtresource
%_libdir/libTAO_XtResource.so.%TAOVERSO

%endif

# ---------------- tao-xtresource-devel ----------------

%if %{?_with_xt:1}%{!?_with_xt:0}

%files -n dre-tao-xtresource-devel
%_libdir/libTAO_XtResource.so
%dir %_includedir/tao
%_includedir/tao/XtResource/XtResource_Factory.h
%_includedir/tao/XtResource/XtResource_Loader.h
%_includedir/tao/XtResource/TAO_XtResource_Export.h

%endif

%endif

%changelog
* Fri Oct 28 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 8.0.1-alt2
- spec clean up
  add init.d files for alt

* Tue Aug 06 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 8.0.1-alt1
- new version

* Thu Jun 06 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 8.0.0-alt1
- new version

* Mon Apr 15 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.1.4-alt1
- new version

* Mon Feb 19 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.1.3-alt1
- new version

* Fri Sep 01 2023 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.1.1-alt1
- Initial build for ALT Linux Sisyphus (closes: 45123)

* Fri Jan 31 2014 Steve Huston <shuston@riverace.com> 6.2.5
- Added rpmbuild options "--with tao" and "--without tao"; defaults to 'with'.
  Allows building ACE only (--without tao)

* Thu Aug 11 2011 Thomas Lockhart <lockhart@fourpalms.org> 6.0.3-54
- Parameterize code inlining. Defaults to not inlining which was the previous behavior.
- Implement the rpmbuild options "--with inline" and "--without inline".

