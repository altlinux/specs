Name: screen-message
Version: 0.6
Release: alt2

Summary: Screen message show given text in fullscreen
License: GPLv2+
Group: System/X11

Source: %name-%version.tar.gz
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libgtk+2-devel


%description
Screen message show given text in fullscreen

%prep
%setup
%patch0 -p2

%build
%configure
make

%install
make install DESTDIR=%buildroot
install -m 755 sm.py %buildroot%_bindir

%files
%_bindir/*
%_man1dir/*


%changelog
* Tue Mar 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt2
- Porting to python3.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt1
- Rebuild with new sisyphus_check
- Url tag removed (was dummy anyway)

* Thu Aug  2 2007 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt0
- Initial build for Sisyphus
