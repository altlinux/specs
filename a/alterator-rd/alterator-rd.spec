%define _altdata_dir %_datadir/alterator
%def_without citrix
%def_without nx

Name: alterator-rd
Version: 0.0.3
Release: alt2
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for remote desktop
Packager: Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %name-%version.tar

Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: alterator-l10n >= 2.7-alt10
BuildPreReq: alterator >= 4.10-alt8
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for configure remote desktop

%package vnc
Requires: %name == %version-%release
Requires: tigervnc
Summary: VNC support
Group: System/Configuration/Other

%description vnc
Add support for VNC protocol

%if_with citrix
%package citrix
Requires: %name == %version-%release
Requires: citrix-client
Summary: Citrix ICA support
Group: System/Configuration/Other

%description citrix
Add support for Citrix ICA protocol
%endif

%package rdesktop
Requires: %name == %version-%release
Requires: rdesktop
Summary: rdesktop support
Group: System/Configuration/Other

%description rdesktop
Add support for RDP (rdesktop) protocol

%package freerdp
Requires: %name == %version-%release
Requires: xfreerdp
Summary: freerdp support
Group: System/Configuration/Other

%description freerdp
Add support for RDP (freerdp) protocol

%package url
Requires: %name == %version-%release
Requires: xdg-utils
Summary: Open URL in WWW browser
Group: System/Configuration/Other

%description url
Open URL using xdg-utils

%if_with nx
%package nx
Requires: %name == %version-%release
Requires: nxclient
Summary: NoMachine support
Group: System/Configuration/Other

%description nx
Add support for NX protocol
%endif

%package xdmcp
Requires: %name == %version-%release
Requires: xorg-xnest
Summary: xdmcp support
Group: System/Configuration/Other

%description xdmcp
Add support for xdmcp support

%package ssh
Requires: %name == %version-%release
Summary: SSH support
Group: System/Configuration/Other
Requires: sshpass gtk2-ssh-askpass x11-ssh-askpass

%description ssh
Remote desktop alterator module for SSH support

%package all
Requires: %name-vnc == %version-%release
%if_with citrix
Requires: %name-citrix == %version-%release
%endif
Requires: %name-rdesktop == %version-%release
Requires: %name-freerdp == %version-%release
Requires: %name-url == %version-%release
%if_with nx
Requires: %name-nx == %version-%release
%endif
Requires: %name-xdmcp == %version-%release
Requires: %name-ssh == %version-%release
Summary: All remote protocols
Group: System/Configuration/Other

%description all
Meta-package to to include all available remote protocols

# set_findreq_skiplist _bindir/rd-nx
# add_findreq_skiplist _libdir/debug/usr/lib/libpcoip_client.so*

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/rd
%_altdata_dir/applications/rd-users.desktop
%_altdata_dir/ui/rd_users
%_altdata_dir/desktop-directories/*
%_bindir/rd-xsession
%_bindir/rd-list-profiles
%_bindir/rd-profile-info

%files vnc
%_altdata_dir/applications/rd-tigervnc.desktop
%_altdata_dir/ui/rd_tigervnc
%_alterator_backend3dir/rd_tigervnc
%_bindir/rd-tigervnc

%if_with citrix
%files citrix
%_altdata_dir/applications/rd-citrix.desktop
%_altdata_dir/ui/rd_citrix
%_alterator_backend3dir/rd_citrix
%_bindir/rd-citrix
%endif

%files rdesktop
%_altdata_dir/applications/rd-rdesktop.desktop
%_altdata_dir/ui/rd_rdesktop
%_alterator_backend3dir/rd_rdesktop
%_bindir/rd-rdesktop

%files freerdp
%_altdata_dir/applications/rd-freerdp.desktop
%_altdata_dir/ui/rd_freerdp
%_alterator_backend3dir/rd_freerdp
%_bindir/rd-freerdp

%files url
%_altdata_dir/applications/rd-url.desktop
%_altdata_dir/ui/rd_url
%_alterator_backend3dir/rd_url
%_bindir/rd-url

%if_with nx
%files nx
%_altdata_dir/applications/rd-nx.desktop
%_altdata_dir/ui/rd_nx
%_alterator_backend3dir/rd_nx
%_bindir/rd-nx
%endif

%files xdmcp
%_altdata_dir/applications/rd-xdmcp.desktop
%_altdata_dir/ui/rd_xdmcp
%_alterator_backend3dir/rd_xdmcp
%_bindir/rd-xdmcp

%files ssh
%_altdata_dir/applications/rd-ssh.desktop
%_altdata_dir/ui/rd_ssh
%_alterator_backend3dir/rd_ssh
%_bindir/rd-ssh

%files all

%changelog
* Tue Jul 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.0.3-alt2
- Rebuild by cas@
- Optional build Citrix and NX support
- Disable Citrix and NX support (no package cotrix-client and nxclient)

* Tue Jan 15 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- Manage Citrix certificates

* Mon Jun 04 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- Split package to individual for each protocol

* Mon Apr 09 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt2
- Remove autologin

* Wed Feb 29 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build
