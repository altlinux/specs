
%define family Iosevka

Name:    %family-source
Version: 34.7.0
Release: alt1

Summary: Versatile typeface for code -- the sources
License: OFL-1.1
Group:   System/Fonts/True type
Url:     https://github.com/be5invis/Iosevka

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source0:  %family-%version.tar
Source1:  node_modules.tar
Source2:  %family-%version-%release.patch

BuildArch: noarch

%description
Iosevka is an open-source multi-variant typeface family, designed
for writing code, using in terminals, and preparing technical documents.

Iosevka is completely generated from its source code. This package
contains the source code and vendored node_modules that are used
to build the actual packages with the font.

%install
mkdir -p %buildroot%_usrsrc/%family
cp %SOURCE0 %SOURCE1 %SOURCE2 %buildroot%_usrsrc/%family/

%files
%_usrsrc/%family

%changelog
* Mon Jun 29 2026 Ivan A. Melnikov <iv@altlinux.org> 34.7.0-alt1
- 34.7.0

* Mon May 25 2026 Ivan A. Melnikov <iv@altlinux.org> 34.6.1-alt1
- 34.6.1

* Sat May 09 2026 Ivan A. Melnikov <iv@altlinux.org> 34.5.0-alt1
- 34.5.0

* Sun Apr 19 2026 Ivan A. Melnikov <iv@altlinux.org> 34.4.0-alt1
- 34.4.0

* Tue Mar 03 2026 Ivan A. Melnikov <iv@altlinux.org> 34.2.1-alt1
- 34.2.1

* Sun Mar 01 2026 Ivan A. Melnikov <iv@altlinux.org> 34.2.0-alt1
- 34.2.0

* Sat Jan 24 2026 Ivan A. Melnikov <iv@altlinux.org> 34.1.0-alt1
- 34.1.0

* Sat Jan 03 2026 Ivan A. Melnikov <iv@altlinux.org> 34.0.0-alt1
- 34.0.0

* Thu Dec 11 2025 Ivan A. Melnikov <iv@altlinux.org> 33.3.6-alt1
- 33.3.6

* Thu Dec 04 2025 Ivan A. Melnikov <iv@altlinux.org> 33.3.5-alt1
- build a separate source package (inspired by kernel-source-*)
