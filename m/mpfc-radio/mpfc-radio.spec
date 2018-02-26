%define bname mpfc
%define Name MPFC
Name: %bname-radio
Version: 0.1
Release: alt2
Summary: Radio input plugin for %Name
License: %gpl2plus
Group: Sound
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-0.1-alt.patch

BuildRequires: libmpfc-devel
BuildRequires: rpm-build-licenses

%description
Radio input plugin for %Name.


%prep
%setup
%patch -p1


%build
%autoreconf
%configure --enable-shared --disable-static --with-pic
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS
%_libdir/%bname/input/*.so


%changelog
* Thu Oct 16 2008 Led <led@altlinux.ru> 0.1-alt2
- remove alien README

* Thu Oct 16 2008 Led <led@altlinux.ru> 0.1-alt1
- initial revision
