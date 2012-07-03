%define svnrevision	603
Name: libvmime
Version: 0.9.2
Release: alt5
Summary: Powerful library for MIME messages and Internet messaging services
Group: System/Libraries
License: GPLv3+
Url: http://www.vmime.org/
Packager: Radik Usupov <radik@altlinux.org>

Source: %name-%version.tar.bz2

Patch0: vmime-0.8.1-header-value-on-next-line.diff
Patch1: vmime-mixed-qp-in-parameter.diff
Patch2: vmime-0.9.2-qp-in-buffers.diff

# Path of the sendmail binary gets a C/C++ definement during build
BuildRequires: sendmail
BuildRequires: libgsasl-devel
BuildRequires: libgnutls-devel
BuildRequires: gcc-c++
BuildRequires: libgnutls-extra-devel
BuildRequires: libgcrypt-devel
BuildRequires: iconv

%description
VMime is a powerful C++ class library for working with MIME messages
and Internet messaging services like IMAP, POP or SMTP.

With VMime you can parse, generate and modify messages, and also
connect to store and transport services to receive or send messages
over the Internet. The library offers all the features to build a
complete mail client.

%package devel
Summary: Development headers for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: pkgconfig
Requires: libgsasl-devel
Requires: libgnutls-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export EXTRA_CFLAGS="-g -DVMIME_ALWAYS_GENERATE_7BIT_PARAMETER=1"
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_docdir/vmime
%_libdir/%name.so.*

%files devel
%_includedir/vmime/
%_libdir/%name.so
%_pkgconfigdir/vmime.pc

%changelog
* Tue Jun 12 2012 Radik Usupov <radik@altlinux.org> 0.9.2-alt5
- Added vmime-0.9.2-qp-in-buffers.diff
- Updated buildrequires

* Tue May 15 2012 Radik Usupov <radik@altlinux.org> 0.9.2-alt4
- Added always_generate_7bit_parameter option
- Added --disable-static option

* Tue Jan 24 2012 Radik Usupov <radik@altlinux.org> 0.9.2-alt3
- New upstreame snapshot (svn603)

* Fri Sep 30 2011 Radik Usupov <radik@altlinux.org> 0.9.2-alt2.svn581
- Added vmime-empty-bodypart.diff
- Added vmime-mixed-qp-in-parameter.diff

* Tue Mar 29 2011 Radik Usupov <radik@altlinux.org> 0.9.2-alt1.svn581
- initial build for ALT Linux Sisyphus
