%define module mageia-compat
Name: rpm-macros-%module
Summary: Mageia compatibility set of macro
Version: 0.061
Release: alt1
License: GPLv2+
Group: System/Base
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %name-%version.tar
Requires: rpm-macros-generic-compat
Patch: mageia-compat.patch

%description
%summary

%prep
%setup
%patch -p0

%install
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module-base
for ext in cmake qt4 qt5 qt6 ; do
    install -D -m644 orig/macros.$ext -p %buildroot%_rpmmacrosdir/%module-$ext
done
for ext in scons ; do
    install -D -m644 orig/$ext.macros -p %buildroot%_rpmmacrosdir/%module-$ext
done

%files
%_rpmmacrosdir/*

%changelog
* Mon Oct 02 2023 Igor Vlasenko <viy@altlinux.org> 0.061-alt1
- added qt6 support

* Mon Nov 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.060-alt1
- added _rundir

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.059-alt1
- set _vpath_builddir to build

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.058-alt1
- updated mageia cmake

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.057-alt1
- added %%_metainfodir

* Mon Mar 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.056-alt1
- ctest macros

* Sat Oct 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.055-alt1
- added kf5 compat macros

* Fri Oct 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.054-alt1
- added %%perl_convert_version

* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.053-alt1
- more macros from 20build.macros

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.052-alt1
- added Requires: rpm-macros-generic-compat

* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.051-alt1
- added %%arch_tagged

* Fri Feb 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added rename from mageia

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- cmake fixes

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added qt4

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added qt5 && scons macros

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
