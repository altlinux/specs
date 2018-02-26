%define realname gudev-sharp

Name: lib%{realname}
Version: 0.2
Release: alt1
Summary: C# bindings for gudev
Group: Development/Other
License: LGPLv2
Url: http://github.com/mono/%name
# Releases are tarballs downloaded from a tag at github.
# They are releases, but the file is generated on the fly.
# The actual URL is: http://github.com/mono/$name/tarball/$tagname
Source: %name-%version.tar
# Patch: %name-%version-%release.patch

BuildRequires: libgudev-devel libgtk+2-devel
BuildRequires: libgtk-sharp2-devel libgtk-sharp2-gapi mono-devel mono-mcs
BuildRequires: rpm-build-mono
BuildRequires: /proc

%package devel
Summary: Development files for gudev-sharp
Group: Development/Other
Requires: %name = %version-%release

%description
C# bindings for gudev

%description devel
Development files for gudev-sharp

%prep
%setup -q

%build
./autogen.sh
%configure
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_monodir/%realname-1.0/*.dll.config

%files
%doc AUTHORS ChangeLog LICENSE.LGPL NEWS
%_monodir/%realname-1.0
%_monogacdir/*

%files devel
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- initial build
