%define build_static 1

%if %_vendor == "alt"
%define bzip2lib bzlib-devel
%else
%define bzip2lib bzip2-devel
%endif

Summary: Binkd - the binkp daemon
Name: binkd
Version: 1.1a.99
Release: alt1
License: GPL
Group: Networking/FTN
Source: %name-%version.tar.xz
URL: https://github.com/pgul/binkd
BuildRoot: %_tmppath/%name-%version-root
%if %build_static
BuildRequires: glibc-devel-static zlib-devel-static %bzip2lib-static
%else
BuildRequires: zlib-devel %bzip2lib perl-devel
%endif

%description
Binkd is the daemon for FTN communications over reliable links.


%prep
%setup
cp -p mkfls/unix/{Makefile*,configure.in,install-sh,mkinstalldirs} ./
%if %build_static
sed -i -re '/THREADS/d' configure.in
%endif


%build
%if %build_static
export LDFLAGS="-s -static"
%endif

%autoreconf
%configure \
  --with-proxy \
  --without-ntlm \
  --with-bwlim \
  --with-perl \
  --with-zlib \
  --with-bzip2 \
  ;
%make


%install
rm -rf %buildroot
%make DESTDIR=%buildroot install
rm -rf %buildroot%_sysconfdir


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%_sbindir/%{name}*
%_man8dir/%{name}.*


%changelog
* Sun Mar 10 2019 Gremlin from Kremlin <gremlin@altlinux.org> 1.1a.99-alt1
- import from upstream, first build for ALT Linux

