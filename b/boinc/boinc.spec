Name:		boinc
Version: 7.8.4
Release: alt2
Packager: Ilya Mashkin <oddity@altlinux.ru>
License:	GPLv3+/LGPLv3+
Group:		Sciences/Other
URL:		http://boinc.berkeley.edu/
Summary:	The Berkeley Open Infrastructure for Network Computing

Source0:	%name-%version.tar.gz
Source1:	%name-conffiles-%version.tar

#Patch1:		texfont_removal.patch
#Patch2:		no-string-overload.patch
Patch3:		install-examples.patch
Patch4:		install-translations.patch
Patch7:		install-init-script.patch
Patch8:		alt-service-actions.patch
Patch9:		fix-boinc-client-service.patch
Patch10:	README.patch
#Patch13:	fix-wxEvtHandler-access.patch
#Patch15:	fix-wxString-cast.patch
#Patch16:	wx-postponed.patch
Patch17:	libadds.patch
#Patch18:	serverbindir.patch
Patch19:	install-py.patch
#Patch20:	totalGlobalMem.patch
Patch21:	make_clientgui_resources.patch
#Patch22:	refactor_sched_vda.patch
Patch23:	install_appmgr.patch
Patch24:  boinc-7.0.31-alt-glibc-2.16.patch

Patch25: boinc-7.4.42-alt-wxGTK3.1.patch
Patch26: boinc-7.4.42-alt-gtk3.patch
Patch27: boinc-7.8.4-alt-glibc.patch

# Use def_with server to enable it
%def_without server

BuildRequires: docbook-dtds docbook2X gcc-c++ gcc-fortran libGL-devel libMySQL-devel libSM-devel libXi-devel libXmu-devel libcurl-devel libfreeglut-devel libjpeg-devel libsqlite3-devel libstdc++-devel-static python-devel xsltproc libssl-devel zlib-devel libgtk+3-devel libnotify-devel
BuildRequires: libwxGTK3.1-devel

%description
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

Install the %name-client package to participate in a number of scientific
projects.

%if_with server
Install the %name-server package to host a computational project.

Install the %name-demo package to view sample projects.
%endif
Use the %name-devel package files in development of a new computational
project.

%package client
Group:		Sciences/Other
Summary:	Client software for the Berkeley Open Infrastructure for Network Computing

Requires:	%{name} = %{version}-%{release}

%description client
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package installs the BOINC client software, which will allow your
computer to participate in one or more BOINC projects, using your spare
computer time to search for cures for diseases, model protein folding, study
global warming, discover sources of gravitational waves, and many other types
of scientific and mathematical research.

%package manager
Summary:	GUI to control and monitor the BOINC system
Group:		Sciences/Other

Requires:	%{name}-client = %{version}-%{release}

%description manager
The BOINC Manager is a graphical monitor and control utility for the BOINC
core client. It gives a detailed overview of the state of the client it is
monitoring. The BOINC Manager has two modes of operation, the "Simple View" in
which it only displays the most important information and the "Advanced View"
in which all information and all control elements are available.

%package manager-skins
Summary:	Skins for the BOINC Manager GUI
Group:		Sciences/Other

Requires:	%{name}-manager = %{version}-%{release}
BuildArch: noarch

%description manager-skins
The BOINC Manager is a graphical monitor and control utility for the BOINC
core client. It gives a detailed overview of the state of the client it is
monitoring. The BOINC Manager has two modes of operation, the "Simple View" in
which it only displays the most important information and the "Advanced View"
in which all information and all control elements are available.

This package contains skin files to style the GUI.

%package devel
Summary:	Development files for BOINC system
Group:		Development/C
Requires: lib%name = %version-%release

%description devel
This package contains development files for the Berkeley Open
Infrastructure for Network Computing.

%package server-devel
Summary:	Server development files for BOINC system
Group:		Development/C
Requires: lib%name = %version-%release

