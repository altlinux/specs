Name: kmscon
Version: 8
Release: alt2
Summary: KMS/DRM based System Console
Group: Terminals

License: MIT and LGPLv2+
Url: http://www.freedesktop.org/wiki/Software/kmscon/
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libtsm)
BuildRequires: pkgconfig(libudev) >= 172
BuildRequires: pkgconfig(libdrm)
BuildRequires: libsystemd-devel
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(pango) pkgconfig(pangoft2)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: xsltproc docbook-style-xsl docbook-dtds

%description
Kmscon is a simple terminal emulator based on Linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a user-space
console. See kmscon(1) man-page for usage information.

%prep
%setup
%patch1 -p1

%build
mkdir -p m4
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules \
	--with-renderers="bbulk,gltex,pixman"

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/%name/mod-*.la

# Install systemd services
mkdir -p %buildroot%_unitdir
install -pm 0644 docs/kmscon.service %buildroot%_unitdir
install -pm 0644 docs/kmsconvt@.service %buildroot%_unitdir

%check
%make check

%post
%post_service kmscon.service
#%%systemd_post kmsconvt@.service

%preun
%preun_service kmscon.service
# %%systemd_preun kmsconvt@.service

%files
%doc COPYING NEWS README
%_bindir/%name
%_unitdir/*.service
%dir %_libdir/%name
%_libdir/%name/mod-*.so
%_man1dir/%name.1*

%changelog
* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8-alt2
- Fixed build with new systemd and glibc.

* Tue Jun 17 2014 Alexey Shabalin <shaba@altlinux.ru> 8-alt1
- initial build
