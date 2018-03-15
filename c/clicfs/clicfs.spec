Name: clicfs
Version: 1.4.6
Release: alt2.1
Summary: Compressed Loop Image Container
License: GPLv2
Group: System/Kernel and hardware
Url: http://gitorious.org/opensuse/clicfs
Source: %name.tar
Patch: %name-%version-%release.patch
Requires: fuse >= 2.6

BuildRequires: cmake gcc-c++ libfuse-devel liblzma-devel libssl-devel

%description
Clic FS is a FUSE file system to mount a Compressed Loop Image Container.
It has several features that make it a good choice for live systems.
It will compress a Loop Image and export it as read write,
creating a copy on write behaviour.


%package utils
Summary: Clicfs utils
Group: System/Kernel and hardware
Provides: %name-tools = %version-%release

%description utils
Clic FS is a FUSE file system to mount a Compressed Loop Image Container.
It has several features that make it a good choice for live systems.
It will compress a Loop Image and export it as read write,
creating a copy on write behaviour.
This package contains utils for create, extract and check Clic FS.


%prep
%setup -q -n %name
%patch -p1


%build
%cmake_insource
%make_build


%install
%makeinstall_std


%files
%_bindir/%name
%_man1dir/%name.*


%files utils
%_bindir/*
%exclude %_bindir/%name
%_man1dir/*
%exclude %_man1dir/%name.*


%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt2.1
- NMU: added URL

* Tue Feb 05 2013 Led <led@altlinux.ru> 1.4.6-alt2
- fixed format strings for output

* Tue Feb 05 2013 Led <led@altlinux.ru> 1.4.6-alt1
- initial build