%description server-devel
This package contains development files for the Berkeley Open
Infrastructure for Network Computing server components.

%package doc
Summary:	Documentation files for BOINC system
Group:		Sciences/Other
BuildArch:	noarch

Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Berkeley Open
Infrastructure for Network Computing.

%package server
Group:		Sciences/Other
Summary:	Server software for the Berkeley Open Infrastructure for Network Computing

Requires:	%{name} = %{version}-%{release}

%description server
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package installs the BOINC server software. The BOINC server is
intended to be a central communicational node for the number of
distributed computational projects. This includes program distribution,
project status tracking, data distributing, result acquiring and more.

%package demo
Group:      Sciences/Other
Summary:    Sample projects for the Berkeley Open Infrastructure for Network Computing
Requires:   %{name}-server = %{version}-%{release}

%description demo
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package installs a number of sample projects for the BOINC server
software.

%package -n lib%name
Group:      Sciences/Other
Summary:    Libraries of the Berkeley Open Infrastructure for Network Computing

%description -n lib%name
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package contains a set of libraires of the BOINC software.

%package -n lib%name-server
Group:      Sciences/Other
Summary:    Server libraries of the Berkeley Open Infrastructure for Network Computing
Requires: lib%name = %version-%release

%description -n lib%name-server
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package contains a set of server libraires of the BOINC software.

%prep
%setup -b1
#%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch13 -p1
#%patch15 -p1
#%patch16 -p1
%patch17 -p2
#%patch18 -p1
%patch19 -p1
#%patch20 -p2
%patch21 -p2
#%patch22 -p2
%patch23 -p2
%patch24 -p2
%patch25 -p0
#%patch26 -p0
%patch27 -p2

