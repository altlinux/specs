
Name: qmergeinifiles
Version: 2.0.0
Release: alt1


Summary: Utility to merge INI-format files
Group: Development/Other
License: GPL

Requires: libqt4-core >= %{get_version libqt4-core}

Source: %name-%version.tar

BuildRequires(pre): libqt4-core
BuildRequires: gcc-c++ libqt4-devel libstdc++-devel

%description
Utility to merge INI-format files


%prep
%setup -q
qmake-qt4 -spec default

%build
%make_build CUSTOM_OPT_FLAGS="%optflags"

%install
%make INSTALL_ROOT=%buildroot install


%files
%_bindir/*

%changelog
* Fri Feb 10 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version

* Fri Oct 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.91.0-alt0.M60P.1
- built for M60P

* Thu Oct 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.91.0-alt1
- create General section only if exists according settings

* Wed Oct 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.90.0-alt1
- rewrite to merge without recoding text

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- fix compile with new Qt

* Fri Nov 09 2007 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial specfile

