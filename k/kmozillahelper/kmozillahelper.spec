%def_enable hackaround

Name:           kmozillahelper
Version:        0.6.3
Release:        alt1

Group:          Graphical desktop/KDE
Summary:        Mozilla KDE Integration
License:        X11/MIT

%define helper_version 6
%if_enabled hackaround
%define helper_version 5
%endif
Requires: xulrunner-kde4-version = %{helper_version}

Source:         %name-%version.tar
Patch1: kmozillahelper-0.6-alt-set-def-browser.patch
Patch2: kmozillahelper-0.5-alt-install-program.patch

BuildRequires: gcc-c++ kde4libs-devel

%description
Package providing integration of Mozilla applications with KDE.

%prep
%setup -q
%patch1 -p1
%patch2 -p1


%build
%if_enabled hackaround
%else
  version=$(cat main.cpp | grep '#define HELPER_VERSION' | cut -d ' ' -f 3)
  if test "$version" != %{helper_version}; then
      echo fix the version in the .spec file
      exit 1
  fi
%endif
%K4build


%install
%K4install


%files
%_bindir/kmozillahelper
%_K4apps/kmozillahelper


%changelog
* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- new version

* Mon Sep 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt0.M51.1
- built for M51

* Mon Sep 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Fri Mar 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.6-alt1
- new version

* Fri Oct 16 2009 Sergey V Turchin <zerg@altlinux.org> 0.5-alt3
- fix check for default browser

* Thu Oct 15 2009 Alexey Gladkov <legion@altlinux.ru> 0.5-alt2
- Move kmozillahelper to %%_bindir.

* Thu Sep 24 2009 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- new version

* Thu Sep 17 2009 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- initial spec