# Do not use /usr/bin/env in PHP scripts.
grep -rHsl -m 1 -e 'bin/env' html/* |
    while read f; do
        sed -e '1 s,^#!/usr/bin/env[[:space:]]\+\(.*\)$,#!/usr/bin/\1,' -i "$f"
    done

# Copy the icons to the expected place
cp -vf packages/generic/sea/boincmgr.*.png clientgui/res/

%build
# On some architectures it is required to change the BOINC platform of the
# core client (with the --with-boinc-platform configure option) to match the
# official BOINC platform, otherwise it would not download any applications,
# because projects mostly provide applications for official BOINC platforms
# only. See http://boinc.berkeley.edu/trac/wiki/BoincPlatforms for the list
# of official BOINC platforms.
TYPE_FLAGS=
case %_target in
    i?86-linux|pentium?-linux)
        TYPE_FLAGS="$TYPE_FLAGS --with-boinc-platform=i686-pc-linux-gnu"
        ;;
    x86_64-linux)
        TYPE_FLAGS="$TYPE_FLAGS --with-boinc-platform=x86_64-pc-linux-gnu"
        ;;
    else)
        echo "Can't find the corresponding BOINC platform for %_target. See http://boinc.berkeley.edu/trac/wiki/BoincPlatforms for details."
        exit -1
        ;;
esac

# Build script
%autoreconf
#./_autosetup
%configure $TYPE_FLAGS CXXFLAGS=-std=gnu++11 \
    --enable-client \
%if_with server
    --enable-server  \
%else
    --disable-server \
%endif
    --enable-unicode \
    --with-ssl
%make V=1

# Generate binary message catalogs of the BOINC Manager.
#	for i in `ls locale/client`; do \
#	  if [ -f "locale/client/$i/BOINC Manager.po" ]; then \
#	    msgfmt -o "locale/client/$i/BOINC Manager.mo" \
#	      "locale/client/$i/BOINC Manager.po"; \
#	  fi; \
#	done;

# Make the manpages
pushd doc/manpages
%make DOCBOOK2X_MAN=db2x_docbook2man
popd

%install
%make DESTDIR=%buildroot \
      prefix=%{_usr} \
      exec_prefix=%{_usr} \
      bindir=%{_bindir} \
      sbindir=%{_sbindir} \
      sysconfdir=%{_sysconfdir} \
      initrddir=%_initrddir \
      datadir=%{_datadir} \
      includedir=%{_includedir} \
      libdir=%{_libdir} \
      libexecdir=%{_libexecdir} \
      localstatedir=%{_localstatedir} \
      sharedstatedir=%{_sharedstatedir} \
      mandir=%{_mandir} \
      infodir=%{_infodir} \
      scheddir=%{_libexecdir}/%name-server/sched \
      serverbindir=%{_libexecdir}/%name-server/bin \
      cgidir=%{_libexecdir}/%name-server/cgi-bin \
      python_sitelibdir=%{python_sitelibdir} \
      install

# Bash completion script for boinccmd.
    install -D -m0644 ../%name-conffiles-%version/bash/boinc \
      %buildroot%{_sysconfdir}/bash_completion.d/boinc

# Install BOIC client default configuration files
#    install -D -m 0644 ../%name-conffiles-%version/cc_config.xml \
#      %buildroot%{_sysconfdir}/boinc-client/cc_config.xml
#    install -D -m 0644 ../%name-conffiles-%version/global_prefs_override.xml \
#      %buildroot%{_sysconfdir}/boinc-client/global_prefs_override.xml
#    install -D -m 0644 ../%name-conffiles-%version/gui_rpc_auth.cfg \
#      %buildroot%{_sysconfdir}/boinc-client/gui_rpc_auth.cfg
    install -D -m 0644 ../%name-conffiles-%version/remote_hosts.cfg \
       %buildroot%_localstatedir/boinc/remote_hosts.cfg
#      %buildroot%{_sysconfdir}/boinc-client/remote_hosts.cfg

# Install the icons.
install -m0644 -D clientgui/res/boincmgr.16x16.png %buildroot%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
install -m0644 -D clientgui/res/boincmgr.32x32.png %buildroot%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
install -m0644 -D clientgui/res/boincmgr.48x48.png %buildroot%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png

# Install the desktop and menu files
    install -D -m 0644 ../%name-conffiles-%version/boinc-manager.desktop \
      %buildroot%{_datadir}/applications/boinc-manager.desktop

# Install common links to the executables
    ln -s boinc_client %buildroot%{_bindir}/boinc-client
    rm -f %buildroot%{_bindir}/boinc
    ln -s boinc_client %buildroot%{_bindir}/boinc
    mv %buildroot%{_bindir}/{,boinc_}switcher
    ln -s boinc_switcher %buildroot%{_bindir}/boinc-switcher

# Create boinc user home directory
    mkdir -p -m 0750 %buildroot%{_localstatedir}/boinc

%if_with server
# Install the PHP part of the server.
    mkdir -p -m 0755 %buildroot%{_datadir}/%name-server/html
    cp -Rp html/* %buildroot%{_datadir}/%name-server/html/

# Install database files.
    install -d -m 0755 %buildroot%{_datadir}/%name-server/db
    install -m 0644 db/*.sql %buildroot%{_datadir}/%name-server/db/
    install -m 0644 db/init_db %buildroot%{_datadir}/%name-server/db/init-db
%endif

# Install the documentation
	install -D -m 0644 COPYING %buildroot%{_docdir}/%name-%version/COPYING
	install -D -m 0644 COPYING.LESSER %buildroot%{_docdir}/%name-%version/COPYING.LESSER
	install -D -m 0644 COPYRIGHT %buildroot%{_docdir}/%name-%version/COPYRIGHT
	install -D -m 0644 README.ALT %buildroot%{_docdir}/%name-%version/README.ALT

# Install the manpages
pushd doc/manpages
%makeinstall
	ln -s boinc.1 %buildroot%{_man1dir}/boinc-client.1
popd

# Install BOINC Manager skins
pushd clientgui/skins
mkdir -p -m0755 %buildroot%_datadir/boinc/skins
find | while read f; do \
	if [ -d "$f" ]; then \
		mkdir -p -m0755 "%buildroot%_datadir/boinc/skins/${f#./}"; \
	else case "$f" in \
		*.png|*.xml) \
			install -D -m0644 "$f" "%buildroot%_datadir/boinc/skins/${f#./}";; \
	esac; fi; \
done
popd

%find_lang BOINC-Client
%find_lang BOINC-Manager 

%pre client

# Create BOINC user and group
getent group boinc >/dev/null || groupadd -r boinc
getent passwd boinc >/dev/null || \
useradd -r -g boinc -d %{_localstatedir}/boinc -s /sbin/nologin \
	-c "BOINC client account." boinc

%post client
/sbin/chkconfig --add boinc-client
# Don't install ca-bundle.crt from BOINC, and keep the system using
# the ca-bundle.crt provided by ca-certificates.
    if ! [ -L %{_localstatedir}/boinc/ca-bundle.crt ]; then
        ln -s %{_datadir}/ca-certificates/ca-bundle.crt \
          %{_localstatedir}/boinc/ca-bundle.crt
    fi
chown -R boinc:boinc %{_localstatedir}/boinc

%preun client
if [ $1 -eq 0 ]; then #if uninstalling, not only updating
	/sbin/service boinc-client stop
	/sbin/chkconfig --del boinc-client
fi

%if_with server
%post server
getent group boincadm >/dev/null || groupadd -r boincadm
%endif

%files
%dir %{_datadir}/boinc
%dir %{_docdir}/%name-%version
%doc %{_docdir}/%name-%version/COPYING
%doc %{_docdir}/%name-%version/COPYING.LESSER
%doc %{_docdir}/%name-%version/COPYRIGHT
%doc %{_docdir}/%name-%version/README.ALT

# OpenCL procs are platform-dependent and thus are left undefined...
%add_verify_elf_skiplist %_libdir/libboinc_opencl.so*

%files -n libboinc
%{_libdir}/libboinc*.so.*
%exclude %_libdir/libboinc_opencl.so.*

%if_with server

%files -n libboinc-server
%{_libdir}/libsched.so.*

%files demo
%{_libexecdir}/boinc-apps-examples/*

%files server
%dir %{_libexecdir}/boinc-server
%_libexecdir/boinc-server-maker
%dir %{_libexecdir}/boinc-apps-examples
%dir %{_libexecdir}/boinc-server/bin
%{_libexecdir}/boinc-server/bin/*
%dir %{_libexecdir}/boinc-server
%{_libexecdir}/boinc-server/sched
%{_libexecdir}/boinc-server/bin
%dir %{_datadir}/boinc-server
%{_datadir}/boinc-server/html
%dir %{_datadir}/%name-server/db
%{_datadir}/%name-server/db/*.sql
%{_datadir}/%name-server/db/init-db
%dir %{python_sitelibdir}/Boinc
%{python_sitelibdir}/Boinc/*.py*
%{python_sitelibdir}/boinc_path_config.py*
%{python_sitelibdir}/Boinc-%version-py*.egg-info
%_mandir/man8/appmgr.8.gz
%_datadir/boinc-server-maker

%files server-devel
%exclude %{_libdir}/libsched.a
%{_libdir}/libsched.so

%endif

%files client -f BOINC-Client.lang
%{_sysconfdir}/bash_completion.d/boinc
#%dir %{_sysconfdir}/boinc-client
#%config(noreplace) %{_sysconfdir}/boinc-client/*.xml
#%config(noreplace) %{_sysconfdir}/boinc-client/*.cfg
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/sysconfig/boinc-client
%{_initrddir}/boinc-client
%{_bindir}/boinc_client
%{_bindir}/boinc
#%{_bindir}/boinc_cmd
%{_bindir}/boinc-client
%{_bindir}/boinccmd
%{_bindir}/boinc_switcher
%{_bindir}/boinc-switcher
%{_mandir}/man1/boinccmd.1.xz
%{_mandir}/man1/boinc.1.xz
%{_mandir}/man1/boinc-client.1.xz
%dir %attr(0750, boinc, boinc) %{_localstatedir}/boinc
%attr(0644, boinc, boinc) %config(noreplace) %{_localstatedir}/boinc/remote_hosts.cfg

%files manager -f BOINC-Manager.lang
#%{_bindir}/boinc_gui
%{_bindir}/boincmgr
%{_datadir}/applications/boinc-manager.desktop
#%{_datadir}/locale/*/LC_MESSAGES/*.mo
%_datadir/boinc/boincmgr.*.png
%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png
%{_mandir}/man1/boincmgr.1.xz

%files manager-skins
%{_datadir}/boinc/skins

%files devel
%exclude %{_libdir}/libboinc*.a
%exclude %_libdir/libboinc_opencl.so
%exclude %_includedir/boinc/boinc_opencl.h
%{_libdir}/libboinc*.so
%dir %{_includedir}/boinc
%{_includedir}/boinc/*.h


%changelog
* Thu Feb 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.8.4-alt2
- Fixed build with new glibc.

* Tue Nov 28 2017 Ilya Mashkin <oddity@altlinux.ru> 7.8.4-alt1
- update to 7.8.4 Build prepared by Oleg Solovyov (mcpain)

* Fri Nov 24 2017 Ilya Mashkin <oddity@altlinux.ru> 7.4.42-alt2
- fix build

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 7.4.42-alt1.3
- Rebuilt for new gcc5 C++11 ABI.

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.4.42-alt1.2
- Rebuilt with gcc5

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.4.42-alt1.1
- Rebuilt with wxGTK3.1 (instead of wxGTK3.0) & gtk+3 (instead of gtk+2)

* Wed Mar 11 2015 Cronbuild Service <cronbuild@altlinux.org> 7.4.42-alt1
- Fresh up to v7.4.42 with the help of cronbuild and update-source-functions.

* Tue Mar 03 2015 Paul Wolneykien <manowar@altlinux.org> 7.4.41-alt1
- Fresh up to v7.4.41 with the help of cronbuild and update-source-functions.
- Disable building the server packages.
- Build with -std=gnu++11.

* Tue Apr 01 2014 Cronbuild Service <cronbuild@altlinux.org> 7.3.15-alt1
- Fresh up to v7.3.15 with the help of cronbuild and update-source-functions.

* Wed Mar 19 2014 Cronbuild Service <cronbuild@altlinux.org> 7.3.13-alt1
- Fresh up to v7.3.13 with the help of cronbuild and update-source-functions.

* Wed Mar 12 2014 Paul Wolneykien <manowar@altlinux.ru> 7.3.12-alt1
- Fresh up to v7.3.12 with the help of cronbuild and update-source-functions.

* Mon Feb 03 2014 Cronbuild Service <cronbuild@altlinux.org> 7.2.41-alt1
- Fresh up to v7.2.41 with the help of cronbuild and update-source-functions.

* Tue Jan 28 2014 Cronbuild Service <cronbuild@altlinux.org> 7.2.39-alt1
- Fresh up to v7.2.39 with the help of cronbuild and update-source-functions.

* Thu Jan 16 2014 Cronbuild Service <cronbuild@altlinux.org> 7.2.38-alt1
- Fresh up to v7.2.38 with the help of cronbuild and update-source-functions.

* Wed Jan 08 2014 Cronbuild Service <cronbuild@altlinux.org> 7.2.37-alt1
- Fresh up to v7.2.37 with the help of cronbuild and update-source-functions.

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 7.2.36-alt1
- Fresh up to v7.2.36 with the help of cronbuild and update-source-functions.

* Tue Dec 03 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.34-alt1
- Fresh up to v7.2.34 with the help of cronbuild and update-source-functions.

* Tue Nov 26 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.33-alt1
- Fresh up to v7.2.33 with the help of cronbuild and update-source-functions.

* Sat Nov 23 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.32-alt1
- Fresh up to v7.2.32 with the help of cronbuild and update-source-functions.

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.31-alt1
- Fresh up to v7.2.31 with the help of cronbuild and update-source-functions.

* Thu Nov 07 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.28-alt1
- Fresh up to v7.2.28 with the help of cronbuild and update-source-functions.

* Tue Nov 05 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.27-alt1
- Fresh up to v7.2.27 with the help of cronbuild and update-source-functions.

* Sat Oct 26 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.26-alt1
- Fresh up to v7.2.26 with the help of cronbuild and update-source-functions.

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.25-alt1
- Fresh up to v7.2.25 with the help of cronbuild and update-source-functions.

* Tue Oct 15 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.23-alt1
- Fresh up to v7.2.23 with the help of cronbuild and update-source-functions.

* Sat Oct 12 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.22-alt1
- Fresh up to v7.2.22 with the help of cronbuild and update-source-functions.

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.21-alt1
- Fresh up to v7.2.21 with the help of cronbuild and update-source-functions.

* Tue Oct 08 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.20-alt1
- Fresh up to v7.2.20 with the help of cronbuild and update-source-functions.

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.18-alt1
- Fresh up to v7.2.18 with the help of cronbuild and update-source-functions.

* Sun Sep 22 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.17-alt1
- Fresh up to v7.2.17 with the help of cronbuild and update-source-functions.

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.16-alt1
- Fresh up to v7.2.16 with the help of cronbuild and update-source-functions.

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.15-alt1
- Fresh up to v7.2.15 with the help of cronbuild and update-source-functions.

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.14-alt1
- Fresh up to v7.2.14 with the help of cronbuild and update-source-functions.

* Tue Aug 27 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.13-alt1
- Fresh up to v7.2.13 with the help of cronbuild and update-source-functions.

* Fri Aug 23 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.12-alt1
- Fresh up to v7.2.12 with the help of cronbuild and update-source-functions.

* Fri Aug 16 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.11-alt1
- Fresh up to v7.2.11 with the help of cronbuild and update-source-functions.

* Thu Aug 08 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.10-alt1
- Fresh up to v7.2.10 with the help of cronbuild and update-source-functions.

* Tue Aug 06 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.9-alt1
- Fresh up to v7.2.9 with the help of cronbuild and update-source-functions.

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.8-alt1
- Fresh up to v7.2.8 with the help of cronbuild and update-source-functions.

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.7-alt1
- Fresh up to v7.2.7 with the help of cronbuild and update-source-functions.

* Wed Jul 17 2013 Cronbuild Service <cronbuild@altlinux.org> 7.2.5-alt1
- Fresh up to v7.2.5 with the help of cronbuild and update-source-functions.

* Fri Jul 12 2013 Paul Wolneykien <manowar@altlinux.ru> 7.2.4-alt1
- Update the libadds patch.
- Fresh up to v7.2.4 with the help of cronbuild and update-source-functions.

* Thu Jun 27 2013 Paul Wolneykien <manowar@altlinux.ru> 7.2.0-alt1
- Fresh up to v7.2.0 with the help of cronbuild and update-source-functions.

* Fri May 31 2013 Paul Wolneykien <manowar@altlinux.org> 7.1.3-alt1
- Fresh up to v7.1.3 with the help of cronbuild and update-source-functions.

* Fri May 31 2013 Paul Wolneykien <manowar@altlinux.org> 7.0.34-alt1
- Fresh up to v7.0.34 with the help of cronbuild and update-source-functions.

* Fri May 31 2013 Paul Wolneykien <manowar@altlinux.org> 7.0.33-alt1
- Fresh up to v7.0.33 with the help of cronbuild and update-source-functions.

* Fri May 31 2013 Paul Wolneykien <manowar@altlinux.org> 7.0.32-alt1
- Fresh up to v7.0.32 with the help of cronbuild and update-source-functions.

* Mon Sep 10 2012 Paul Wolneykien <manowar@altlinux.ru> 7.0.31-alt3
- Fix/improve the version comparison proc.

* Sun Jul 15 2012 Paul Wolneykien <manowar@altlinux.ru> 7.0.31-alt2
- Install the remote host ACL template into the BOINC home directory.
- Do not install the configuration files into the /etc/boinc.

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 7.0.31-alt1
- repocop cronbuild 20120703. At your service.

* Wed Jun 27 2012 Cronbuild Service <cronbuild@altlinux.org> 7.0.30-alt1
- repocop cronbuild 20120627. At your service.

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 7.0.29-alt1
- repocop cronbuild 20120626. At your service.

* Sun Jun 10 2012 Paul Wolneykien <manowar@altlinux.ru> 7.0.27-alt1
- Make 'boincadm' groupadd more reliable (closes: 24577).
- Make -skins package noarch.
- Fix missing installation of the appmgr script.
- Add parse_test to the set of development tools.
- Add the -vda subpackage for the Volunteer Data Archival (VDA)
  network.
- Skip libboinc_opencl.so (no link target in Sisyphus).
- Pack language files for the BOINC client.
- Relink the sched_vda from libsched to cgi (fix undefined syms).
- Fix boinc_zip linkage (update libadds.patch).
- Re-enable the libadds.patch.
- Add -manager-skins subpackage.
- Add patch to make/install client GUI resources.
- Add libnotify-devel to the build requisite set.
- Add libgtk+2-devel to the build requisite set.
- Add patch fixing 'totalGlobalMem' field access.
- Update serverbindir.patch.
- Disable possibly outdated/applied libadds.patch.
- Remove already applied xpm-const-char.patch.
- Remove outdated use-peak-flops.patch.
- Remove already applied fix-crypt-prog-linkage.patch.
- Remove already applied 200_don-t-assume_SCHED_BATCH_exist.patch.
- Update sources with the help of bundled cronbuild scripts (closes: 27125).

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.10.58-alt2.qa2.1
- Rebuild with Python-2.7

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 6.10.58-alt2.qa2
- NMU: dropped obsolete menu entry; added desktop categories; fixed build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 6.10.58-alt2.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Sep 28 2010 Paul Wolneykien <manowar@altlinux.ru> 6.10.58-alt2
- Fix some of the repocop warnings:
  * library-pkgnames-static in -devel packages;
  * altlinux-policy-shared-lib-contains-devel-so in lib* packages;
  * altlinux-find-lang-mo in boinc-manager package;
  * freedesktop-desktop in boinc-manager package.

* Tue Jul 27 2010 Paul Wolneykien <manowar@altlinux.ru> 6.10.58-alt1
- Upgrade to new version 6.10.58 (ALT #23765, #23387)

* Wed Mar 10 2010 Ilya Mashkin <oddity@altlinux.ru> 6.4.5-alt4
- rebuild with current wxGTK

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 6.4.5-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for boinc
  * postclean-05-filetriggers for spec file

* Mon Dec 07 2009 Paul Wolneykien <manowar@altlinux.ru> 6.4.5-alt3
- Fix errors in the boinc-client init script (closes: 22066).
- Add README and COPYING files.
- Install the manual pages.

* Mon Jul 28 2009 Paul Wolneykien <manowar@altlinux.ru> 6.4.5-alt2
- + BOINC-server package.
- Repocop warnings on the version 6.4.5-alt1 fixed.

* Mon Jul 28 2009 Paul Wolneykien <manowar@altlinux.ru> 6.4.5-alt1
- Initial ALTLinux release.
