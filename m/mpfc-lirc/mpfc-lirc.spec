%define bname mpfc
%define Name MPFC
Name: %bname-lirc
Version: 0.1
Release: alt1
Summary: Lirc control plugin for %Name
License: %gpl2plus
Group: Sound
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-0.1-alt.patch

BuildRequires: libmpfc-devel liblirc-devel
BuildRequires: rpm-build-licenses

%description
lirc plugin allows you to control MPFC using a LIRC-compatible device.
This plugin works by mapping lirc events to mpfc actions.


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
%doc AUTHORS ChangeLog README
%dir %_libdir/%bname/general
%_libdir/%bname/general/*.so


%changelog
* Thu Oct 16 2008 Led <led@altlinux.ru> 0.1-alt1
- initial revision
