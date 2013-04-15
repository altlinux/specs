%define bname mpfc
%define Name MPFC
Name: %bname-cue
Version: 0.1
Release: alt2.qa1
Summary: CUE sheets support plugin for %Name
License: %gpl2plus
Group: Sound
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-0.1-alt.patch
Requires: mpfc

BuildRequires: libmpfc-devel
BuildRequires: rpm-build-licenses

%description
CUE sheets support plugin for %Name.


%prep
%setup
%patch -p1


%build
%autoreconf
%configure --enable-shared --disable-static --with-pic
%make_build LDFLAGS=-avoid-version


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS README
%_libdir/%bname/input/*.so


%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Sep 24 2008 Led <led@altlinux.ru> 0.1-alt2
- rebuild with lib%bname.so.0

* Wed Aug 13 2008 Led <led@altlinux.ru> 0.1-alt1
- initial build
