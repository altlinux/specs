Name: bubblewrap
Version: 0.1.5
Release: alt1

Summary: Unprivileged sandboxing tool

Group: System/Base
License: LGPLv2+
Url: https://github.com/projectatomic/bubblewrap

BuildPreReq: gcc-c++ binutils-devel libelf-devel

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/projectatomic/bubblewrap/releases/download/v%version/bubblewrap-%version.tar.xz
Source: %name-%version.tar

# manually removed: python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs 
# Automatically added by buildreq on Sun Aug 14 2016
# optimized out: docbook-dtds libgpg-error perl pkg-config python-base python-modules python3 python3-base xml-common
BuildRequires: db2latex-xsl docbook-style-xsl libcap-devel xsltproc

%description
Many container runtime tools like systemd-nspawn, docker, etc. focus on providing
infrastructure for system administrators and orchestration tools (e.g. Kubernetes) to run containers.

These tools are not suitable to give to unprivileged users,
because it is trivial to turn such access into to a fully privileged root shell on the host.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/bwrap
%_man1dir/bwrap*
%_datadir/bash-completion/completions/bwrap

%changelog
* Sat Dec 31 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- new version 0.1.4 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- new version 0.1.2 (with rpmrb script)

* Sun Aug 14 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux Sisyphus
