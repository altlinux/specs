Name: unimrcp
Version: 1.0.0
Release: alt2

Summary: Media Resource Control Protocol Stack
License: Apache
Group: System/Libraries
Url: http://unimrcp.org

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: libexpat-devel
BuildRequires: flite-devel >= 1.3.9
BuildRequires: libapr1-devel >= 1.3.6 libaprutil1-devel >= 1.3.6
BuildRequires: libsofia-sip-devel

%description
Media Resource Control Protocol (MRCP) allows to control media processing
resources over the network using distributed client/server architecture.
Media processing resources include:
- Speech Synthesizer (TTS)
- Speech Recognizer (ASR) 
- Speaker Verifier (SV)
- Speech Recorder (SR)
MRCP is not a stand alone protocol and it relies on various VoIP protocols
such as:
- SIP (MRCPv2), RTSP (MRCPv1) session management
- SDP offer/answer model
- RTP media streaming
UniMRCP is an open source cross-platform MRCP implementation, which provides
everything required for MRCP client and server side deployment.
UniMRCP encapsulates SIP/MRCPv2, RTSP, SDP and RTP stacks inside and provides
MRCP version independent user level interface for the integration.

%package -n libunimrcp
Summary: Media Resource Control Protocol Stack shared librarries
Group: System/Libraries

%package -n libunimrcp-devel
Summary: Media Resource Control Protocol Stack development
Group: Development/C
Requires: libunimrcp = %version-%release

%description -n libunimrcp
UniMRCP is an open source cross-platform MRCP implementation, which provides
everything required for MRCP client and server side deployment.
UniMRCP encapsulates SIP/MRCPv2, RTSP, SDP and RTP stacks inside and provides
MRCP version independent user level interface for the integration.
This package contains UniMRCP shared libraries

%description -n libunimrcp-devel
UniMRCP is an open source cross-platform MRCP implementation, which provides
everything required for MRCP client and server side deployment.
UniMRCP encapsulates SIP/MRCPv2, RTSP, SDP and RTP stacks inside and provides
MRCP version independent user level interface for the integration.
This package contains development part of UniMRCP.

%prep
%setup

%build
[ ! -x ./bootstrap ] || ./bootstrap
%configure \
    --datadir=%_datadir/%name \
    --includedir=%_includedir/unimrcp \
    --localstatedir=%_var \
    --enable-flite-plugin \
    --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%dir %_sysconfdir/unimrcp
%dir %_sysconfdir/unimrcp/client-profiles
%config(noreplace) %_sysconfdir/unimrcp/logger.xml
%config(noreplace) %_sysconfdir/unimrcp/unimrcpclient.xml
%config(noreplace) %_sysconfdir/unimrcp/unimrcpclient.xsd
%config(noreplace) %_sysconfdir/unimrcp/unimrcpserver.xml
%config(noreplace) %_sysconfdir/unimrcp/unimrcpserver.xsd
%config(noreplace) %_sysconfdir/unimrcp/umcscenarios.xml
%config(noreplace) %_sysconfdir/unimrcp/client-profiles/lumenvox.xml
%config(noreplace) %_sysconfdir/unimrcp/client-profiles/nuance.xml
%config(noreplace) %_sysconfdir/unimrcp/client-profiles/unimrcp.xml

%_bindir/asrclient
%_bindir/unimrcpclient
%_bindir/unimrcpserver
%_bindir/umc

%_libdir/unimrcp

%_datadir/unimrcp

%files -n libunimrcp
%_libdir/libasrclient.so.*
%_libdir/libunimrcpclient.so.*
%_libdir/libunimrcpserver.so.*

%files -n libunimrcp-devel
%_includedir/unimrcp

%_libdir/libasrclient.so
%_libdir/libunimrcpclient.so
%_libdir/libunimrcpserver.so

%_pkgconfigdir/unimrcpclient.pc
%_pkgconfigdir/unimrcpplugin.pc
%_pkgconfigdir/unimrcpserver.pc

%changelog
* Mon May 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt2
- explicitly link binaries with apr libraries

* Wed Aug 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Sat Feb 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- 0.9.0 released

* Tue Aug  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 released

* Mon Jul 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- Initial build.
