%define bname mpfc
%define Name MPFC
Name: %bname-remote
Version: 0.1
Release: alt1
Summary: Remote interface for %Name
License: %gpl2plus
Group: Sound
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-0.1-alt.patch
Requires: mpfc

# Automatically added by buildreq on Wed Oct 15 2008
BuildRequires: glib-devel libmpfc-devel
BuildRequires: rpm-build-licenses

%description
Remote interface for %Name.


%prep
%setup
%patch -p1


%build
%autoreconf
%configure --enable-shared --disable-static --with-pic
%make_build -C src


%install
%make_install -C src DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog README
%dir %_libdir/%bname/general
%_libdir/%bname/general/*.so


%changelog
* Wed Oct 15 2008 Led <led@altlinux.ru> 0.1-alt1
- initial build
