%define realname gkeyfile-sharp

Name: lib%{realname}
Version: 0.2
Release: alt1
Summary: C# bindings for glib2's keyfile implementation
Group: Development/Other
License: LGPLv2
Url: http://github.com/mono/%name
# Releases are tarballs downloaded from a tag at github.
# They are releases, but the file is generated on the fly.
# The actual URL is: http://github.com/mono/$name/tarball/$tagname

Source: %name-%version.tar
# Patch: %name-%version-%release.patch

BuildRequires: glib2-devel
BuildRequires: libgtk-sharp2-devel libgtk-sharp2-gapi
BuildRequires: rpm-build-mono mono-devel mono-mcs
BuildRequires: /proc


%package devel
Summary: Development files for gkeyfile-sharp
Group: Development/Other
Requires: %name = %version-%release

%description
C# bindings for glib2's keyfile implementation

%description devel
Development files for gkeyfile-sharp

%prep
%setup -q

%build
./autogen.sh
%configure
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_monodir/%realname/*.dll.config

%files
%doc AUTHORS ChangeLog LICENSE.LGPL NEWS
%_monodir/%realname
%_monogacdir/*

%files devel
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- initial build
