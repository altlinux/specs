%def_enable glx
%def_disable valgrind
%def_disable tracer

Name: xvba-video
Version: 0.8.0
Release: alt3
Summary: XvBA-based backend for VA-API
Group: System/Libraries
License: GPLv2+
Url: http://www.splitted-desktop.com/~gbeauchesne/%name/
Source: %name.tar
Patch1: %name-h264-level51.patch
Patch2: %name-GL_GLEXT_VERSION-85-fix.patch
Patch3: %name-%version-glx-fix.patch
Patch4: %name-%version-va-0.34.0.patch

BuildRequires: pkgconfig(libva) libX11-devel libXext-devel libGL-devel libxvba-devel python-base libdrm-devel
%{?_enable_valgrind:BuildRequires: pkgconfig(valgrind)}

%description
This is the XvBA-based backend for VA-API to use the hardware acceleration.


%prep
%setup -q -n %name
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1


%build
./autogen.sh
%configure \
	%{subst_enable glx} \
	%{subst_enable valgrind} \
	%{subst_enable tracer} \
	--disable-debug \
	--with-gnu-ld
%make_build


%install
%makeinstall_std
%define driverdir %(pkg-config libva --variable driverdir)


%files
%doc AUTHORS NEWS README
%driverdir/*.so
%exclude %driverdir/*.la


%changelog
* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt3
- Updated build dependencies

* Tue Feb 04 2014 Led <led@altlinux.ru> 0.8.0-alt2
- add compat to va 0.34.0 API

* Tue Jun 25 2013 Led <led@altlinux.ru> 0.8.0-alt1
- initial build
