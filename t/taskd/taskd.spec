%define _unpackaged_files_terminate_build 1

%def_with check

Name:      taskd
Version:   1.1.0
Release:   alt1

Summary:   Taskserver - Taskwarrior Synchronisation Server
License:   MIT
Group:     System/Servers
Url:       https://github.com/GothenburgBitFactory/taskserver

Source:    %name-%version.tar
Source1:   %name.service
Source2:   %name.config
Source3:   %name.tmpfiles
Source4:   README.altlinux

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgnutls-devel
BuildRequires: libuuid-devel
BuildRequires: libnettle-devel
BuildRequires: libtasn1-devel
BuildRequires: libidn2-devel
BuildRequires: libp11-kit-devel
BuildRequires: zlib-devel

%description
The Taskserver is a lightweight, secure server providing multi-user,
multi-client access to task data.  This allows true syncing between
desktop and mobile clients.

Users want task list access from multiple devices running software of
differing sophistication levels to synchronize data seamlessly.
Synchronization requires the ability to exchange transactions between
devices that may not have continuous connectivity, and may not
havefeature parity.

The Taskserver provides this and builds a framework to go several steps
beyond merely synchronizing data.

%prep
%setup
cp %SOURCE4 README.altlinux

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
install -m644 -D %SOURCE1 %buildroot%_unitdir/%name.service
install -m755 -D pki/generate* -t %buildroot%_sysconfdir/pki/%name/
install -m644 -D pki/vars %buildroot%_sysconfdir/pki/%name/
install -m644 -D pki/README %buildroot%_sysconfdir/pki/%name/
install -m644 -D %SOURCE2 %buildroot%_localstatedir/%name/config
install -m644 -D %SOURCE3 %buildroot%_tmpfilesdir/%name.conf
mkdir -p %buildroot%_localstatedir/%name/orgs
mkdir -p %buildroot%_logdir/%name/

%check
cp %_cmake__builddir/test/run_all test/
pushd %_cmake__builddir
rm -rf test/version.t
%make test
popd

%pre
%_sbindir/groupadd -r -f %name 2> /dev/null ||:
%_sbindir/useradd -r -n -g %name -d %_localstatedir/%name -s /bin/bash \
        -c "User for %name" %name 2> /dev/null ||:

%files
%doc README README.altlinux INSTALL ChangeLog NEWS
%_bindir/*
%dir %attr(0750, %name, %name) %_sysconfdir/pki/%name/
%_sysconfdir/pki/%name/generate*
%_sysconfdir/pki/%name/README
%config(noreplace) %_sysconfdir/pki/%name/vars
%dir %attr(0750, %name, %name) %_logdir/%name/
%dir %attr(0750, %name, %name) %_localstatedir/%name/
%dir %attr(0750, %name, %name) %_localstatedir/%name/orgs/
%config(noreplace) %attr(0644, %name, %name) %_localstatedir/%name/config
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%exclude %_defaultdocdir/%name
%_man1dir/*
%_man5dir/*

%changelog
* Sat Nov 04 2023 Andrey Limachko <liannnix@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
